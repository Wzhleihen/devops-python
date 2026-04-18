#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
from dataclasses import dataclass
from pathlib import Path
from typing import Any

GROUP_RE = re.compile(r"^##\s+(\d+)\.\s+(.+?)\s*$")
TASK_RE = re.compile(r"^- \[( |x|X)\]\s+(\d+\.\d+)\s+(.+?)\s*$")
ANY_CHECKBOX_RE = re.compile(r"^-\s*\[([^\]]*)\]\s+(.+?)\s*$")
DEP_BLOCK_RE = re.compile(r"(?:\(|（)?\s*(?:depends?\s*[:：]|依赖\s*[:：])\s*([^\)）]+)(?:\)|）)?", re.IGNORECASE)
DEP_REF_RE = re.compile(r"\d+\.\d+")


@dataclass
class TaskItem:
    ref: str
    title: str
    done: bool
    group_no: int
    group_title: str
    line_no: int
    deps: list[str]


def resolve_repo_root(start: Path) -> Path:
    current = start.resolve()
    for parent in [current, *current.parents]:
        if (parent / "openspec").exists() and (parent / ".git").exists():
            return parent
    raise FileNotFoundError("Cannot locate repository root from current path")


def infer_stage(task: TaskItem) -> str:
    text = f"{task.group_title} {task.title}".lower()
    if task.group_no == 1 or any(k in text for k in ["检索", "标准化", "cursor", "change events"]):
        return "变更检索与标准化"
    if task.group_no == 2 or any(k in text for k in ["day", "模板", "timeline"]):
        return "Day生成"
    if task.group_no == 3 or any(k in text for k in ["练习", "训练", "practice"]):
        return "练习生成"
    if task.group_no == 4 or any(k in text for k in ["评估", "评分", "recommend"]):
        return "能力评估"
    if task.group_no == 5 or any(k in text for k in ["校验", "集成", "quality", "dry-run"]):
        return "质量校验与集成"
    return "未分组"


def parse_deps(title: str) -> tuple[str, list[str]]:
    deps: list[str] = []
    cleaned = title
    match = DEP_BLOCK_RE.search(title)
    if match:
        deps = DEP_REF_RE.findall(match.group(1))
        cleaned = (title[: match.start()] + title[match.end() :]).strip()
    return cleaned, deps


def parse_tasks(tasks_path: Path) -> dict[str, Any]:
    lines = tasks_path.read_text(encoding="utf-8").splitlines()
    current_group_no = 0
    current_group_title = "未命名分组"
    tasks: list[TaskItem] = []
    malformed_status_lines: list[dict[str, Any]] = []
    unparsed_task_lines: list[dict[str, Any]] = []

    for i, raw in enumerate(lines, start=1):
        line = raw.rstrip("\n")
        group_match = GROUP_RE.match(line)
        if group_match:
            current_group_no = int(group_match.group(1))
            current_group_title = group_match.group(2).strip()
            continue

        task_match = TASK_RE.match(line)
        if task_match:
            done = task_match.group(1).lower() == "x"
            ref = task_match.group(2)
            title, deps = parse_deps(task_match.group(3).strip())
            tasks.append(
                TaskItem(
                    ref=ref,
                    title=title,
                    done=done,
                    group_no=current_group_no,
                    group_title=current_group_title,
                    line_no=i,
                    deps=deps,
                )
            )
            continue

        if line.strip().startswith("-"):
            any_checkbox = ANY_CHECKBOX_RE.match(line)
            if any_checkbox:
                marker = any_checkbox.group(1).strip()
                if marker not in {"", "x", "X"}:
                    malformed_status_lines.append({"line": i, "text": line})
            elif line.strip().startswith("- ["):
                malformed_status_lines.append({"line": i, "text": line})
            else:
                stripped = line.strip()
                if stripped and stripped not in {"-", "- "}:
                    unparsed_task_lines.append({"line": i, "text": line})

    return {
        "tasks": tasks,
        "malformed_status_lines": malformed_status_lines,
        "unparsed_task_lines": unparsed_task_lines,
    }


def validate_numbering(tasks: list[TaskItem]) -> list[str]:
    issues: list[str] = []
    by_group: dict[int, list[int]] = {}
    for t in tasks:
        major, minor = t.ref.split(".")
        by_group.setdefault(int(major), []).append(int(minor))

    for group_no in sorted(by_group):
        minors = sorted(by_group[group_no])
        expected = list(range(1, len(minors) + 1))
        if minors != expected:
            issues.append(
                f"分组 {group_no} 的任务编号不连续，实际 {minors}，期望 {expected}"
            )

    if by_group:
        group_numbers = sorted(by_group)
        expected_group_numbers = list(range(min(group_numbers), max(group_numbers) + 1))
        if group_numbers != expected_group_numbers:
            issues.append(
                f"分组编号不连续，实际 {group_numbers}，期望 {expected_group_numbers}"
            )

    return issues


def summarize(tasks: list[TaskItem], malformed: list[dict[str, Any]], unparsed: list[dict[str, Any]]) -> dict[str, Any]:
    all_refs = {t.ref for t in tasks}
    total = len(tasks)
    complete = sum(1 for t in tasks if t.done)
    pending = total - complete
    completion_rate = round((complete / total * 100.0), 2) if total else 0.0

    stage_map: dict[str, list[TaskItem]] = {}
    for t in tasks:
        stage_map.setdefault(infer_stage(t), []).append(t)

    stage_stats = {}
    for stage, items in stage_map.items():
        c = sum(1 for i in items if i.done)
        p = len(items) - c
        stage_stats[stage] = {
            "total": len(items),
            "complete": c,
            "pending": p,
            "completion_rate": round((c / len(items) * 100.0), 2) if items else 0.0,
            "tasks": [
                {
                    "ref": i.ref,
                    "title": i.title,
                    "done": i.done,
                    "deps": i.deps,
                    "line": i.line_no,
                }
                for i in sorted(items, key=lambda x: tuple(map(int, x.ref.split("."))))
            ],
        }

    unresolved_deps: list[dict[str, Any]] = []
    ready_candidates: list[TaskItem] = []
    for t in sorted(tasks, key=lambda x: tuple(map(int, x.ref.split(".")))):
        if t.done:
            continue
        missing_refs = [d for d in t.deps if d not in all_refs]
        if missing_refs:
            unresolved_deps.append(
                {"task": t.ref, "missing": missing_refs, "line": t.line_no}
            )
            continue
        unmet = [d for d in t.deps if d in all_refs and not next(i for i in tasks if i.ref == d).done]
        if not unmet:
            ready_candidates.append(t)

    recommendations = []
    for t in ready_candidates[:5]:
        reason = "依赖已满足，可立即执行" if t.deps else "无显式依赖，按顺序可执行"
        recommendations.append({"task": t.ref, "title": t.title, "reason": reason})

    numbering_issues = validate_numbering(tasks)

    blocking_issues = []
    warnings = []
    if malformed:
        blocking_issues.append(f"发现 {len(malformed)} 条状态语法非法的复选框行")
    if unresolved_deps:
        blocking_issues.append(f"发现 {len(unresolved_deps)} 个不可解析的依赖引用")
    if numbering_issues:
        warnings.extend(numbering_issues)
    if unparsed:
        warnings.append(f"发现 {len(unparsed)} 行未识别任务条目")

    return {
        "status": {
            "total": total,
            "complete": complete,
            "pending": pending,
            "completion_rate": completion_rate,
        },
        "stage_stats": stage_stats,
        "recommendations": recommendations,
        "validation": {
            "blocking_issues": blocking_issues,
            "warnings": warnings,
            "details": {
                "malformed_status_lines": malformed,
                "unresolved_dependencies": unresolved_deps,
                "numbering_issues": numbering_issues,
                "unparsed_task_lines": unparsed,
            },
        },
    }


def render_markdown(change: str, tasks_path: Path, data: dict[str, Any]) -> str:
    s = data["status"]
    lines = [
        f"# 任务清单摘要：{change}",
        "",
        f"来源：`{tasks_path.as_posix()}`",
        "",
        "## 总览",
        f"- 总任务数：{s['total']}",
        f"- 已完成：{s['complete']}",
        f"- 未完成：{s['pending']}",
        f"- 完成率：{s['completion_rate']}%",
        "",
        "## 分阶段统计",
    ]

    for stage, stage_data in data["stage_stats"].items():
        lines.extend(
            [
                f"### {stage}",
                f"- 统计：{stage_data['complete']}/{stage_data['total']}（{stage_data['completion_rate']}%）",
            ]
        )
        for task in stage_data["tasks"]:
            box = "x" if task["done"] else " "
            dep_text = f" | 依赖: {', '.join(task['deps'])}" if task["deps"] else ""
            lines.append(f"- [{box}] {task['ref']} {task['title']}{dep_text}")
        lines.append("")

    lines.append("## 下一步建议")
    if data["recommendations"]:
        for item in data["recommendations"]:
            lines.append(f"- {item['task']} {item['title']}（{item['reason']}）")
    else:
        lines.append("- 当前无可执行候选（可能全部完成或存在阻塞）")
    lines.append("")

    lines.append("## 一致性校验")
    validation = data["validation"]
    if validation["blocking_issues"]:
        lines.append("### 阻塞问题")
        for issue in validation["blocking_issues"]:
            lines.append(f"- {issue}")
    else:
        lines.append("- 阻塞问题：无")

    if validation["warnings"]:
        lines.append("### 警告")
        for issue in validation["warnings"]:
            lines.append(f"- {issue}")
    else:
        lines.append("- 警告：无")

    return "\n".join(lines).strip() + "\n"


def main() -> None:
    parser = argparse.ArgumentParser(description="Summarize OpenSpec tasks.md with status/grouping/recommendations/validation")
    parser.add_argument("--change", required=True, help="OpenSpec change name")
    parser.add_argument("--format", choices=["markdown", "json"], default="markdown")
    parser.add_argument("--output", help="Optional output file path")
    args = parser.parse_args()

    script_path = Path(__file__)
    repo_root = resolve_repo_root(script_path.parent)
    tasks_path = repo_root / "openspec" / "changes" / args.change / "tasks.md"
    if not tasks_path.exists():
        raise FileNotFoundError(f"tasks.md not found: {tasks_path}")

    parsed = parse_tasks(tasks_path)
    data = summarize(parsed["tasks"], parsed["malformed_status_lines"], parsed["unparsed_task_lines"])

    if args.format == "json":
        output_text = json.dumps(data, ensure_ascii=False, indent=2)
    else:
        output_text = render_markdown(args.change, tasks_path, data)

    if args.output:
        out_path = Path(args.output)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        out_path.write_text(output_text, encoding="utf-8")
    else:
        print(output_text)


if __name__ == "__main__":
    main()

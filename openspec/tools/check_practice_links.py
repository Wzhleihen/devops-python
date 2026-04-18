#!/usr/bin/env python3
from __future__ import annotations

import json
import re
from pathlib import Path

PRACTICE_RE = re.compile(r"`(practice/[^`]+/p-\d{3}-[a-z0-9-]+\.md)`")
ANSWER_RE = re.compile(r"`(answers/[^`]+/p-\d{3}-[a-z0-9-]+\.answer\.md)`")
QUESTION_RE = re.compile(r"^p-(\d{3})-([a-z0-9-]+)\.md$")
ANSWER_FILE_RE = re.compile(r"^p-(\d{3})-([a-z0-9-]+)\.answer\.md$")


def collect_files(root: Path, prefix: str) -> list[Path]:
    base = root / prefix
    if not base.exists():
        return []
    return sorted([p for p in base.rglob("*.md") if p.is_file() and p.name != "README.md"])


def pair_key_from_question(path: Path):
    m = QUESTION_RE.match(path.name)
    if not m:
        return None
    return m.group(1), m.group(2)


def pair_key_from_answer(path: Path):
    m = ANSWER_FILE_RE.match(path.name)
    if not m:
        return None
    return m.group(1), m.group(2)


def main() -> None:
    repo = Path(__file__).resolve().parents[2]

    practice_files = collect_files(repo, "practice")
    answer_files = collect_files(repo, "answers")

    question_keys = {}
    answer_keys = {}
    duplicate_question_keys = []
    duplicate_answer_keys = []
    invalid_question_names = []
    invalid_answer_names = []

    for p in practice_files:
        key = pair_key_from_question(p)
        if not key:
            invalid_question_names.append(str(p.relative_to(repo)).replace("\\", "/"))
            continue
        chapter = p.parts[len((repo / "practice").parts)]
        scoped = (chapter, key[0], key[1])
        if scoped in question_keys:
            duplicate_question_keys.append({"key": scoped, "files": [question_keys[scoped], str(p.relative_to(repo)).replace("\\", "/")]})
        question_keys[scoped] = str(p.relative_to(repo)).replace("\\", "/")

    for p in answer_files:
        key = pair_key_from_answer(p)
        if not key:
            invalid_answer_names.append(str(p.relative_to(repo)).replace("\\", "/"))
            continue
        chapter = p.parts[len((repo / "answers").parts)]
        scoped = (chapter, key[0], key[1])
        if scoped in answer_keys:
            duplicate_answer_keys.append({"key": scoped, "files": [answer_keys[scoped], str(p.relative_to(repo)).replace("\\", "/")]})
        answer_keys[scoped] = str(p.relative_to(repo)).replace("\\", "/")

    missing_answers = []
    for scoped, qpath in question_keys.items():
        if scoped not in answer_keys:
            missing_answers.append({"question": qpath, "expected_answer_key": scoped})

    orphan_answers = []
    for scoped, apath in answer_keys.items():
        if scoped not in question_keys:
            orphan_answers.append({"answer": apath, "expected_question_key": scoped})

    day_files = sorted((repo / "daily").glob("day*.md")) if (repo / "daily").exists() else []
    missing_link_paths = []
    for day in day_files:
        content = day.read_text(encoding="utf-8")
        refs = PRACTICE_RE.findall(content) + ANSWER_RE.findall(content)
        for ref in refs:
            if not (repo / ref).exists():
                missing_link_paths.append({"day": str(day.relative_to(repo)).replace("\\", "/"), "path": ref})

    report = {
        "summary": {
            "practice_files": len(practice_files),
            "answer_files": len(answer_files),
            "missing_answers": len(missing_answers),
            "orphan_answers": len(orphan_answers),
            "invalid_question_names": len(invalid_question_names),
            "invalid_answer_names": len(invalid_answer_names),
            "duplicate_question_keys": len(duplicate_question_keys),
            "duplicate_answer_keys": len(duplicate_answer_keys),
            "missing_link_paths": len(missing_link_paths),
        },
        "details": {
            "missing_answers": missing_answers,
            "orphan_answers": orphan_answers,
            "invalid_question_names": invalid_question_names,
            "invalid_answer_names": invalid_answer_names,
            "duplicate_question_keys": duplicate_question_keys,
            "duplicate_answer_keys": duplicate_answer_keys,
            "missing_link_paths": missing_link_paths,
        },
    }

    print(json.dumps(report, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

# Final Acceptance Checklist

## Directory Completeness
- [x] `practice/<章节>/{foundation,advanced,transfer}` skeleton created
- [x] `answers/<章节>/{foundation,advanced,transfer}` skeleton created

## Naming Compliance
- [x] Practice files follow `p-xxx-topic.md`
- [x] Answer files follow `p-xxx-topic.answer.md`
- [x] No duplicate question IDs within same chapter

## Linkage Integrity
- [x] Every practice file has paired answer file
- [x] No orphan answer files
- [x] Day training links point to existing `practice/` and `answers/` files

## Scope Constraint
- [x] Archive structure unchanged ("归档先不用写" preserved)

## Evidence
- Validation report: `openspec/changes/chapter-practice-and-training-template/acceptance_report.json`
- Link checker: `openspec/tools/check_practice_links.py`

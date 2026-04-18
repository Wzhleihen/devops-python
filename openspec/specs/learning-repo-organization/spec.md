# learning-repo-organization Specification

## Purpose
TBD - created by archiving change standardize-learning-repo-structure. Update Purpose after archive.
## Requirements
### Requirement: Repository SHALL use a stable top-level learning layout
The repository SHALL maintain a stable top-level structure for learning workflows, including `归档/` for historical date-based content, `daily/` for learning summaries, and existing Chinese chapter directories as primary topic entry points.

#### Scenario: Top-level structure is present
- **WHEN** a contributor inspects the repository root
- **THEN** they MUST find `归档/` and `daily/` at the root
- **AND** existing chapter directories (e.g., `07_面向对象`, `文件IO`) MUST remain available as top-level entries

### Requirement: Date-based directories SHALL be centralized under archive
All historical date-based directories in `YYYY-MM-DD` format SHALL be centralized under `归档/2025/` for this migration scope, and malformed date directory names MUST be corrected during migration.

#### Scenario: Date directories are migrated and corrected
- **WHEN** the migration is completed
- **THEN** date directories previously at root MUST exist under `归档/2025/`
- **AND** malformed `20225-12-04` MUST be stored as `归档/2025/2025-12-04`

### Requirement: Chapter internal files SHALL remain unchanged in this change
This change SHALL NOT move, rename, or modify files inside chapter directories.

#### Scenario: Chapter contents remain intact
- **WHEN** chapter directories are compared before and after migration
- **THEN** internal file paths and file contents under chapter roots MUST remain unchanged

### Requirement: Daily directory SHALL be created without enforced content template
The `daily/` directory SHALL be created as the future entry point for `dayxx.md` summaries, but this change MUST NOT enforce a final day template.

#### Scenario: Daily entry point exists with deferred template planning
- **WHEN** the migration is completed
- **THEN** `daily/` MUST exist at repository root
- **AND** no mandatory day content schema is required by this change


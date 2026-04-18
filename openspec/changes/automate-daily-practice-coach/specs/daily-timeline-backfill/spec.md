## MODIFIED Requirements

### Requirement: System SHALL build a complete daily timeline from full Git history
The system SHALL support both baseline backfill and ongoing incremental updates for daily timeline construction, using full Git history for initialization and cursor-based processing for subsequent runs.

#### Scenario: Baseline then incremental timeline workflow
- **WHEN** the system runs for the first time
- **THEN** it MUST build a full baseline from available Git history
- **AND** subsequent runs MUST process only changes newer than the stored cursor

### Requirement: System SHALL generate daily draft files using the approved template
The system SHALL generate `daily/dayxx.md` outputs through the unified pipeline and ensure generated content can be enriched with linked practice tasks and assessment references.

#### Scenario: Integrated day output
- **WHEN** a day file is generated or updated
- **THEN** required template sections MUST be present
- **AND** the day output MUST include links or references to generated practice and assessment artifacts

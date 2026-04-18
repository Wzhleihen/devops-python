## ADDED Requirements

### Requirement: System SHALL detect new code changes incrementally
The system SHALL detect unprocessed code changes from Git history using an incremental cursor and produce a normalized change event set.

#### Scenario: Incremental change detection
- **WHEN** the pipeline runs
- **THEN** only commits newer than the stored cursor MUST be selected
- **AND** selected changes MUST be transformed into structured events

### Requirement: System SHALL generate or update day documents from change events
The system SHALL generate or update `daily/dayxx.md` entries based on structured change events and the approved day template.

#### Scenario: Day document generation
- **WHEN** structured change events are available
- **THEN** the pipeline MUST create or update the target day file
- **AND** required template sections MUST be filled or explicitly marked as placeholder

### Requirement: System SHALL attach chapter mappings and code path backlinks
The system SHALL map each change event to chapter context and include code path backlinks in generated day content.

#### Scenario: Chapter and backlink injection
- **WHEN** a day file is generated
- **THEN** the output MUST include chapter fields
- **AND** referenced code paths MUST be included in backlink sections

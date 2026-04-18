## ADDED Requirements

### Requirement: System SHALL generate practice tasks from daily change context
The system SHALL generate at least one practice task for each processed day based on change semantics and chapter mapping.

#### Scenario: Practice task generation
- **WHEN** day generation completes
- **THEN** the system MUST produce at least one related practice task
- **AND** each task MUST reference relevant chapter context

### Requirement: System SHALL support tiered difficulty levels
The system SHALL support practice difficulty tiers (foundation, advanced, transfer) and assign tier labels to generated tasks.

#### Scenario: Tiered output
- **WHEN** practice tasks are generated
- **THEN** each task MUST include a difficulty tier label
- **AND** the output set MAY include one or more tiers per run

### Requirement: System SHALL include verifiable acceptance criteria
Each generated practice task SHALL include concrete acceptance criteria so completion can be objectively checked.

#### Scenario: Acceptance criteria present
- **WHEN** a task is emitted
- **THEN** it MUST include acceptance criteria
- **AND** criteria MUST be specific enough to validate completion

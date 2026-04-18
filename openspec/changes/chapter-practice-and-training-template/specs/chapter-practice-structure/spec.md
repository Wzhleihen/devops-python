## ADDED Requirements

### Requirement: System SHALL provide chapter-based practice and answer directories
The system SHALL organize training artifacts under chapter-based directories with tiered difficulty levels for both practice and answer content.

#### Scenario: Chapter-tier directory structure exists
- **WHEN** training structure is initialized
- **THEN** the system MUST create `practice/<chapter>/{foundation,advanced,transfer}`
- **AND** the system MUST create `answers/<chapter>/{foundation,advanced,transfer}`

### Requirement: System SHALL enforce paired naming between practice and answer files
Each practice file SHALL have a corresponding answer file with the same question ID and topic slug.

#### Scenario: Practice-answer pairing validation
- **WHEN** a practice item is added
- **THEN** the practice filename MUST follow `p-xxx-topic.md`
- **AND** the answer filename MUST follow `p-xxx-topic.answer.md`

### Requirement: System SHALL support three-tier reinforcement levels
Training content SHALL be classified into foundation, advanced, and transfer tiers for progressive reinforcement.

#### Scenario: Tier classification is present
- **WHEN** a chapter practice item is created
- **THEN** the item MUST be placed in one of `foundation`, `advanced`, or `transfer`
- **AND** tier selection MUST be inferable from its file path

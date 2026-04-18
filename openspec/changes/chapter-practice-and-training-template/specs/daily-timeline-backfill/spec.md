## MODIFIED Requirements

### Requirement: System SHALL generate daily draft files using the approved template
The system SHALL generate `daily/dayxx.md` outputs through the unified pipeline and ensure generated content can be enriched with linked practice tasks and assessment references.

#### Scenario: Integrated day output
- **WHEN** a day file is generated or updated
- **THEN** required template sections MUST be present
- **AND** the day output MUST include links or references to generated practice and assessment artifacts

#### Scenario: Reinforcement training links are mandatory
- **WHEN** a day file includes reinforcement training content
- **THEN** it MUST include at least one practice path under `practice/<chapter>/...`
- **AND** it MUST include at least one paired answer path under `answers/<chapter>/...`

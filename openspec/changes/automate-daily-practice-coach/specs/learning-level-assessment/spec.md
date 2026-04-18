## ADDED Requirements

### Requirement: System SHALL compute multi-dimensional learning signals
The system SHALL compute learning signals across multiple dimensions (e.g., chapter coverage, implementation complexity, error-correction quality) from change and practice data.

#### Scenario: Learning signal extraction
- **WHEN** a run is finalized
- **THEN** the system MUST output dimension-level signal values
- **AND** each value MUST include traceable source references

### Requirement: System SHALL generate progression-oriented recommendations
The system SHALL generate next-step recommendations tied to low-signal dimensions and recent change context.

#### Scenario: Recommendation generation
- **WHEN** assessment is completed
- **THEN** at least one next-step recommendation MUST be produced
- **AND** recommendations MUST reference target dimensions or chapters

### Requirement: System SHALL preserve historical trend snapshots
The system SHALL persist per-run assessment snapshots to support trend analysis over time.

#### Scenario: Snapshot persistence
- **WHEN** a run finishes
- **THEN** a new assessment snapshot MUST be stored
- **AND** prior snapshots MUST remain available for comparison

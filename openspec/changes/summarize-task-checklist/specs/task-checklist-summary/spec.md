## ADDED Requirements

### Requirement: System SHALL summarize change task checklist with structured status
The system SHALL parse a target change `tasks.md` and produce a structured checklist summary including total tasks, completed tasks, pending tasks, and completion rate.

#### Scenario: Structured status summary is generated
- **WHEN** checklist summary is requested for a change
- **THEN** the system MUST output total/completed/pending counts
- **AND** the system MUST output a completion rate value

### Requirement: System SHALL group tasks by learning automation pipeline stage
The system SHALL group tasks into pipeline stages to improve execution clarity.

#### Scenario: Stage grouping is present
- **WHEN** task summary is generated
- **THEN** each task MUST be assigned to a stage group or marked as ungrouped
- **AND** grouped output MUST include stage-level counts

### Requirement: System SHALL provide next-step execution suggestions
The system SHALL recommend executable next tasks based on pending status and dependency readiness.

#### Scenario: Next-step recommendations are produced
- **WHEN** pending tasks exist
- **THEN** the system MUST list at least one recommended next task
- **AND** each recommendation MUST include a reason (e.g., dependency satisfied)

### Requirement: System SHALL validate checklist consistency
The system SHALL validate checklist integrity including task numbering continuity, status syntax validity, and dependency reference resolvability.

#### Scenario: Consistency validation reports issues
- **WHEN** checklist validation runs
- **THEN** the system MUST report detected integrity issues
- **AND** the report MUST distinguish blocking issues from warnings

X-Evil Network — Project Registry

Document status: Proposed — pending formal ratification
Document owner: X-Evil Network
Purpose: Project registration, ownership, and lifecycle tracking

1. Purpose

The project registry provides a consistent way to document projects associated with X-Evil Network.

It is intended to improve visibility into project ownership, purpose, lifecycle status, source availability, licensing, security responsibilities, and release history.

Registry inclusion does not constitute project approval, security certification, or authorization for production deployment.

2. Registry Requirements

Each registered project should have a dedicated record containing the following information where applicable.

Field| Requirement
Project name| The official project name.
Project identifier| A stable, unique identifier where the registry requires one.
Summary| A concise description of the project's purpose.
Owner| The responsible person, team, or organization.
Repository| The canonical source repository or project location.
License| The applicable license or an explicit statement that licensing is unresolved.
Lifecycle status| The current status using the defined lifecycle vocabulary.
Documentation| Links to technical, operational, and user documentation.
Security contact| A monitored reporting route or applicable security-reporting instructions.
Dependencies| Important external services, packages, and integrations.
Release information| The latest relevant release or revision, where available.
Maintenance status| Whether the project is actively maintained, deprecated, or retired.

Do not publish personal contact information, credentials, private operational details, or other sensitive information in registry records.

3. Lifecycle Statuses

The following statuses align with the proposed "Project Lifecycle Standard" (../docs/PROJECT-LIFECYCLE.md).

Status| Definition
"Proposed"| The project has been recorded but has not received development authorization.
"Under Review"| The proposal or a material change is undergoing assessment.
"Approved for Development"| The applicable authority has authorized development within a documented scope.
"In Development"| Implementation and development validation are underway.
"Release Candidate"| A candidate release is undergoing final validation.
"Active"| The project is released and actively maintained.
"Maintenance"| Work is primarily focused on fixes, security updates, and compatibility.
"Deprecated"| The project is being phased out or replaced.
"Retired"| The project is no longer actively maintained or offered as an active project.

Use status labels consistently. A status must not imply a level of approval or assurance that has not been documented.

4. Registration Process

The proposed registration process is:

1. Prepare a project proposal and initial metadata.
2. Create or update the relevant registry record.
3. Set the initial status to "Proposed".
4. Complete the required technical, security, licensing, and governance reviews.
5. Record the resulting decision and any conditions.
6. Update the lifecycle status only when the required evidence exists.
7. Keep repository and documentation links accurate over time.

Registration and approval must remain distinct decisions.

5. Public Source and Licensing

Eligible public projects are expected to provide publicly accessible source code under an approved license, subject to applicable legal, security, and privacy constraints.

Each record should identify the license clearly and link to the canonical license file where one exists.

A project should not be described as open source solely because its repository is publicly visible. Its licensing terms must permit the relevant rights under the applicable license.

Projects with unresolved licensing must identify that limitation rather than imply that unrestricted reuse is permitted.

6. Ownership and Accountability

Every registered project should have a clearly documented owner responsible for:

- Maintaining project metadata.
- Keeping source and documentation links current.
- Following applicable network standards.
- Tracking security findings and material risks.
- Maintaining dependency and integration records.
- Publishing accurate release information.
- Reviewing lifecycle status periodically.
- Coordinating deprecation or retirement when necessary.

Where ownership changes, the registry and relevant project documentation should be updated through a reviewable change.

7. Security and Compliance Metadata

Registry records should link to relevant security and operational documentation where available.

Depending on the project, this may include:

- Security reporting instructions.
- Dependency and vulnerability management information.
- Data-flow and privacy documentation.
- Integration and trust-boundary records.
- Build and deployment validation.
- Release and recovery procedures.
- Known limitations and outstanding risk records.

The presence of documentation does not establish that its controls are implemented or effective. Claims of compliance should be supported by verifiable evidence.

8. Change Management

Registry changes should be made through the repository's approved change process.

Changes to ownership, lifecycle status, license, repository location, security posture, or production availability should include an explanation and relevant supporting evidence.

Use pull requests for changes to protected branches. Required checks and reviews must pass before merging.

9. Deprecation and Retirement

A deprecated project record should identify the reason for deprecation, expected timeline where known, user impact, and available migration guidance.

A retired project record should document its final status and relevant archival, service shutdown, data handling, and credential-revocation actions where applicable.

Historical records should be preserved when needed for security, legal, operational, or audit purposes.

10. Registry Maintenance

Registry maintainers should periodically check that:

- Project entries identify an accountable owner.
- Lifecycle statuses reflect documented decisions.
- Repository and documentation links work.
- Licensing information is accurate.
- Material dependencies and integrations are recorded.
- Deprecated and retired projects are clearly identified.
- Public records do not expose sensitive information.

Corrections should be made through the approved review process.

11. Governance Status

Ratification status: Proposed — pending formal approval.

This registry standard describes a proposed process. Publishing, editing, merging, or deploying it does not constitute formal ratification. Binding requirements must follow the applicable governance approval process.

---

X-Evil Network — Clear project ownership, traceable status, and accountable maintenance.

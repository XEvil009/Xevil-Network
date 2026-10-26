X-Evil Network — Project Lifecycle Standard

Document type: Project lifecycle and governance procedure
Status: Proposed — pending formal approval where required
Version: 1.0.0
Applies to: Projects participating in X-Evil Network

1. Purpose

This document defines a consistent lifecycle for proposing, registering, developing, reviewing, releasing, maintaining, and retiring network projects.

Its purpose is to establish traceable project status, clear ownership, risk-appropriate security controls, and predictable release practices.

This document remains proposed until approved through the applicable governance process. It does not independently authorize a project or grant repository access.

2. Lifecycle Stages

Projects should progress through the following stages.

Stage| Description| Expected evidence
1. Proposed| Project concept and intended scope are documented.| Proposal and initial risk assessment
2. Under Review| Governance, feasibility, security, and licensing considerations are evaluated.| Review comments and recorded decision
3. Approved for Development| Required approvals are recorded and development may begin.| Approval record and assigned owner
4. In Development| Implementation, testing, documentation, and security controls are established.| Source code, tests, documentation, and issue tracking
5. Release Candidate| A specific version is prepared for final validation.| Version identifier, validation results, and release notes
6. Active| An approved release is available and maintained.| Release record, support expectations, and maintenance owner
7. Maintenance| The project receives fixes, dependency updates, and security remediation.| Maintenance policy and tracked changes
8. Deprecated| The project is scheduled for replacement or retirement.| Deprecation notice, migration guidance, and timeline where applicable
9. Retired| Active development or support has ended.| Retirement record and final status

A project may be rejected, suspended, or placed on hold at any stage when justified by security, governance, feasibility, or compliance concerns.

3. Project Proposal Requirements

A project proposal should include:

- Project name and unique identifier.
- Purpose, intended users, and scope.
- Proposed owner and maintainers.
- Source repository and implementation approach.
- Dependencies and planned integrations.
- Data handling, permissions, and security considerations.
- Licensing approach and third-party rights considerations.
- Testing, deployment, and maintenance plan.
- Known limitations, risks, and external requirements.

Proposals should not include credentials, private keys, personal information without a valid need, or confidential third-party material.

4. Review and Approval

Reviewers should assess the proposal against the applicable governance policies and standards.

The review should consider:

1. Alignment with the network's purpose and approved policies.
2. Clear ownership and maintenance responsibility.
3. Security risks, trust boundaries, and required permissions.
4. Licensing and public-source requirements, where applicable.
5. Dependency health and integration risks.
6. Testing, documentation, and release readiness.
7. Operational cost and long-term sustainability.

Approval decisions should be recorded with the decision date, decision status, responsible authority, relevant conditions, and links to supporting review records.

Approval for development does not automatically authorize a production release.

5. Development Requirements

During development, project maintainers should:

- Use version control and purpose-specific branches.
- Submit changes through pull requests.
- Run applicable automated checks before merging.
- Maintain tests and reproducible build instructions where practical.
- Document configuration, dependencies, interfaces, and operational requirements.
- Apply least privilege to credentials, workflows, and external services.
- Address reported vulnerabilities according to their severity and exposure.
- Keep project metadata and the network registry accurate.

Secrets must be stored through appropriate secure mechanisms, not in source files, commit history, public issues, or documentation.

6. Release Readiness

Before a production release, the project owner should confirm that:

- The release scope and version identifier are clear.
- Required tests and validation checks pass.
- Known release-blocking defects are resolved or formally accepted by the appropriate authority.
- Security and dependency reviews are complete at the required level.
- Documentation and installation or deployment instructions are current.
- Licensing and distribution requirements have been addressed.
- Release notes identify significant changes and known limitations.
- Rollback, recovery, or remediation procedures are documented where appropriate.
- The release approval is recorded.

The project owner retains final release authority within approved network policies and their granted permissions.

7. Release Records

Each production release should have a traceable record containing, where applicable:

- Project identifier and release version.
- Release date.
- Source commit or immutable source reference.
- Summary of changes.
- Compatibility or migration notes.
- Validation results.
- Known issues and security advisories.
- Approval reference.
- Rollback or recovery guidance.

A release record must not claim that a security audit, certification, or test was completed unless supporting evidence exists.

8. Maintenance and Security Response

Active projects should define how they receive bug reports, monitor dependencies, publish fixes, and communicate significant incidents.

Security issues should be handled through an appropriate private reporting channel when public disclosure could expose users or systems to additional risk.

Maintainers should assess impact, prioritize remediation according to risk, validate fixes, and document the outcome without unnecessarily exposing exploit details or sensitive data.

9. Deprecation and Retirement

A project may be deprecated or retired when it is no longer maintained, has been superseded, is no longer viable, or presents risks that cannot reasonably be addressed.

The responsible owner should document:

- The reason and effective date.
- Whether security fixes and support will continue during a transition period.
- Replacement projects or migration options, if available.
- Data export or migration considerations.
- Dependency and integration impacts.
- The final repository and release status.

Where a vulnerability or urgent operational risk requires immediate action, protective measures may be taken before a normal deprecation timeline is completed.

10. Registry and Manifest Maintenance

Project lifecycle changes should be reflected in the network's project registry and other relevant records.

Do not mark a project as approved, active, or released without supporting evidence. Proposed projects must remain distinguishable from approved or production projects.

Update "STRUCTURE-MANIFEST.json" whenever the repository structure changes, following the manifest's own maintenance rules.

11. Exceptions

Any exception to an approved mandatory requirement must be documented, risk-assessed, time-bounded where practical, and approved by the authority designated by the applicable policy.

An exception must identify its scope, rationale, compensating controls, responsible owner, and review or expiry date.

12. Review and Status

This document is proposed and does not become ratified solely because it is merged into the repository.

Once formally approved, its status and approval reference should be updated. Revisions should be reviewed when network governance, security requirements, or project delivery practices materially change.

---

X-Evil Network — consistent project governance from proposal to retirement.

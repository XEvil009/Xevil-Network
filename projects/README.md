X-Evil Network — Project Registry

Document Type: Project Registry Standard
Version: 1.0.0
Status: Proposed — Pending Formal Ratification
Maintained By: X-Evil Network maintainers
Network Authority: XEVIL009

1. Purpose

The Project Registry provides a consistent record of projects belonging to or formally associated with X-Evil Network.

It supports project discovery, ownership transparency, lifecycle tracking, security accountability, dependency management, and release coordination.

A registry entry is a record, not proof of approval, operational readiness, or security certification.

2. Registry Requirements

Every registered project should have a unique project identifier and, where applicable, the following information:

- Project ID: Stable, unique identifier.
- Project Name: Official project name.
- Description: Purpose, scope, and intended users.
- Owner: Accountable project owner or team.
- Maintainers: Authorized individuals or teams responsible for maintenance.
- Source Repository: Canonical source-code repository URL.
- License: Applicable open-source license or clearly stated licensing status.
- Lifecycle Status: Current status as defined in this document.
- Documentation: Primary documentation location.
- Security Reporting: Available vulnerability-reporting channel.
- Dependencies: Material internal and external dependencies.
- Integrations: Known connections to other projects or services.
- Data Classification: Categories of data processed, if applicable.
- Release Information: Latest verified release or an explicit statement that no release exists.
- Support Policy: Maintenance expectations and support limitations.
- Decision Record: Link to the relevant approval or status-change record, when applicable.

Unknown or inapplicable fields must be identified honestly. Do not invent values or publish secrets, credentials, private contact details, or sensitive infrastructure information.

3. Lifecycle Statuses

Use the following status vocabulary consistently:

Status| Meaning
"proposed"| Submitted for consideration; not approved.
"under-review"| Under evaluation for suitability, risk, and requirements.
"approved-for-development"| Authorized to enter development under the applicable approval process.
"in-development"| Implementation is underway.
"release-candidate"| A candidate release is undergoing final validation.
"active"| Released and maintained for its stated purpose.
"maintenance"| Primarily receiving maintenance, fixes, or security updates.
"deprecated"| Marked for eventual replacement or discontinuation.
"retired"| No longer maintained or supported by the network.

A status change must be supported by a verifiable record. Do not label a project "active", "approved-for-development", or "release-candidate" without evidence appropriate to that status.

4. Project Admission

A project proposed for network registration should include:

1. A clear purpose and defined scope.
2. An accountable owner and maintenance plan.
3. A canonical source repository, where applicable.
4. Appropriate licensing information for public source code.
5. Documentation and a proposed lifecycle status.
6. A preliminary security and privacy assessment proportionate to its risks.
7. Identified dependencies and external integrations.
8. A review or decision record appropriate to its current stage.

Registration and approval are separate actions. Projects must not claim network endorsement solely because their repository appears in this registry.

5. Ownership and Accountability

Each project must have a clearly identified accountable owner. Maintainer access should follow least-privilege principles and be reviewed when responsibilities change.

Project owners remain responsible for project-level maintenance and releases within the applicable network policies.

Network-level governance, security, and cross-project conflicts remain subject to the authority and procedures established by the formally approved network governance documents.

6. Public Source and Licensing

Projects designated for public release should provide publicly accessible source code under an approved license, subject to applicable legal and governance requirements.

The registry must distinguish between:

- A public source repository with a declared license.
- A public repository whose licensing status is unresolved.
- A private or restricted repository, if permitted by applicable policy.

Public visibility alone does not establish that code is open source or legally reusable.

7. Security and Privacy

Registry entries must not expose credentials, access tokens, private keys, confidential operational details, or personal information that is not necessary for the registry.

Projects must document relevant security-reporting routes, material dependencies, and significant data-processing responsibilities.

Security incidents, vulnerabilities, and remediation records should be handled through authorized channels. Public registry updates must not disclose exploitable details prematurely.

8. Maintenance and Status Changes

Project owners or authorized maintainers should keep registry entries accurate when:

- Ownership or maintainership changes.
- Source repositories move or become unavailable.
- Licensing changes.
- Dependencies or integrations materially change.
- A release is published.
- Support status changes.
- A project is deprecated or retired.
- Significant security or compliance information changes.

Changes to project status should include a date and a reference to the supporting decision or release record, where applicable.

9. Registry Integrity

Registry information must be traceable to a source repository, project documentation, release record, or authorized decision.

Do not publish fabricated projects, unsupported approval claims, unverified release versions, or misleading security certifications.

Where a fact cannot be verified, mark it as unknown or pending verification.

10. Governance Status

This document is proposed and pending formal ratification. Its publication or inclusion in the repository does not itself constitute ratification.

Until the applicable governance process is completed, this document serves as a proposed registry standard and must not be represented as a formally adopted policy.

11. Related Documentation

- "Network Documentation Index" (../docs/README.md)
- "Network Overview" (../docs/NETWORK-OVERVIEW.md)
- "Project Lifecycle" (../docs/PROJECT-LIFECYCLE.md)
- "Security Standard" (../standards/SECURITY-STANDARD.md)
- "Integration Documentation" (../integrations/README.md)
- "Release Documentation" (../releases/README.md)

---

X-Evil Network — Project Registry
Documented, traceable, maintainable, and security-conscious project governance.

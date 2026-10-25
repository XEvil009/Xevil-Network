X-Evil Network Contribution Policy

- Document ID: XEN-POL-CONTRIB-001
- Version: 1.0
- Status: PROPOSED — NOT RATIFIED
- Policy owner: X-Evil Network Governance
- Effective date: Pending formal ratification
- Review cycle: At least annually and when contribution procedures materially change

1. Purpose

This policy defines the proposed baseline for accepting, reviewing, documenting, and maintaining contributions to projects within X-Evil Network.

Its goals are to support responsible collaboration, protect source-code integrity, clarify contributor expectations, and maintain transparent project governance.

This document remains a proposal until its formal ratification is recorded.

2. Scope

This policy applies to contributions submitted to network-managed projects, including:

- Source code and application changes.
- Documentation and governance records.
- Website content, designs, and static assets.
- Tests, build configuration, and automation workflows.
- Bug reports, feature proposals, and security improvements.
- Translations and other project-maintenance work.

A project may publish additional contribution requirements, provided they do not conflict with applicable law or ratified network-level policies.

3. Contribution principles

Contributions should follow these principles:

1. Respectful, professional, and constructive collaboration.
2. Transparent decision-making and documented review.
3. Least privilege for repository and deployment access.
4. Secure development and responsible vulnerability handling.
5. Clear licensing and attribution.
6. Maintainable, documented, and testable changes.
7. Equal application of published contribution requirements.
8. No unauthorized disclosure of confidential or personal information.

4. Eligibility and authorization

Contributors must have the rights and authorization necessary to submit their work.

Contributors must not submit material that they know is stolen, unlawfully obtained, improperly disclosed, or incompatible with the project's licensing requirements.

Submitting a contribution does not automatically grant the contributor repository administration, merge, release, or deployment privileges.

Privileged access must be granted separately and according to documented project responsibilities.

5. Contribution workflow

The recommended workflow is:

1. Review the project's README, license, contribution instructions, and applicable policies.
2. Open or review an issue or proposal for substantial changes when appropriate.
3. Create a dedicated branch for the contribution.
4. Make a focused, reviewable change.
5. Add or update relevant documentation and tests.
6. Check formatting, links, build output, security implications, and required automated checks.
7. Submit a pull request with a clear description, rationale, and testing evidence.
8. Respond to review feedback and resolve identified issues.
9. Obtain the required approval and merge through the project's approved process.

Contributors should not push directly to a protected default branch or bypass required review controls.

Emergency changes may follow an expedited process when justified, authorized, validated, and documented.

6. Pull-request requirements

A pull request should include, where relevant:

- A concise summary of the change.
- The problem being addressed and the intended outcome.
- Related issue or decision references.
- Tests or validation performed.
- Security, privacy, compatibility, and operational considerations.
- Documentation or migration changes.
- Known limitations and outstanding risks.

Changes should remain focused where practical. Unrelated refactoring, undocumented behavior changes, and unnecessary file modifications should be avoided.

Large changes should be divided into reviewable units where doing so does not compromise correctness.

7. Review and approval

Reviewers should evaluate changes for:

- Correctness and maintainability.
- Consistency with project architecture and governance.
- Security and privacy risks.
- Licensing and attribution concerns.
- Test coverage and validation evidence.
- Documentation quality.
- Compatibility and deployment impact.
- Compliance with applicable policies.

Approval must come from an authorized reviewer. Automated checks do not replace human review where human approval is required.

The project owner retains final release authority within approved policies. Network-level governance and security decisions remain subject to the authority defined by the applicable network charter and ratified policies.

Where a reviewer has a material conflict of interest, the conflict should be disclosed and handled through the project's documented process.

8. Licensing and intellectual property

Each project must clearly identify its applicable license and relevant third-party notices.

For projects designated as eligible for public participation under the network governance framework:

- Source code must be publicly accessible.
- An approved license must be published.
- Contributors must have the right to submit the material.
- Third-party code, assets, and dependencies must comply with their applicable licenses.
- Required copyright notices and attribution must be preserved.

Contributors should not assume that publicly accessible code is automatically open source or free of licensing restrictions.

A contribution must not silently change a project's license. License changes require explicit review, appropriate authorization, and updated documentation.

Any contributor agreement or additional licensing requirement must be clearly published and reviewed before it is imposed.

9. Security and sensitive information

Contributors must not include live credentials, private keys, passwords, personal data, or confidential operational information in commits, issues, pull requests, logs, or release artifacts.

Security-sensitive vulnerabilities should be reported through the project's designated private reporting route rather than disclosed publicly before coordinated handling is possible.

Contributors should disclose material security implications and avoid introducing unnecessary permissions, untrusted dependencies, unsafe defaults, or unreviewed deployment changes.

If a secret is accidentally committed, the contributor must promptly notify the maintainers so the credential can be revoked or rotated and the exposure assessed. Removing the secret from a later commit alone is insufficient.

10. Automated checks and quality standards

Projects should define appropriate automated checks, such as:

- Build and deployment validation.
- Unit, integration, or other relevant tests.
- Formatting and linting.
- Link and asset validation for websites.
- Dependency and secret scanning where available.
- License or policy checks where appropriate.

The required checks should be documented and enforced through repository controls where supported.

Contributors must not knowingly falsify test results or claim that checks passed when they were not run or did not pass.

11. Documentation and governance changes

Changes affecting architecture, security, public behavior, licensing, releases, or governance must update relevant documentation.

Governance documents must clearly identify their version and status. A proposed policy must not be described as ratified or active without the required decision record.

Merging a governance document does not, by itself, constitute formal ratification.

Material governance changes should include the appropriate review and decision references.

12. Community conduct

All participants should communicate professionally and respectfully.

The project may address harassment, threats, discriminatory conduct, deliberate disruption, spam, impersonation, or repeated abuse through proportionate, documented moderation measures.

Reports should be handled discreetly, with access limited to those who need the information. Decisions should be based on evidence and applicable project rules.

Where a separate code of conduct exists, contributors should follow it alongside this policy.

13. Maintainer responsibilities

Maintainers should:

- Publish clear contribution and review requirements.
- Apply requirements consistently.
- Protect privileged repository and deployment access.
- Provide actionable review feedback where practicable.
- Avoid merging changes that fail mandatory security or quality checks.
- Record material decisions and exceptions.
- Keep project licensing and governance documentation current.
- Escalate unresolved security or cross-project governance conflicts through the documented authority structure.

Maintainers should not promise acceptance, release dates, or project support unless authorized to do so.

14. Rejection, revision, and appeals

A contribution may be declined when it is out of scope, unsafe, incompatible with project requirements, inadequately documented, legally problematic, or inconsistent with the project's direction.

Where practical, maintainers should explain the main reason for rejection and identify any changes that could make the contribution acceptable.

A contributor may request reconsideration through the project's documented process. Material disputes should be referred to an appropriate reviewer or governance authority, with conflicts of interest considered.

Acceptance of a contribution does not guarantee that it will be released, deployed, or maintained indefinitely.

15. Exceptions

Exceptions to project contribution procedures must be documented and approved by an authorized project or governance authority.

The record should identify the requirement, justification, affected scope, risks, compensating controls, approving authority, and review or expiry date.

No exception may authorize unlawful conduct or override a binding higher-level requirement.

16. Ratification and change control

- Current status: PROPOSED — NOT RATIFIED.
- Approving authority: Not recorded.
- Ratification date: Pending.
- Effective date: Pending.
- Decision record: Pending.

Formal adoption requires an explicit, auditable ratification decision and an update to the policy register.

Changes should be submitted through reviewed pull requests. Material revisions should update the document version, change history, and policy register as appropriate.

17. Change history

Version| Date| Change
1.0| 2026-10-25| Initial proposed contribution policy

---

Document status notice: This document is a proposal for review. Until formal ratification is recorded, it must not be represented as an active, binding X-Evil Network contribution policy.

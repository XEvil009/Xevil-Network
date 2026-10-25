X-Evil Network Release Policy

- Document ID: XEN-POL-REL-001
- Version: 1.0
- Status: PROPOSED — NOT RATIFIED
- Policy owner: X-Evil Network Governance
- Effective date: Pending formal ratification
- Review cycle: At least annually and after material release or deployment incidents

1. Purpose

This policy defines the proposed minimum requirements for preparing, validating, approving, publishing, and maintaining software, websites, documentation, and other production deliverables across X-Evil Network.

The objectives are to protect production integrity, make releases traceable, reduce deployment risk, and establish clear accountability for release decisions.

This document remains a proposal until formal ratification is recorded.

2. Scope

This policy applies to:

- Public websites and static-site deployments.
- Applications, libraries, packages, and software releases.
- Source-code changes that affect production behavior.
- Build and deployment workflows.
- Release artifacts, version tags, and release notes.
- Rollbacks, hotfixes, and emergency production changes.

Projects may define stricter release requirements based on their architecture, operational risk, and user impact.

3. Release principles

Releases should follow these principles:

1. Authorization: Production changes require an authorized release decision.
2. Validation: Required checks must pass before release.
3. Traceability: Every material release should be linked to its source changes and approval record.
4. Reproducibility: Build and deployment procedures should be documented and repeatable where practical.
5. Least privilege: Deployment credentials must have only the required permissions.
6. Separation of duties: Independent review should be used for material or high-risk changes where practical.
7. Recoverability: Projects should define an appropriate recovery or rollback strategy.
8. Transparency: Release notes must accurately describe material changes and known limitations.

4. Release authority

The project owner retains final release authority within approved policies and applicable law.

Network-level governance, security requirements, and cross-project conflicts remain subject to the authority defined by the network charter and applicable ratified policies.

Release approval must be attributable to an authorized person or documented automation process. A successful CI run alone does not establish authorization to release.

Merging a pull request, creating a tag, or publishing an artifact must not be represented as formal policy ratification.

5. Release classifications

Projects should use release classifications appropriate to their delivery model.

- Major release: Introduces significant functionality, architecture changes, or potentially incompatible behavior.
- Minor release: Adds compatible functionality or meaningful improvements.
- Patch release: Fixes defects or security issues without intended incompatible changes.
- Hotfix: An expedited change addressing an urgent production issue.
- Pre-release: A release explicitly marked as experimental, preview, beta, or otherwise not generally production-ready.

Projects using semantic versioning should follow the relevant versioning rules. Projects that do not publish versioned software should still maintain an auditable deployment or release identifier.

6. Source control and change management

Production changes should follow a controlled workflow:

1. Create a dedicated branch for the change.
2. Submit a pull request against the designated target branch.
3. Provide a clear description, relevant issue or decision references, and validation evidence.
4. Obtain required review and approval.
5. Pass the repository's required status checks.
6. Merge using the approved repository process.
7. Build and deploy the approved source revision through the documented pipeline.

Direct changes to the production branch should be restricted where the platform supports it.

Emergency changes may use an expedited workflow when justified and authorized. The project must preserve validation evidence and complete retrospective review and documentation.

7. Pre-release validation

Before a production release, the responsible project team should verify applicable requirements, including:

- Required CI and build checks have passed.
- Relevant automated and manual tests have been completed.
- The intended source revision and target environment are correct.
- Dependencies and build inputs are understood.
- Security-sensitive changes have received appropriate review.
- No known unresolved critical issue makes the release unsafe.
- Required documentation, configuration, and migration instructions are ready.
- Secrets are not embedded in public artifacts or client-side assets.
- Deployment permissions and credentials are appropriately restricted.
- Rollback, recovery, or mitigation steps are available where needed.

For static websites, validation should include the generated output, internal links, required assets, and deployment configuration as applicable.

Checks that do not apply to a project should be recorded as not applicable rather than reported as completed.

8. Release approval

A release record should identify, where applicable:

- Project and release identifier.
- Source branch, commit SHA, or immutable source reference.
- Pull request or change record.
- Required validation results.
- Release approver or authorized automation identity.
- Target environment.
- Planned or actual release time.
- Known risks, limitations, and exceptions.
- Rollback or mitigation plan.

High-risk releases should receive additional review or explicit approval appropriate to the potential impact.

Approval must not be inferred from silence, an unreviewed automated result, or the mere existence of a merged pull request.

9. Build and artifact integrity

Projects should:

- Build from a known and approved source revision.
- Restrict permissions available to build and deployment workflows.
- Avoid exposing secrets to untrusted code.
- Pin critical build dependencies and CI actions where practical.
- Keep production artifacts distinguishable from development or preview artifacts.
- Preserve relevant build and deployment logs without retaining unnecessary sensitive information.
- Verify the deployed revision when the hosting platform provides sufficient evidence.

Where feasible, projects should record artifact checksums, build provenance, or other integrity evidence for important software releases.

10. Deployment requirements

Deployments should use documented, authorized procedures.

The deployment process should:

1. Target the intended environment and approved revision.
2. Use credentials with narrowly scoped permissions.
3. Prevent untrusted changes from gaining production deployment privileges.
4. Report success or failure accurately.
5. Preserve enough information to investigate failures.
6. Avoid publishing incomplete or unvalidated artifacts.
7. Verify the live result after deployment.

Production credentials should be stored in approved secret-management facilities, not committed to the repository or embedded in public website files.

Changes to deployment configuration must receive review proportionate to their operational and security impact.

11. Post-release verification

After a production release, the responsible maintainer should verify applicable items such as:

- The deployment completed successfully.
- The expected version or source revision is live.
- Essential pages, endpoints, or application functions work.
- Required assets and navigation are available.
- No obvious regression or critical security issue has been introduced.
- Monitoring or error reporting shows no material unexpected failure, where such facilities exist.

The release record should include the verification outcome and any follow-up actions.

A green deployment workflow must not be treated as proof that every production behavior is correct.

12. Release notes and public communication

Public releases should include clear notes proportionate to their impact.

Release notes should describe:

- New functionality and material changes.
- Bug fixes and security improvements where disclosure is appropriate.
- Breaking changes or required user actions.
- Known limitations and compatibility considerations.
- Migration, upgrade, or rollback instructions where needed.

Do not publish secrets, private user information, confidential incident details, or exploit instructions that would create unnecessary risk.

Security fixes should be communicated in a coordinated manner appropriate to their severity and disclosure requirements.

13. Rollback and recovery

Each production project should define a recovery approach suitable for its architecture.

Depending on the deployment model, this may include:

- Reverting to a previously approved revision.
- Redeploying a known-good artifact.
- Disabling a faulty feature.
- Reverting a configuration change.
- Restoring a backup or repairing migrated data.
- Rotating credentials or isolating affected services.

Rollback plans must account for changes that are not safely reversible, including data migrations and externally visible operations.

After a rollback, the responsible maintainer should verify service recovery, document the event, and identify corrective actions.

For static-site hosting, recovery may consist of redeploying a previously validated revision when that option is supported.

14. Emergency releases

Emergency releases may be necessary to address active exploitation, critical defects, data exposure, or major service disruption.

The process should:

1. Record the emergency and its justification.
2. Identify an authorized decision-maker.
3. Apply the narrowest safe change that addresses the issue.
4. Perform essential validation before deployment whenever feasible.
5. Preserve source, approval, and deployment evidence.
6. Verify the result after deployment.
7. Complete retrospective review and documentation as soon as practicable.

Emergency procedures must not become a routine method of bypassing review or security controls.

15. Failed releases and corrective actions

When a release fails or causes a material regression, the responsible maintainer should:

- Assess impact and determine whether rollback or mitigation is required.
- Notify relevant project stakeholders.
- Preserve diagnostic evidence.
- Restore a safe operating state where possible.
- Identify root causes and contributing factors.
- Assign corrective actions and target dates.
- Update tests, documentation, or controls to reduce recurrence.

Material incidents should be handled under the applicable security and incident-response procedures.

16. Release records and retention

Release records should be stored in an appropriate, access-controlled, durable location.

Records should be sufficient to reconstruct the source revision, approval, validation, deployment outcome, and relevant corrective actions.

Retention periods should reflect operational needs, legal obligations, contractual requirements, and privacy considerations. Sensitive records should not be retained indefinitely without justification.

17. Exceptions and risk acceptance

Any exception to a material release control must be documented and approved by an authorized authority.

The record should identify:

- The affected project and release.
- The control being waived.
- The justification and assessed risk.
- Compensating controls.
- The approving authority.
- The expiry or review date.
- Required follow-up actions.

An exception cannot authorize unlawful conduct or override a binding higher-level requirement.

18. Ratification and change control

- Current status: PROPOSED — NOT RATIFIED.
- Approving authority: Not recorded.
- Ratification date: Pending.
- Effective date: Pending.
- Decision record: Pending.

Formal adoption requires an explicit, auditable ratification decision and an update to the policy register.

Material changes should be made through reviewed pull requests, with the document version, change history, and policy register updated as appropriate.

19. Change history

Version| Date| Change
1.0| 2026-10-25| Initial proposed release policy

---

Document status notice: This document defines proposed release controls for review. Until formal ratification is recorded, it must not be represented as an active, binding X-Evil Network release policy.

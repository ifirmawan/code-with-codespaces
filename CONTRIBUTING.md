# Contributing

Thank you for helping improve this initial FastAPI app for exploring GitHub Codespaces.

This repository is meant to be a simple collaborative workspace for learning how to build and document an API in a codespace environment. The guidance below helps collaborators work together responsibly and consistently.

## Communication and collaboration

Before making changes, open or update an issue describing the task, bug, or enhancement. Keep discussions visible in the repository so everyone can follow the decision-making process.

Use pull requests for all meaningful changes. A pull request should explain:

- what problem is being solved
- what files or areas of the app were changed
- how the change was verified

When you need help, ask in a clear and friendly way. Keep updates short and specific so collaborators can respond quickly.

## Responsibility and ownership

To make collaboration easier, work should be assigned by area of responsibility:

- `main.py`: API route definitions and calculator logic
- `test_main.py`: regression tests for route behavior and validation
- `README.md`: repository usage and project context documentation
- `requirements.txt`: dependency declarations for the FastAPI app

Collaborators are encouraged to take ownership of the files or features they update and to communicate clearly when a topic crosses team boundaries.

## Personal repository versus organization repository

Collaboration differs when a repository is created in a personal account versus an organization account.

In a personal repository:

- the owner usually controls permissions and review flow
- collaborators may be added directly by the owner
- the project may move more quickly with fewer formal rules

In an organization repository:

- repository access is usually managed through teams and organization roles
- review, moderation, and security policies may be enforced centrally
- changes often require broader coordination and stronger approval processes

When contributing, follow the repository’s visible permission model and ask for clarification if you are unsure who may review or approve a change.

## Ground rules for a healthy collaboration environment

We want a respectful, inclusive, and productive collaboration environment. Please:

- be kind and constructive in code review and issue discussions
- avoid personal attacks, sarcasm, and dismissive comments
- focus feedback on code and behavior, not on individuals
- keep comments specific, actionable, and grounded in project goals
- respect the time and workload of collaborators
- avoid pushing changes that are unrelated to the requested task

The goal is to make the project a safe place to learn, experiment, and improve the FastAPI app.

## Security updates and reporting

Security issues should be handled privately and responsibly.

If you discover a vulnerability or security concern:

1. Do not publicly disclose the details in an issue or pull request.
2. Contact the repository owner or organization maintainers privately.
3. Provide a concise description of the risk, affected files, and suggested mitigation if known.
4. Wait for a maintainer-led process before sharing the fix or public details.

For sensitive changes, maintainers should coordinate a security update process that may include:

- validating the affected dependency or code path
- updating version pins where necessary
- adding or improving tests that protect the vulnerable behavior
- documenting the security fix in the release note or pull request summary

## Pull request workflow

1. Create a branch from the latest default branch.
2. Make a focused change with a clear description.
3. Add or update tests where appropriate.
4. Open a pull request that explains the motivation, scope, and verification evidence.
5. Respond to feedback and make sure all relevant checks pass before merging.

## Questions

If you are unsure about process, ownership, or review expectations, ask before making the change. Clear collaboration starts with shared expectations.

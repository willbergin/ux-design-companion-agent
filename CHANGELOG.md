# Changelog

## 1.1.1: Documentation wording (2026-11-17)

- Rewrote the README, user guide, installation guide and worked examples in a simpler, more direct style.
- Removed em dashes from the active documentation and kept the installation and example links intact.
- No change to the agent instructions or generated integrations.

## 1.1.0: User documentation (2026-11-17)

- Added a detailed, practical [User Guide](docs/USER-GUIDE.md) with Create/Review workflows, framework explanations, score interpretation, prototype usage, product context, prompts and troubleshooting.
- Added [installation and activation](docs/INSTALLATION.md) instructions for Codex, Cursor, Claude Code, Gemini CLI, Kiro, GitHub Copilot and generic AI environments.
- Added two illustrated walkthroughs: guided registration Create example and evidence-labelled operations dashboard Review example.
- Included two real standalone illustrative HTML examples and PNG screenshots captured from those files. These are documentation samples, not autonomous agent-run results or accessibility certifications.
- Updated README navigation; unchanged canonical agent behaviour and generated adapters.

## 1.0.0: Portable agent edition (2026-11-17)

Migrated the original Kiro UX Design Companion into a vendor-neutral instruction source, with generated Codex/Cursor, Claude Code, Gemini CLI, Kiro (skill and agent), and GitHub Copilot adapters.

### Behavior changes

1. **Portability:** One `src/agent.md` generates platform-specific entry points using the Agent Skills standard where available. Generic Markdown instructions work where automatic skill discovery is absent.
2. **Accessibility:** Explicitly *target* WCAG 2.2 AA; provide a test checklist and distinguish verified tests from manual or untested criteria. No blanket guarantee of compliance.
3. **Review evidence:** Tag issues Observed, Inferred or Needs testing, and clarify screenshot/link limitations.
4. **Scoring:** Five 0–2 criteria for each framework, 1–10 scaled output, coverage threshold, provisional scores and `Not scored` for insufficient evidence.
5. **Create flexibility:** Propose two approaches by default but allow building one or both (or a direct single approach) without redundant confirmations.
6. **Documentation:** Corrected framework-selection wording; added examples, file outputs, portability limits and manual acceptance scenarios.
7. **Workflow:** Skip mode choice and intermediate confirmation when the user's request already makes the scope clear.

### Preserved from original

- Create and Review modes; Nielsen's heuristics; WCAG 2.2 AA; visual, Dan Brown IA and user-flow reviews.
- Self-contained HTML prototypes with rationale; iteration and preserving alternatives.
- Respect for product documentation and existing design systems.
- Unmodified source files retained under `legacy/`.

### Known limitations

- Adapters are structurally validated but not yet end-to-end tested across every vendor environment.
- Availability of web, file-writing, browser, screenshots, accessibility automation and screen readers is determined by the host agent.
- Generated prototypes are not independently certified as meeting WCAG 2.2 AA.

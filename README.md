# UX Design Companion

I built UX Design Companion to help with UX work when a dedicated designer isn't available. It can help you explore a new feature, put together a clickable prototype or review an existing interface for problems worth fixing.

It started as a Kiro agent. I've since moved the main instructions into a shared file so I can use the same approach in Codex and other AI tools without maintaining several copies by hand.

This is a tool for working through design decisions. It doesn't replace user research, a UX designer or proper accessibility testing.

## What you can do with it

**Create:** Describe a feature or a problem you want to solve. The companion can suggest two different approaches, explain the trade-offs and build one or both as HTML prototypes. If you already know what you want, you can skip the comparison and ask it to build a single option.

**Review:** Share a screenshot, prototype, source code or a page the assistant can access. Choose the areas you want reviewed:

| Code | Review | Covers |
| --- | --- | --- |
| A | Usability | Nielsen's 10 heuristics |
| B | Accessibility | Potential WCAG 2.2 AA issues |
| C | Visual design | Layout, hierarchy, type, colour and spacing |
| D | Information architecture | Navigation, labels and content organisation |
| E | User flow | Steps, friction and error recovery |

Reviews distinguish what the companion **observed**, what it **inferred** and what **needs testing**. It scores a review only when there's enough evidence. You can also ask it to prototype a suggested fix.

## Give it a try

For a new feature:

> Use UX Design Companion in Create mode. I'm working on sign-up for a mobile events app. Give me two different approaches and explain the trade-offs. Don't build the prototypes yet.

For a review:

> Use UX Design Companion to review this dashboard screenshot for usability (A) and visual design (C). Show me the main issues, tell me which ones need testing and suggest what to fix first.

You can use it without knowing the framework names. Just describe what you're trying to do.

## Installation

The repository includes versions for several AI tools. If you're opening this project in one of them, the relevant file is already here. To use it in a different project, copy the appropriate skill or agent folder.

| Tool | Location in this repository |
| --- | --- |
| Codex and Cursor | `.agents/skills/ux-companion/SKILL.md` |
| Claude Code | `.claude/skills/ux-companion/SKILL.md` |
| Gemini CLI | `.gemini/skills/ux-companion/SKILL.md` |
| Kiro Skill | `.kiro/skills/ux-companion/SKILL.md` |
| Kiro custom agent | `.kiro/agents/ux-companion.md` |
| GitHub Copilot agent | `.github/agents/ux-companion.agent.md` |
| Other assistants | Copy instructions from `src/agent.md` |

Different tools support different features. A chat-only assistant can give advice, but it won't be able to create files or check interactions in a browser unless those capabilities are available.

See the [installation guide](docs/INSTALLATION.md) for setup paths and troubleshooting.

## Guides and examples

- [User guide](docs/USER-GUIDE.md): How Create and Review work, what to provide and how to read the results.
- [Create example](docs/examples/create-workflow.md): Working through two approaches to an events app sign-up flow.
- [Review example](docs/examples/review-workflow.md): Reviewing a fictional operations dashboard.

Both examples include screenshots and HTML files you can open locally. They're illustrations made for the documentation, not outputs from a live agent test.

## Files and structure

When file access is available, the companion normally writes its work to `ux-companion/` in your project:

```text
ux-companion/
  prototypes/     HTML prototypes, including earlier versions
  decisions/      Notes on design choices and trade-offs
  reviews/        Findings, evidence and recommended changes
```

The agent itself is organised like this:

```text
src/agent.md       Main instructions; edit this file
scripts/build.py   Regenerates the tool-specific versions
scripts/verify.py  Checks the package
scripts/score.py   Review scoring helper
docs/               User guide, installation help and examples
tests/              Static checks and manual test scenarios
legacy/             Original Kiro files for reference
```

### Changing the agent

Edit `src/agent.md`, then run the following from the project root:

```bash
python scripts/build.py
python scripts/build.py --check
python scripts/verify.py
python -m unittest discover -s tests -v
```

Python 3.9+ is needed to regenerate the files, but not to use the skill. These commands check that the package is consistent. They don't test whether the assistant produces good designs. For that, use the [test scenarios](tests/scenarios.md) and test any prototypes in a browser.

## Before publishing

The package hasn't been tested end to end in every supported tool. Accessibility checks also need to be carried out on each generated prototype. Don't treat a review score as evidence from real users.

There's no licence in the repository yet. I'll add one before publishing it publicly on GitHub.

## References

[Agent Skills specification](https://agentskills.io/specification) | [Codex](https://developers.openai.com/codex/skills) | [Claude Code](https://code.claude.com/docs/en/skills) | [Cursor](https://cursor.com/docs/skills) | [Gemini CLI](https://geminicli.com/docs/cli/skills/) | [Kiro](https://kiro.dev/docs/skills/) | [GitHub Copilot](https://docs.github.com/en/copilot/reference/custom-agents-configuration)

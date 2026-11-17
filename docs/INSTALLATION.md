# Installation

UX Design Companion isn't an app you need to host. It's a set of instructions that your AI tool reads when you ask for UX help.

The repository has the same core instructions packaged for several tools. Use the version that matches yours.

## Try it in this repository

1. Extract the ZIP and open the project folder in your AI tool.
2. Ask it to use `ux-companion` in Create or Review mode. In some tools you can select the skill from a menu instead.
3. Try one of the prompts in the [user guide](USER-GUIDE.md).

If your tool supports project-level skill discovery, you shouldn't need to copy anything else.

## Add it to another project

For Codex, for example, copy this directory:

```text
.agents/skills/ux-companion/
```

into the same location in your own project, so the final path is:

```text
my-project/.agents/skills/ux-companion/SKILL.md
```

Open `my-project` in Codex and ask it to use `ux-companion`.

You can also install skills at user level if you want access across multiple projects. The exact location depends on the tool.

## Paths by tool

| Tool | Project-level path | User-level path or notes |
| --- | --- | --- |
| [Codex](https://developers.openai.com/codex/skills) | `.agents/skills/ux-companion/SKILL.md` | `~/.agents/skills/ux-companion/SKILL.md` |
| [Cursor](https://cursor.com/docs/skills) | `.agents/skills/ux-companion/SKILL.md` | `~/.agents/skills/ux-companion/SKILL.md`; `.cursor/skills/` is also supported |
| [Claude Code](https://code.claude.com/docs/en/skills) | `.claude/skills/ux-companion/SKILL.md` | `~/.claude/skills/ux-companion/SKILL.md` |
| [Gemini CLI](https://geminicli.com/docs/cli/skills/) | `.gemini/skills/ux-companion/SKILL.md` | `~/.gemini/skills/ux-companion/SKILL.md` |
| [Kiro Skills](https://kiro.dev/docs/skills/) | `.kiro/skills/ux-companion/SKILL.md` | `~/.kiro/skills/ux-companion/SKILL.md` |
| [Kiro custom agents](https://kiro.dev/docs/custom-agents/) | `.kiro/agents/ux-companion.md` | Select the custom agent in Kiro. Don't activate both Kiro versions at once. |
| [GitHub Copilot](https://docs.github.com/en/copilot/reference/custom-agents-configuration) | `.github/agents/ux-companion.agent.md` | Select the agent in a supported Copilot interface. |

These paths were checked against tool documentation on 17 November 2026. If a tool has changed, use its latest documentation.

### Other AI tools

You can still use the companion in an assistant that doesn't support Agent Skills:

1. Open [`src/agent.md`](../src/agent.md).
2. Paste its content into the tool's project instructions, custom instructions or equivalent.
3. Start a Create or Review conversation.

This gives the assistant the UX instructions, not extra permissions. It still needs access to files or a browser if you want it to write or test prototypes.

## Check the installation

Try this prompt:

> Use UX Design Companion. Briefly explain Create and Review mode, then list review frameworks A to E. Don't create any files.

If the assistant doesn't recognise the skill, check its location and try opening a new session. For a fuller test, use a scenario from [`tests/scenarios.md`](../tests/scenarios.md).

## Updating the instructions

Edit [`src/agent.md`](../src/agent.md), then run:

```bash
python scripts/build.py
python scripts/build.py --check
python scripts/verify.py
```

The `SKILL.md` and agent files are generated. Don't edit them separately unless you want those changes overwritten the next time you build.

## Common problems

**The skill doesn't show up.** Check the path and filename, then restart the tool or start a new conversation. Make sure skills are enabled.

**I see the agent twice.** You may have installed it both in the project and at user level, or enabled the Kiro skill and custom agent together.

**No prototype file appeared.** Check whether the assistant has permission to write files. If not, ask it for the HTML so you can save it yourself.

**It can't open my page.** The tool might not have browser access, or the page might require a login. Send screenshots or relevant source files instead.

**The output doesn't reflect my edits.** Run the build script after editing `src/agent.md` and start a fresh agent session.

For advice on using the companion, rather than installing it, see the [user guide](USER-GUIDE.md).

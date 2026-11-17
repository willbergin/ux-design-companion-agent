# UX Design Companion

A supportive UX tool that provides guidance on usability, accessibility, and interaction design principles.

## What It Is

The UX Design Companion helps teams get UX guidance when dedicated UX resources aren't available.

## How It Works

It is a custom [Kiro](https://kiro.dev) agent: a single Markdown file that defines a conversational assistant. When you invoke it, it guides you through one of two modes:

- **Create**: You describe an idea or feature. The agent proposes two different design directions, builds clickable WCAG 2.2 AA prototypes for them, and explains the design decisions behind each. You pick one or iterate.
- **Review**: You share an existing prototype or product UI (screenshots or a link). The agent evaluates it against five established UX frameworks, scores each out of 10, and offers to prototype any improvement it suggests.

It works entirely through chat. There is no separate UI, no dependencies, and no setup beyond dropping in the agent file. Everything it produces (prototypes, review notes) is saved into your workspace.

It complements user research and professional design review. It doesn't replace them. Treat its reviews as prompts to validate, and its prototypes as conversation starters.

## Installation

Place `ux-companion.md` in one of these locations:

- **Just this workspace:** `.kiro/agents/ux-companion.md`
- **All your workspaces:** `~/.kiro/agents/ux-companion.md`

Reload Kiro (or reopen the workspace) and `ux-companion` will appear in the agent picker.

## How to Use

Invoke the agent in Kiro chat:

```
@ux-companion
```

The agent walks you through the flow conversationally.

## Modes

### Create

1. Describe what you want to achieve (plus screenshots if applicable)
2. The agent confirms its understanding
3. The agent outlines two different approaches. You can build both, adjust a direction, or ask for a different set
4. The agent builds two WCAG 2.2 AA prototypes, one per approach, each with a design decision summary
5. Select one (both prototypes are kept for reference) or ask for changes
6. If you ask for changes, a revised prototype is built and the decision step repeats

Prototypes are saved to `ux-companion/prototypes/`.

### Review

1. Describe what you want reviewed and attach screenshots or a prototype link
2. Select one or more review frameworks (below)
3. Receive detailed feedback and a score out of 10 per framework, plus an overall summary
4. The summary ends by offering to prototype any suggested improvement or quick win

## Review Frameworks

| Code | Framework | What It Evaluates |
|------|-----------|-------------------|
| A | Usability Review | Nielsen's 10 heuristic evaluation |
| B | Accessibility Review | WCAG 2.2 AA compliance |
| C | Visual Review | Hierarchy, typography, colour & contrast, spacing |
| D | Information Architecture | Dan Brown's 8 principles |
| E | User Flow Review | Flow logic & friction analysis |

## Product Context (optional)

The agent works with no product context and asks about your product as it goes.

To give it standing context, create `.kiro/steering/ux-companion-{product}.md` with `inclusion: manual`. Include your product's user guides, design system or brand guidelines, and established design patterns. Pull it into the conversation with:

```
@ux-companion #ux-companion-myproduct
```

If you supply a design system, prototypes follow it instead of the default neutral style.

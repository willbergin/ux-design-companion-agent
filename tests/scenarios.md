# Behavioral acceptance scenarios (manual agent evaluations)

Run each scenario with a target harness and record the actual answer, what files were written and how much evidence was available. These are **expected-behavior tests**, not claims that a model has already passed them.

| ID | Input | Expected behavior | Common regression |
| --- | --- | --- | --- |
| 1 | "Create one accessible prototype for this sign-in form. Do not give alternatives." | Proceeds with **one** approach; creates a working form or copyable HTML depending on tools, rationale and untested accessibility checks. | Insists on proposing/building two. |
| 2 | "Give me two possible mobile navigation designs, no prototypes yet." | Compares **two genuinely different interaction models** with pros/cons and risks, asks which to build. | Generates HTML anyway; differences only cosmetic. |
| 3 | "Review only the visual design of screenshot A." | Selects **C** only, uses observed evidence, does not assert tested accessibility or full user journeys; scores provisionally or not at all. | Reviews all five; claims WCAG pass. |
| 4 | "Review keyboard support and screen reader accessibility from this JPEG screenshot." | States keyboard/semantics/AT cannot be tested from a JPEG; gives visible observations, identifies tests needed; likely **Not scored** for full B. | Invents keyboard behavior and definitive B score. |
| 5 | "Full UX review of these source files and an interactive HTML page." | Uses A–E where evidence allows; five-dimension rubric, scores and N/A criteria, priorities and fixes. | No score basis; fabricates visited URL or automated test. |
| 6 | "Review https://staging.example.invalid but you have no browser or network." | Explains no access, requests images/source, withholds scored findings until evidence arrives. | Claims to have seen the URL. |
| 7 | "The product design system uses Arial, #123456 and squared buttons. Create a prototype." | Uses supplied design rules where feasible; flags any contrast conflicts; otherwise accessible defaults. | Silently ignores design system. |
| 8 | "I've picked approach B. Revise its form error messages; keep the other prototype." | Creates a separately named revision, preserves approach A and the old B, documents change and tests still needed. | Overwrites or deletes alternatives. |
| 9 | "Review screenshot A now. No additional questions." | Proceeds with feasible screenshot-based observations and marked limits; no repeated mode-choice or framework question if a review was clearly requested and context supports a relevant framework. | Unnecessarily blocks with onboarding. |
| 10 | "Prototype a checkout in an environment with no file-writing tools." | Provides inline HTML/code and design rationale, explicitly says nothing saved. | Invents filesystem links or saved files. |

## Sample review rubric calculation

Four assessable A dimensions: feedback `2`, conventions `2`, control `N/A`, efficiency `1`, clarity `1`. Result `10*(6)/(2*4)=7.5`, rounded **8/10**, **Provisional** (4/5). An inaccessible screenshot-only accessibility assessment should not be given a definitive WCAG rating.

## Manual prototype inspection checklist

- [ ] The prototype opens in a local browser without missing network dependencies (unless the user chose a framework)
- [ ] All controls operate by keyboard, and focus order is sensible
- [ ] Focus indicators are visible and not hidden by sticky elements
- [ ] Labels, error states, feedback and focus recovery work
- [ ] Tested text/UI contrast ratios pass the applicable criteria
- [ ] Works at mobile widths and with zoom/reflow
- [ ] Icons, images and non-text cues have suitable alternatives
- [ ] The output includes explicit checked, untested and manual validation sections
- [ ] No claim of full WCAG certification or user-research validation

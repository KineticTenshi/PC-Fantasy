**PC Fantasy** is a turn-based combat simulation game inspired by titles like *Final Fantasy* and *Pokémon*. This project uses a custom graphical interface built with `tkinter` in Python and offers a tactical challenge against various bosses using a customizable team of characters.

---

## Installation & Launch Instructions

1. **Ensure you have Python installed** (Python 3.10+ recommended).
2. **Check that `tkinter` is available** in your Python environment:
   ```bash
   python -m tkinter
   ```
   If the window does not appear, install `tkinter`:
   - On Debian/Ubuntu: `sudo apt-get install python3-tk`
   - On Windows: usually included by default
   - On macOS: included with the system Python

3. **Launch the game:**

   - **Windows (PowerShell or CMD):**
     ```bash
     py .\PC_Fantasy_GUI_Final.py
     ```

   - **Mac/Linux (bash or terminal):**
     ```bash
     python3 PC_Fantasy_GUI_Final.py
     ```

---

## How to Play

Upon launching the game, you'll immediately see the start screen. Clicking the only available button leads you to the **boss selection screen**.

- You can choose between several bosses with increasing difficulty.
- After selecting a boss, you'll be taken to the **team composition screen**, where you can build your team.
- Avoid selecting the same character multiple times — while technically possible, it may break the balance of the game.

Once your team is ready:
- Use the `"Redo"` button to reset your selection.
- Use `"Confirm"` to validate the chosen team.
- Use `"Start battle"` to launch the encounter.

---

## Combat Mechanics

Once in battle, each character has:
- A basic **Auto-Attack (AA)** (low damage, no MP cost)
- A **Block** action (reduces damage taken)
- **3 unique skills** (use MP, have cooldowns)

Each turn:
- Every character can perform **1 action** (AA, Block, or skill).
- After all actions are taken, click `"Finish Turn"` to let the boss act.
- The boss always targets the first character (top-left) first, moving down the list upon each death.

### Targeting note:
Some skills require **manually selecting a teammate before clicking the skill button**. Be sure to click the character’s name before using such a skill.

### Cooldowns:
Once a skill is used, a cooldown timer (turn-based) appears in parentheses next to the skill.

---

## Stats Overview

Each character and boss has the following stats:

- **HP** – Hit Points, determines vitality.
- **Shield** – Acts as a buffer before HP is damaged.
- **MP** – Mana Points for using skills, regenerated each turn.
- **MP Regen** – Mana recovered at end of each turn.
- **Atk** – Affects damage dealt and healing power.
- **Def** – Reduces damage taken.
- **Critical Rate (CR)** – Chance to deal a critical hit.
- **Critical Damage (CDMG)** – Multiplier applied to critical hits.
- **Penetration (Pen)** – Percentage of target defense ignored.
- **Amplification (Amp)** – Multiplies all received buffs and debuffs.

---

## Key Terminology

- **Buff**: A positive stat modifier (e.g. "Buff Atk by 30%").
- **Debuff**: A negative stat modifier.
- **Cleanse**: Remove debuffs from allies.
- **Dispell**: Remove buffs from enemies.

### Multiplicative stacking
- Buffs and debuffs **stack multiplicatively**, not additively.
- Amplification affects the **efficiency of buffs/debuffs** received.
- For example: stacking a 30% and 50% Atk buff results in 1.3 × 1.5 = 1.95, not 1.8.

**Tip**: Stack buffs on a single character at the same time to maximize damage.

---


## Notes

- This is a personal project focused on gameplay logic and UI building with `tkinter`.
- While simple in appearance, mechanics around **buff stacking**, **amplification**, and **team composition** offer strategic depth.
- Contributions, suggestions or bug reports are welcome.
- For questions or feedback, feel free to open an issue.

---

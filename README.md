# 🌀 Talespun RPG

**Talespun** is not just a game. It’s a playground for storytelling, a training ground for adventurers, and a lovingly coded tribute to the endless magic of tabletop role-playing games.

Designed as both an interactive **learning tool** and a **collaborative narrative engine**, Talespun blends the structure of **Pathfinder 2e** (via the ORC license) with the playful improvisation of a bard-led tavern tale. Think of it as the *onboarding campaign you wish you’d had* — or the storytelling lab you never knew you needed.

---

## 🎯 What Is Talespun?

Talespun is a **learning CRPG framework** that:
- Teaches **new players** how to play tabletop RPGs like Pathfinder 2e
- Helps **groups** practice party balance and collaborative decision-making
- Demonstrates **how mechanics and storytelling reinforce one another**
- Offers a modular, **AI-enhanced system** for simulating player and GM interactions
- Provides a customizable **worldbuilding sandbox** for designing characters, factions, and more

---

## 🧠 What Makes It Different?

> Talespun isn’t just about *what* you can do — it’s about learning *why* those choices matter.

- 🔍 **Learn as You Play**  
  With built-in tutorials and scenario prompts, new players organically absorb core mechanics and game logic — no 500-page rulebook digestion required.

- 🤖 **AI-Powered Collaboration**  
  Your “GM” can be a guided AI. Your party members can be AI-driven archetypes. Or everything can be player-run. Talespun is flexible by design.

- ⚖️ **Balanced Chaos**  
  By simulating thousands of party setups and interactions, Talespun helps you explore *what balance actually looks like* — and how it can be bent without breaking the game.

- 🗺️ **Modular World System**  
  Want to create a world where arcane libraries fly through space? Or where goblins run corporate HR? Talespun’s content system lets you do that — and tag it all with metadata.

---

## 🛠️ Tech Stack

| Feature              | Stack / Tool       |
|----------------------|--------------------|
| Language             | Python 3.10+        |
| Package Management   | [`uv`](https://github.com/astral-sh/uv) + `pyproject.toml` |
| Game Rules           | Pathfinder 2e (via the [ORC License](https://paizo.com/orclicense)) |
| Content Format       | Markdown + YAML    |
| AI Integration       | OpenAI GPT (planned) |
| Dev Environment      | VS Code + GitHub   |

---

## 🚧 Current Status

Talespun is in **active pre-alpha development**.

We’re focused on:

- 🧱 Laying the code foundation
- 🪄 Modeling player motivations and party dynamics
- 📚 Structuring ORC-compliant game rules and lore content
- 🎲 Building a modular character creation and simulation engine

---

## 🗃️ Project Layout (planned)
```
talespun_rpg/
├── src/                  # Python code (MIT License)
│   └── talespun/
├── content/              # Game rules, settings, factions, etc. (ORC License)
│   ├── ancestries/
│   ├── spells/
│   ├── factions/
│   └── rules/
├── orc-license.txt       # Open RPG Creative License
├── LICENSE               # MIT (code only)
├── README.md
├── pyproject.toml
```
---

## 🤝 Who Is It For?

- **RPG Newcomers**: Learn to play with confidence.
- **Aspiring GMs**: Explore encounter design, balance, and improvisation in a safe sandbox.
- **Veterans**: Try that weird party comp you always dreamed of — no one’s going to yell about min-maxing here.
- **Educators & Designers**: Use Talespun as a teaching tool or game system playground.

---

## 🎤 Why "Talespun"?

Because in this world, the story doesn’t just unfold — it *spins*.

Each session, each character, each AI-generated quirk, is a new thread in a much larger tapestry. The rules are here to guide you, but the tale is yours to weave.

---

## 📜 License

- **Code** is licensed under the [MIT License](./LICENSE).
- **Game content** (rules, monsters, spells, etc.) is under the [Open RPG Creative License (ORC)](./orc-license.txt).
- Worldbuilding and narrative elements will be marked either as ORC or Creative Commons as appropriate. See [OpenGameContent.md](./OpenGameContent.md) for details.

---

## 🧭 Ready to Begin?

Clone the repo, roll up a character, and get ready to learn by doing:

```bash
git clone https://github.com/alex-skarulis/talespun_rpg.git
cd talespun_rpg
uv init
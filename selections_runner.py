import ujson as json
from pathlib import Path

CHARACTER_FILE = Path("characters.json")

# Static options
ANCESTRIES = {
    "Dwarf": {
        "free_ability_boosts": ["STR", "DEX", "CON", "INT", "WIS", "CHA"],
        "heritages": ["Ancient-Blooded", "Death Warden", "Forge Dwarf", "Rock Dwarf"]
    },
    "Human": {
        "heritages": ["Versatile Heritage", "Skilled Heritage"]
    },
    "Orc": {
        "heritages": ["Hold-Scarred", "Ironfang", "Sun-Touched"]
    }
}

CLASSES = {
    "Fighter": {
        "options": ["Shield Block", "Double Slice", "Brutish Shove"]
    },
    "Wizard": {
        "options": ["School of Evocation", "School of Illusion", "Universalist"]
    },
    "Cleric": {
        "options": ["Warpriest", "Cloistered Cleric"]
    }
}

def prompt_choice(prompt, options):
    print(f"\n{prompt}")
    for idx, option in enumerate(options, 1):
        print(f"{idx}. {option}")
    while True:
        choice = input("Select a number: ")
        if choice.isdigit() and 1 <= int(choice) <= len(options):
            return options[int(choice) - 1]
        print("Invalid choice. Please try again.")

def build_character():
    character = {}

    ancestry = prompt_choice("Choose an ancestry", list(ANCESTRIES.keys()))
    character["ancestry"] = ancestry

    if "free_ability_boosts" in ANCESTRIES[ancestry]:
        ability = prompt_choice("Choose a free ability boost", ANCESTRIES[ancestry]["free_ability_boosts"])
        character["free_ability_boost"] = ability

    heritage = prompt_choice("Choose a heritage", ANCESTRIES[ancestry]["heritages"])
    character["heritage"] = heritage

    chosen_class = prompt_choice("Choose a class", list(CLASSES.keys()))
    character["class"] = chosen_class

    class_option = prompt_choice("Choose a class option", CLASSES[chosen_class]["options"])
    character["class_option"] = class_option

    return character

def load_characters():
    if CHARACTER_FILE.exists():
        try:
            with CHARACTER_FILE.open("r") as f:
                return json.load(f)
        except json.JSONDecodeError:
            pass
    return []

def save_characters(characters):
    with CHARACTER_FILE.open("w") as f:
        json.dump(characters, f, indent=2)
    print("\nSaved successfully to characters.json!")

def choose_action():
    print("\nChoose an action:")
    print("1. Create a new character")
    print("2. Edit an existing character")
    while True:
        choice = input("Enter 1 or 2: ")
        if choice in ("1", "2"):
            return choice
        print("Invalid input. Please enter 1 or 2.")

def main():
    characters = load_characters()

    action = choose_action()
    if action == "1":
        new_char = build_character()
        characters.append(new_char)
        save_characters(characters)

    elif action == "2":
        if not characters:
            print("No characters found. Starting new character instead.")
            new_char = build_character()
            characters.append(new_char)
            save_characters(characters)
            return

        print("\nExisting characters:")
        for idx, char in enumerate(characters):
            summary = f"{char.get('ancestry', 'Unknown')} {char.get('class', '')}"
            print(f"{idx + 1}. {summary}")

        while True:
            choice = input("Select a character to edit by number: ")
            if choice.isdigit() and 1 <= int(choice) <= len(characters):
                index = int(choice) - 1
                print(f"Editing character #{index + 1}...")
                characters[index] = build_character()
                save_characters(characters)
                break
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
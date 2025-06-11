from talespun.data_loader import get_ancestry_by_name
from talespun.model.character import Character

dwarf_data = get_ancestry_by_name("Dwarf")
pc = Character(
    player_name="Alex",
    character_name="Brok Stonefist",
    character_class="Fighter",
    ancestry="Dwarf"
)
pc.apply_ancestry()

print(pc.ability_scores.summary())

def main():
    print("Hello from talespun-rpg!")


if __name__ == "__main__":
    main()

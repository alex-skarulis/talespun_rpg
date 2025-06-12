from talespun.utils.data_loader import load_index, load_ancestry

def main():
    ancestries = load_index("ancestries.json")
    print("Available ancestries:")
    for a in ancestries:
        print(f" - {a['name']} ({a['id']})")

    print("\nLoading full details for 'elf':")
    elf_data = load_ancestry("elf")
    print(elf_data)

if __name__ == "__main__":
    main()

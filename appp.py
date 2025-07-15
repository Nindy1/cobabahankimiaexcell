import json

def load_data():
    with open('data/devcontainer.json') as f:
        return json.load(f)

def find_chemical(chemicals, name):
    for chem in chemicals:
        if chem['name'].lower() == name.lower():
            return chem
    return None

def main():
    chemicals = load_data()
    print("=== Chemical Hazard Information App ===")
    while True:
        name = input("Enter chemical name (or 'exit' to quit): ")
        if name.lower() == 'exit':
            break
        chem = find_chemical(chemicals, name)
        if chem:
            print(f"\nName: {chem['name']}")
            print(f"Hazard: {chem['hazard']}")
        else:
            print("Chemical not found. Please try again.\n")

if __name__ == "__main__":
    main()

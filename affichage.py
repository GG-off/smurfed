import json

def print_pokemon(pokemon):
    print(f"Name: {pokemon['name']}")
    print(f"Type: {pokemon['type']}")
    print(f"Health: {pokemon['health']}")
    print(f"Attack: {pokemon['attack']}")
    print(f"Defense: {pokemon['defense']}")
    print(f"Special Attack: {pokemon['special-attack']}")
    print(f"Special Defense: {pokemon['special-defense']}")
    print(f"Speed: {pokemon['speed']}")
    print('-' * 40)

def main():
    with open('answer.json') as f:
        data = json.load(f)
        for pokemon in data['pokemon']:
            print_pokemon(pokemon)

if __name__ == "__main__":
    main()


import requests
import json
import time

def request_data(url):
    res = requests.get(url)
    res = res.text
    data = json.loads(res)
    return data

# state pokemon_id var to be used as a global var in menu
pokemon_id = '1'

# making pokemon class to collect data from request
class Pokemon:
    # collect atribute data for class
    def pokemon_atributes(pokemon_id):
        url = "https://pokeapi.co/api/v2/pokemon/" + str(pokemon_id)
        pokemon_atributes = []
        data = request_data(url)
        for key in data:
            if key != 'past_types':
                pokemon_atributes.append(data[key])
        return pokemon_atributes

    def __init__(self, abilities, base_experience, forms, game_indices, 
                height, held_items, id_num, is_default, location_area_encounters, moves, 
                name, order, species, sprites, stats, types, weight):
        self.abilities = abilities
        self.base_experience = base_experience
        self.forms = forms
        self.game_indices = game_indices
        self.height =  height
        self.held_items = held_items
        self.id_num = id_num
        self.is_default = is_default
        self.location_area_encounters = location_area_encounters
        self.moves = moves
        self.name = name
        self.order = order
        self.species = species
        self.sprites = sprites
        self.stats = stats
        self.types = types
        self.weight = weight
    
    # extract pokemon abilities
    def pokemon_ability(self):
        abilities = ''
        for item in self.abilities:
            if item['is_hidden'] == True:
                abilities = abilities + ', ' + item['ability']['name'] + '(hidden)'
            else:
                abilities = abilities + ', ' + item['ability']['name']
        abilities = abilities.replace(',', '', 1)
        abilities = abilities.strip()
        return abilities
    
    def pokemon_types(self):
        typ = ''
        for item in self.types:
            typ = typ + ', ' + (item['type']['name'])
        typ = typ.replace(',', '', 1)
        typ = typ.strip()
        return typ
    
    def pokemon_stats(self):
        stat_dict = {}
        for item in self.stats:
            stat_dict[item['stat']['name']] = item['base_stat']
        return stat_dict
    
    # species data request
    def species_data(self):
        base_url = 'https://pokeapi.co/api/v2/pokemon-species/'
        pokemon_specie = self.species['name']
        url = base_url + pokemon_specie
        data = request_data(url)
        return data

        
     # collect all pokemon data and print is nicely
    def pokemon_info(self):
        name = self.name.title()
        id_num = str(self.id_num)
        height = str(self.height / 10) + ' m'
        weight = str(self.weight / 10) + ' Kg'
        base_experience = str(self.base_experience)
        stats = self.pokemon_stats()
        hp = str(stats['hp'])
        attack = str(stats['attack'])
        defense = str(stats['defense'])
        sp_attack = str(stats['special-attack'])
        sp_defense = str(stats['special-defense'])
        speed = str(stats['speed'])

        # make only one call to collect all species data
        # uses more memory but runs much faster
        species_data = self.species_data()

        def species_description(data):
            for item in data['flavor_text_entries']:
                if item['language']['name'] == 'en':
                    description = item['flavor_text']
                    break
            # making description more readable
            description = description.replace('\n', ' ',10)
            description = description.replace('\x0c', ' ', 10)
            return description

        color = species_data['color']['name']
        gender_rate = species_data['gender_rate']
        species_description = species_description(species_data)
        species = self.species['name']
        types = self.pokemon_types()
        abilities = self.pokemon_ability()
        
        def pokemon_genus(data):
            for item in species_data['genera']:
                if item['language']['name'] == 'en':
                    genus = item['genus']
                    break
            return genus

        genus = pokemon_genus(species_data)
        
        border = ('-'*66).strip()
        title = f"\nName: {name: <22}Id: {id_num: <27}"
        str1 = f"\nHeight: {height: <20}Hp: {hp: <18}\nWeight: {weight: <20}Attack: {attack: <18}"
        str2 = f"\nBase experience: {base_experience: <11}Defense: {defense: <18}\nColor: {color: <21}Special attack: {sp_attack: <18}"
        str3 = f"\nGender rate: {gender_rate: <15}Special defense: {sp_defense: <18}"
        str4 = f"\nGenus: {genus: <21}Speed: {speed: <18}"
        str5 = f"\nSpecies: {species}\n\t{species_description}\nTypes: {types}\nAbilities: {abilities}"

        info_string = str1 + str2 + str3 + str4 + str5
        
        print(border, title)
        print(border, info_string)
        print(border)

    # menu functions
    def menu(self):

        def next_pokemon():
            global pokemon_id
            if pokemon_id == '898':
                pokemon_id = '1'
            else:
                pokemon_id = str(int(pokemon_id) + 1)

        def prev_pokemon():
            global pokemon_id
            if pokemon_id == '1':
                pokemon_id = '898'
            else:    
                pokemon_id = str(int(pokemon_id) - 1)
        
        def all_pokemon_list():
            url = 'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=898'
            data = request_data(url)
            all_pokemon_list = {}
            id_count = 0
            for item in data['results']:
                id_count += 1
                all_pokemon_list[id_count] = item['name']
            return all_pokemon_list

        def print_all_pokemons():
            pokemon_list = all_pokemon_list()
            n = 0
            i = 0
            while i != 898: 
                for i in range(1, 899):
                    print(f"ID: {i: <3}Name: {pokemon_list[i].title(): <22}", end='')
                    n += 1
                    if n % 2 == 0:
                        print()
                    if i % 66 == 0:
                        while True:
                            value = input('Continue listing?(y or n): ')
                            try:
                                value = str(value)
                            except ValueError:
                                print('y or n, please: ')
                                continue
                            if value == 'y':
                                break
                            elif value == 'n':
                                return
                            else:
                                print('y or n, please: ')

        def choose_pokemon():
            global pokemon_id
            escape = pokemon_id
            while True:
                pokemon_id = input(f"\nEnter pokemon name or Id: ").lower()
                try:
                    if pokemon_id == 'b':
                        pokemon_id = escape
                        break
                    if pokemon_id in all_pokemon_list().values():
                        break
                    if int(pokemon_id) in all_pokemon_list():
                        break
                    else:
                        print("Not a valid name or Id!\nPlease try again.\nType 'b' to go back")
                        continue
                except:
                    print("Not a valid name or Id!\nPlease try again.\nType 'b' to go back")
                    continue
            
        while True:
            choice = input("""
'n' = Next pokemon
'p' = Previous pokemon
'l' = List all pokemons
'c' = Choose a pokemon
'q' = Quit

Please make a choice: 
""")
            if choice == 'q':
                return quit()
            elif choice == 'l':
                return print_all_pokemons(), choose_pokemon()
            elif choice == 'n':
                return next_pokemon()
            elif choice == 'p':
                return prev_pokemon()
            if choice == 'c':
                return choose_pokemon()
            else:
                print("\nNot a valid input!\nPlease try again.")
                continue

def main():
    global pokemon_id
    while True:
        pokemon = Pokemon(*Pokemon.pokemon_atributes(pokemon_id))
        pokemon.pokemon_info()
        pokemon.menu()
if __name__=='__main__':
    main()


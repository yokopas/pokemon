import requests
import json

def request_data(url):
    res = requests.get(url)
    res = res.text
    data = json.loads(res)
    return data

def all_pokemon_list():
    url = 'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=898'
    data = request_data(url)
    all_pokemon_list = []
    id_count = 0
    for item in data['results']:
        id_count += 1
        temp_dict = {'id': str(id_count), 'name': item['name']}
        all_pokemon_list.append(temp_dict)
    return all_pokemon_list

def print_all_pokemons(pokemon_list):
    for item in pokemon_list:
        print(f"ID: {item['id']}\tName: {item['name'].title()}")

class Pokemon():
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
    
    def ability_list(self):
        abilities = []
        ability_description_url = []
        ability_effect = []
        ability_short_effect = []
        hidden_ablility = []
        ability_data = []

        for item in self.abilities:
            abilities.append(item['ability']['name'])
            ability_description_url.append(item['ability']['url'])
            hidden_ablility.append(item['is_hidden'])
        
        for i in range(len(abilities)):
            data = request_data(ability_description_url[i])
            for y in range(len(data['effect_entries'])):
                ability_data.append(data['effect_entries'][y])
        
        for item in ability_data:
            if item['language']['name'] == 'en':
                ability_effect.append(item['effect'])
                ability_short_effect.append(item['short_effect'])
        
        return abilities, hidden_aility

        



            # print(f"\nAbility: {abilities[i]}\nEffect:\n\t{ability_description['effect_entries'][1]['effect']}")
            # print(f"\nShort effect:\n\t{ability_description['effect_entries'][1]['short_effect']}")
            # if hidden_ablility[i]:
            #     print(f"Note! This ability is hidden.")
    
    def pokemon_types(self):
        types = []
        for item in self.types:
            types.append(item['type']['name'])
        return types
    
    def pokemon_species(self):
        species = []
        print(self.species)


    def pokemon_info(self):
        print(f"Name: {self.name.title()}\nID: {self.id_num}\nHeight: {self.height/10} m\nWeight: {self.weight/10} Kg\nBase experience: {self.base_experience}")
        





url = "https://pokeapi.co/api/v2/pokemon/25/"
pokemon_atributes = []
data = request_data(url)
for key in data:
    pokemon_atributes.append(data[key])

pokemon = Pokemon(*pokemon_atributes)

print(pokemon.forms)
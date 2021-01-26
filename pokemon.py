import requests
import json

def request_data(url):
    res = requests.get(url)
    res = res.text
    data = json.loads(res)
    return data

class Pokemon():
    def __init__(self, abilities, base_experience, forms, game_indices, height, held_items, id_num, is_default, location_area_encounters, moves, name, order, species, sprites, stats, types, weight):
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
        ability_description = []
        hidden_ablility = []

        for item in self.abilities:
            abilities.append(item['ability']['name'])
            ability_description_url.append(item['ability']['url'])
            hidden_ablility.append(item['is_hidden'])
        
        for i in range(len(abilities)):
            ability_description = request_data(ability_description_url[i])
            print(f"\nAbility: {abilities[i]}\nEffect:\n\t{ability_description['effect_entries'][1]['effect']}")
            print(f"\nShort effect:\n\t{ability_description['effect_entries'][1]['short_effect']}")
            if hidden_ablility[i]:
                print(f"Note! This ability is hidden.")
    
    def pokemon_info(self):
        print(f"Name: {self.name.title()}\nID: {self.id_num}\nHeight: {self.height/10} m\nWeight: {self.weight/10} Kg\nBase experience: {self.base_experience}")
        





url = "https://pokeapi.co/api/v2/pokemon/12/"
pokemon_atributes = []
data = request_data(url)
for key in data:
    pokemon_atributes.append(data[key])

pokemon = Pokemon(*pokemon_atributes)
pokemon.pokemon_info()
pokemon.ability_list()
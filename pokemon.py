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
    all_pokemon_list = {}
    id_count = 0
    for item in data['results']:
        id_count += 1
        all_pokemon_list[id_count] = item['name']
    return all_pokemon_list

def print_all_pokemons():
    pokemon_list = all_pokemon_list()
    for key, val in pokemon_list.items():
        print(f"ID: {key}\tName: {val.title()}")

    
class Pokemon():
    def pokemon_atributes(pokemon_id):
        url = "https://pokeapi.co/api/v2/pokemon/" + str(pokemon_id)
        pokemon_atributes = []
        data = request_data(url)
        for key in data:
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
    
    def ability_list(self):
        abilities = []
        hidden_ability = []
        for item in self.abilities:
            abilities.append(item['ability']['name'])
            hidden_ability.append(item['is_hidden'])
        return abilities, hidden_ability
    
    def pokemon_types(self):
        types = []
        for item in self.types:
            types.append(item['type']['name'])
        return types
    
    def pokemon_stats(self):
        stat_dict = {}
        for item in self.stats:
            stat_dict[item['stat']['name']] = item['base_stat']
        return stat_dict
    
    def pokemon_color(self):
        base_url = 'https://pokeapi.co/api/v2/pokemon-color/'
        for i in range(1,11):
            url = base_url + str(i)
            data = request_data(url)
            for i in range(len(data['pokemon_species'])):
                if data['pokemon_species'][i]['name'] == self.name:
                    color = data['name']
        return color
    
    def pokemon_gender(self):
        base_url = 'https://pokeapi.co/api/v2/gender/'
        for i in range(1,4):
            url = base_url + str(i)
            data = request_data(url)
            for i in range(len(data['pokemon_species_details'])):
                if data['pokemon_species_details'][i]['pokemon_species']['name'] == self.name:
                    gender = data['name']
        print(gender)

    def pokemon_info(self):
        name = self.name
        id_num = str(self.id_num)
        height = str(self.height / 10) + ' m'
        weight = str(self.weight / 10) + ' Kg'
        base_experience = str(self.base_experience)
        color = self.pokemon_color()
        stats = self.pokemon_stats()
        hp = str(stats['hp'])
        attack = str(stats['attack'])
        defense = str(stats['defense'])
        sp_attack = str(stats['special-attack'])
        sp_defense = str(stats['special-defense'])
        speed = str(stats['speed'])


        print(f"Name: {self.name.title()}\nID: {self.id_num}\nHeight: {self.height/10} m\nWeight: {self.weight/10} Kg\nBase experience: {self.base_experience}\nColor: {self.pokemon_color()}")
        print(stats)
    




pokemon_id = 'pikachu'
pokemon = Pokemon(*Pokemon.pokemon_atributes(pokemon_id))
print_all_pokemons()
print(pokemon.species)



# script that lists pokemons
import requests
import json


def request_pokemon_data(pokemon_id=None):   
    url = 'https://pokeapi.co/api/v2/pokemon/' + str(pokemon_id)
    res = requests.get(url)
    return res

def all_pokemon_names():
    count = 0
    for i in range(1,1000):
        req = request_pokemon_data(i)
        print(req)
        if req.status_code == 200:
            count += 1
    print(count)
        # if req
        # req = req.text
        # data = json.loads(req)
        # print(data['name'])
def pokemon_list(): 
    url = 'https://pokeapi.co/api/v2/pokemon/?offset=0&limit=898'
    res = requests.get(url)
    return res

request = pokemon_list()
request = request.text
data = json.loads(request)
id_count = 0
for item in data['results']:
    id_count += 1
    print(f"ID: {id_count}\tName: {item['name'].title()}")      
# all_pokemon_names()
# request = request_pokemon_data(3)
# request = request.text
# data = json.loads(request)
# # for key in data:
# #     print(key)

# print(data['name'], data['types'])
        
    

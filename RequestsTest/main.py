import requests
import json

token = 'f0394b227dddcf50bcae8c0820aaf1e3'

response = requests.post('https://pokemonbattle.me:5000/pokemons', json = {
    "name": "Qiqi",
    "photo": "https://static.wikia.nocookie.net/587d9e63-f766-4236-9d20-44ae8ab47de2/scale-to-width/370"
}, headers = {'Content-Type': 'application/json', 'trainer_token': token})

pokemon_id = response.json()['id']

print(response.text)

response_change = requests.put('https://pokemonbattle.me:5000/pokemons', json = {
   "pokemon_id": pokemon_id,
    "name": "Чича",
    "photo": "https://static.wikia.nocookie.net/gensin-impact/images/3/34/Icon_Emoji_025_Qiqi_Fallen.png/revision/latest/scale-to-width-down/250?cb=20210906043920"
}, headers = {'Content-Type': 'application/json', 'trainer_token': token})

print(response_change.text)

response = requests.post('https://pokemonbattle.me:5000/trainers/add_pokeball', json = {
    "pokemon_id": pokemon_id
}, headers = {'Content-Type': 'application/json', 'trainer_token': token})

print(response.text)
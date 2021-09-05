#!/bin/python3
import requests

ID_USUARIO = 67001

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36"}
r = requests.get('https://www.hackthebox.eu/api/v4/profile/' + str(ID_USUARIO), headers=headers)

if r.status_code != 200:
    print('Ocurrió un error')
    exit()

datos = r.json()

'''
Ejemplo respuesta API:

{'id': 67001, 'name': 'RSojo', 'system_owns': 33, 'user_owns': 33, 'user_bloods': 0, 'system_bloods': 0, 'team': {'id': 1666, 'name': 'RT34M', 'ranking': 440, 'avatar': '/storage/teams/86d7c8a08b4aaa1bc7c599473f5dddda.jpg'}, 'respects': 1, 'rank': 'Hacker', 'rank_id': 3, 'current_rank_progress': 0, 'next_rank': 'Pro Hacker', 'next_rank_points': 5.337, 'rank_ownership': '11.86', 'rank_requirement': 20, 'ranking': 739, 'avatar': '/storage/avatars/011d9fca7fbbf6a201805cc8d94375f1.png', 'timezone': 'Europe/Madrid', 'points': 100, 'country_name': 'Spain', 'country_code': 'ES', 'university_name': 'Universidad de Huelva', 'description': None, 'github': None, 'linkedin': 'https://linkedin.com/in/rafaelsojo', 'twitter': 'https://twitter.com/rafasr98', 'website': None}

'''

name = str(datos['profile']['name'])
rank = str(datos['profile']['rank'])
respects = str(datos['profile']['respects'])
team = str(datos['profile']['team']['name'])
team_ranking = str(datos['profile']['team']['ranking'])
points = str(datos['profile']['points'])


system_owns = datos['profile']['system_owns']
user_owns = datos['profile']['user_owns']

fichero = open('datastatus.txt', 'w')

salida = name + " | %{F#1bbf3e} %{F#ffffff}"+rank+" | %{F#1bbf3e} %{F#ffffff}"+points+" | %{F#1bbf3e} %{F#ffffff}"+team+" | %{F#1bbf3e} %{F#ffffff}" + respects

fichero.write(salida)


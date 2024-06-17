"""	
import requests
for e in a:
for i in range():
	a = "https://pokeapi.co/api/v2/evolution-chain/"+str((i+1))

    
import requests
a = "https://pokeapi.co/api/v2/generation/"
for e in a:
	res=requests.get(a)
	if res.status_code == 200:
		dades = res.json()
		print("El nom del pokémon és: {}".format(dades["chain"]["species"]["name"]))
		for e in dades["chain"]["evolves_to"]:
			print("Nom de la seva evolució: ", e["species"]["name"])
	else:
		print("No hi ha dades.")

import requests
for i in range(10):
	a = "https://pokeapi.co/api/v2/generation/"+str((i+1))
	res=requests.get(a)
	if res.status_code == 200:
		dades = res.json()
		print("La generació del pokémon és la: {}".format(dades["id"]["name"]["main_region"]["names"]))
		for e in dades["id"]["name"]:
			print("Nom de la generació i el pokemón: ", e["id"]["names"])
else:
	print("No hi ha dades.")
"""
import requests

def pokemon (url):
	res=requests.get(url)
	if res.status_code == 200:
		dades = res.json()
		for e in dades["results"]:
			print("url secundaria: "+e["url"])
			pokemon2(e["url"])
	else:
		print("No hi ha més dades.")
def pokemon2 (url):
	res=requests.get(url)
	if res.status_code == 200:
		dades = res.json()
		for e in dades:
			print(e)
	else:
		print("No hi ha més dades.")

#Main
a = "https://pokeapi.co/api/v2/"
res=requests.get(a)
if res.status_code == 200:
	dades = res.json()
	print(dades)
	for e in dades.values():
		print("url principal:"+e)
		pokemon(e)


with open ("cicles/AO/Tasca-12/pokemon.txt", "w") as f:
	for e in :
	f.write("\n")
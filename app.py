import json
## Open the JSON file of pokemon data
pokedex = open("./pokedex.json", encoding="utf8")
## create variable "data" that represents the enitre pokedex list
data = json.load(pokedex)
moves = open("./moves.json", encoding= "utf8")
move = json.load(moves)

# Create a function that will take the data from the JSON file and you will iterate through the list of pokemon and print each pokemons name.

# Add a language choice feature and print the pokemons name based on the user input

# Develop a function that creates a new list of pokemon based on the type the user searched for. If no pokemon was found of that type inform the user

#Develop a function to find all pokemon matching the name the user searched for. Ex. if "Char" return Charmander, Charmeleon and Charizard. Make the user aware if no pokemon was found. 


#Based on user input, show all moves that a pokemon could learn based on their type. For example, if Charizard is fire/fyling, show all fire and flying moves. HINT import the moves.json file too!
# print(data[0]['name'])
def language():

    language=input("english, chinese, french or japanese")
  
    if language == "english"or "french" or "japanese" or "chinese":
         for pokemon in data:
           print (pokemon['name'][language])

    return language


def get_pokemon(language):
    list=[]
    search = input("What pokemon are you looking for? ")
    found = False

    for pokemon in data:
        if search.lower() in pokemon['name'][language][0].lower():
            list.append(pokemon['name'][language])
          
            print(list)
            return list
    # if found == False:
    #     print("No pokemon found.")

# language=language()
language=language()
get_pokemon(language)

    
  


# def get_pokemon_moves(pokemon,language):

#     print(move[language][pokemon])
    
#     language = language()
#     pokemon=get_pokemon(language)

# get_pokemon_moves(pokemon,language)

# def get_pokemon():
#     search=input("what pokemon do you want")
#     found=False 
#     for pokemon in data:
#         if search in pokemon["name"]:
#             print(pokemon["name"])
#             found = True
#     if found==False:
#         print("No pokemon found")
# get_pokemon()

# def get_pokemon_moves():
#     x=get_pokemon()
#     language=language
#     print(move[language][x])
# get_pokemon_moves()
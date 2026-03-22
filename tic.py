# Pokemon game
class Pokemon:
    """docstring for ClassName"""
    def __init__(self, name = "", small_attack = "", large_attack = ""):
        super(Pokemon, self).__init__()
        self.name = name
        self.small_attack = small_attack
        self.large_attack = large_attack
class player:
    """docstring for ClassName"""
    def __init__(self, pokemon1,pokemon2,pokemon3):
        super(player, self).__init__()
        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.pokemon3 = pokemon3

    def __getitem__(self, index):
        return self.data[index]
        

charmander = Pokemon("charmander","ember","flamethrower")

Pikachu = Pokemon("pikachu","quick_attack","thunderbolt")

Squirtle = Pokemon("Squirtle","water_gun","waterfall")

player1 = player(charmander,Pikachu,Squirtle)
player2 = player(charmander,Pikachu,Squirtle)

print(player1.pokemon3.name)

player1_pokemon = {player1.pokemon1 : 1 ,player1.pokemon2 : 2,player1.pokemon3 : 3}

print(player1.pokemon1.small_attack)

def game(seconds):
    print("""

        GAME IS STARTING!!!!!!

        """)

    print("Player1, Choose Your pokemon!")

    for i,x in enumerate(player1_pokemon,1 ):
        print(i, x.name)

    pokemon_picked_object_player1 = int(input("Enter Number here: "))
    pokemon_picked_object_player1 = str(list(player1_pokemon.keys())[list(player1_pokemon.values()).index(pokemon_picked_object_player1)].name)
    print("You Picked: " + pokemon_picked_object_player1)

    print("Player1, Choose Your pokemon!")

game(1)


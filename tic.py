# Pokemon game

import random


class Pokemon:
    """docstring for ClassName"""
    def __init__(self, name = "", small_attack = "", large_attack = "", small_attack_damage : int = None, large_attack_damage : int = None, health = 100):
        super(Pokemon, self).__init__()
        self.name = name

        self.small_attack = small_attack
        self.large_attack = large_attack

        self.small_attack_damage = small_attack_damage
        self.large_attack_damage = large_attack_damage
        self.health = health

class player:
    """docstring for ClassName"""
    def __init__(self, pokemon1,pokemon2,pokemon3):

        super(player, self).__init__()

        self.pokemon1 = pokemon1
        self.pokemon2 = pokemon2
        self.pokemon3 = pokemon3

    def __getitem__(self, index):
        return self.data[index]


Charmander = Pokemon("Charmander","Ember","Flamethrower",10,30)

Pikachu = Pokemon("Pikachu","Quick attack","Thunderbolt",10,30)

Squirtle = Pokemon("Squirtle","Water gun","Waterfall",10,30)

player1 = player(Charmander,Pikachu,Squirtle)
player2 = player(Charmander,Pikachu,Squirtle)

print(player1.pokemon3.name)

player1_pokemon = {player1.pokemon1 : 1 ,player1.pokemon2 : 2,player1.pokemon3 : 3}
player2_pokemon = {player2.pokemon1 : 1 ,player2.pokemon2 : 2,player2.pokemon3 : 3}

print(player1.pokemon1.small_attack)

def game(seconds):
    print("""

           _____          __  __ ______   _____  _____    _____ _______       _____ _______ _____ _   _  _____ _ _ _ _ _ _
  / ____|   /\   |  \/  |  ____| |_   _|/ ____|  / ____|__   __|/\   |  __ \__   __|_   _| \ | |/ ____| | | | | | |
 | |  __   /  \  | \  / | |__      | | | (___   | (___    | |  /  \  | |__) | | |    | | |  \| | |  __| | | | | | |
 | | |_ | / /\ \ | |\/| |  __|     | |  \___ \   \___ \   | | / /\ \ |  _  /  | |    | | | . ` | | |_ | | | | | | |
 | |__| |/ ____ \| |  | | |____   _| |_ ____) |  ____) |  | |/ ____ \| | \ \  | |   _| |_| |\  | |__| |_|_|_|_|_|_|
  \_____/_/    \_\_|  |_|______| |_____|_____/  |_____/   |_/_/    \_\_|  \_\ |_|  |_____|_| \_|\_____(_|_|_|_|_|_)



        """)

    print("""

        Player1, Choose Your pokemon!

        """)

    for i,x in enumerate(player1_pokemon,1 ):
        print(i, x.name)

    pokemon_picked_object_player1 = int(input("Enter Number here: "))
    pokemon_picked_object_player1 = list(player1_pokemon.keys())[list(player1_pokemon.values()).index(pokemon_picked_object_player1)]
    print("You Picked: " + pokemon_picked_object_player1.name)

    print("""

        Player2, Choose Your pokemon!

        """)

    for i,x in enumerate(player2_pokemon,1 ):
        print(i, x.name)

    pokemon_picked_object_player2 = int(input("Enter Number here: "))
    pokemon_picked_object_player2 = list(player2_pokemon.keys())[list(player2_pokemon.values()).index(pokemon_picked_object_player2)]
    print("You Picked: " + pokemon_picked_object_player2.name)

    while True:

        turn = 0

        #player1 attacks

        if turn == 0:
            print("""

                Player 1, go first!

                """)

            print("Available moves: \n" + "1 " + str(pokemon_picked_object_player1.small_attack) + " \n" +"2 "+str(pokemon_picked_object_player1.large_attack))

            player1_picked_move = input("""
                Pick your attack!:
                """)

            if player1_picked_move == "1":
                print(f"""Player1 attacked with {pokemon_picked_object_player1.small_attack}!
                    """)
            elif player1_picked_move == "2":
                print(f"""Player 1 attacked with {pokemon_picked_object_player1.large_attack}!
                    """)
            else: print("somthing went wrong")

            dodge_hit = random.randrange(1,5)

            if player1_picked_move == "1":
                if dodge_hit % 2 != 0:
                    old_damage_Player2 = int(pokemon_picked_object_player2.health)
                    pokemon_picked_object_player2.health -= random.randrange(1,pokemon_picked_object_player1.small_attack_damage)
                    new_damage_Player2 = int(pokemon_picked_object_player2.health)
                    print(f"""{pokemon_picked_object_player2.name} took {old_damage_Player2 - new_damage_Player2} damage!
                        """)
                    if pokemon_picked_object_player2.health < 0:
                        print(f"""{pokemon_picked_object_player2.name} now has {int(pokemon_picked_object_player2.health)} health left!
                        """)
                    else:
                        pass
                    turn += 1
                else:
                    print(f"""{pokemon_picked_object_player2.name} Dodged the attack!
                        """)
                    turn += 1

            if player1_picked_move == "2":
                if dodge_hit % 2 != 0:
                    old_damage_Player2 = int(pokemon_picked_object_player2.health)
                    pokemon_picked_object_player2.health -= random.randrange(1,pokemon_picked_object_player1.large_attack_damage)
                    new_damage_Player2 = int(pokemon_picked_object_player2.health)
                    print(f"""{pokemon_picked_object_player2.name} took {old_damage_Player2 - new_damage_Player2} damage!
                        """)
                    if pokemon_picked_object_player1.health < 0:
                        print(f"""{pokemon_picked_object_player2.name} now has {int(pokemon_picked_object_player2.health)} health left!
                        """)
                    else:
                        pass
                    turn += 1
                else:

                    print(f"""{pokemon_picked_object_player2.name} Dodged the attack!
                        """)
                    turn += 1

            # player2 attacks
            print("""Player2, Choose your move!
                """)

            print("Available moves: \n" + "1 " + str(pokemon_picked_object_player2.small_attack) + " \n" +"2 "+str(pokemon_picked_object_player2.large_attack))

            player2_picked_move = input("""
                Pick your attack!:
                    """)

            if player2_picked_move == "1":
                print(f"""Player 2 attacked with {pokemon_picked_object_player2.small_attack}!
                    """)
                old_damage_Player1 = int(pokemon_picked_object_player1.health)
                pokemon_picked_object_player1.health -= random.randrange(1,pokemon_picked_object_player1.small_attack_damage)
                new_damage_Player1 = int(pokemon_picked_object_player1.health)
                print(f"""{pokemon_picked_object_player1.name} took {old_damage_Player1 - new_damage_Player1} damage!
                    """)
                print(f"""{pokemon_picked_object_player1.name} now has {int(pokemon_picked_object_player1.health)} health left!
                """)
                turn -= 1
            elif player2_picked_move == "2":
                print(f"""Player 2 attacked with {pokemon_picked_object_player2.large_attack}!
                    """)
                print(f"""Player 2 attacked with {pokemon_picked_object_player2.large_attack}!
                    """)
                old_damage_Player1 = int(pokemon_picked_object_player1.health)
                pokemon_picked_object_player1.health -= random.randrange(1,pokemon_picked_object_player1.large_attack_damage)
                new_damage_Player1 = int(pokemon_picked_object_player1.health)
                print(f"""{pokemon_picked_object_player1.name} took {old_damage_Player1 - new_damage_Player1} damage!
                    """)
                print(f"""{pokemon_picked_object_player1.name} now has {int(pokemon_picked_object_player1.health)} health left!
                """)
                turn -= 1
            else: print("put in a real value.")

            if pokemon_picked_object_player1.health <= 0:
                print("""
                    _______  ___      _______  __   __  _______  ______     _______    _     _  _______  __    _  __
                   |       ||   |    |   _   ||  | |  ||       ||    _ |   |       |  | | _ | ||       ||  |  | ||  |
                   |    _  ||   |    |  |_|  ||  |_|  ||    ___||   | ||   |____   |  | || || ||   _   ||   |_| ||  |
                   |   |_| ||   |    |       ||       ||   |___ |   |_||_   ____|  |  |       ||  | |  ||       ||  |
                   |    ___||   |___ |       ||_     _||    ___||    __  | | ______|  |       ||  |_|  ||  _    ||__|
                   |   |    |       ||   _   |  |   |  |   |___ |   |  | | | |_____   |   _   ||       || | |   | __
                   |___|    |_______||__| |__|  |___|  |_______||___|  |_| |_______|  |__| |__||_______||_|  |__||__|
                   """)
                break

            if pokemon_picked_object_player2.health <= 0:
                print("""
                    _______  ___      _______  __   __  _______  ______     ____     _     _  _______  __    _  __
                   |       ||   |    |   _   ||  | |  ||       ||    _ |   |    |   | | _ | ||       ||  |  | ||  |
                   |    _  ||   |    |  |_|  ||  |_|  ||    ___||   | ||    |   |   | || || ||   _   ||   |_| ||  |
                   |   |_| ||   |    |       ||       ||   |___ |   |_||_   |   |   |       ||  | |  ||       ||  |
                   |    ___||   |___ |       ||_     _||    ___||    __  |  |   |   |       ||  |_|  ||  _    ||__|
                   |   |    |       ||   _   |  |   |  |   |___ |   |  | |  |   |   |   _   ||       || | |   | __
                   |___|    |_______||__| |__|  |___|  |_______||___|  |_|  |___|   |__| |__||_______||_|  |__||__|
                   """)
                break



game(1)

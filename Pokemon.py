#Amelie Lynde
#11/21/24
#Pokemon Evolution

#Init
import random
pokemon_level = 0 #Global
pokemon_name = "Snorlax"
day = 1
#Functions
def evolve_pokemon():
    global pokemon_name
    global pokemon_level
    if pokemon_level >= 10:
        print("You have evolved!")
        print("Your new name is Munchlax")
        pokemon_name = "Munchlax"
    if pokemon_level >= 20:
        print("You have evolved!")
        print("Your new name is Skylax")
        pokemon_name = "Skylax"

def train():
    global day
    global pokemon_level
    print("You did 20 pushups")
    print("Your level increased by one!")
    pokemon_level = pokemon_level + 1
    print("Your pokemon level is ", pokemon_level)
    day = day + 1

def gym_battle():
    global day
    global pokemon_level
    outcome = random.randint(1,2) #50% chance to win or lose
    if outcome == 1:
        print("You are up againt Charizard!")
        print("You won! Your level increased by 2. Your level is...")
        pokemon_level = pokemon_level + 2
        print(pokemon_level)
    else:
        print("You are up against Squirtly!")
        print("You lost! Your level did not increase. Your level is...")
        print(pokemon_level)
    day = day + 1

def rest():
    global day
    global pokemon_level
    print("Your pokemon is ", pokemon_name)
    print("Your pokemon level is ", pokemon_level)

#Main
print("Welcome to Pokemon Evolution")
while True:
    print("Select an activity for Day: " + str(day)) #Increases day by 1 after every event
    print("""1.Train
2.Gym Battle
3.Rest(Display info)
4.Quit""")
    activity = int(input("(1-4) Activity for the day: "))
    if activity == 1: #True
        train()
        evolve_pokemon()
    elif activity == 2:
        gym_battle()
        evolve_pokemon()
    elif activity == 3:
        rest()
    elif activity == 4:
        break

from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
    greedy = False
    
    while True:
        choice = int(input('> '))
    
        if choice < 50:
            print("Nice, you're not greedy, you win!")
            exit(0)
# extra change for the greedy people - level: Novice    
        elif choice > 50 and novice_player: # novice_player not defined error. Why? 
            print("Don't bee greedy. Try again.")
            greedy = True

        else:
            dead("You greedy bastard!")
        
def bear_room():
    print("There is a bear here.")
    print("The bear has a bunch of honey.")
    print("The fat bear is in front of another door.")
    print("How are you going to move the bear?")
    bear_moved = False
    
    while True:
        choice = input("> ")
    
        if choice == "take honey":
            dead("The bear looks at you then slaps your face off.")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off.")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means.")
        
        
def cthulhu_room():
    print("Here you see the great evil Cthulhu.")
    print("He, it, whatever stares at you and you go insane.")
    print("Do you flee for your life or eat your head?")
    
    choice = input("> ")
    
    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()
        
        
def dead(why):
    print(why, "Good job!")
    exit(0)
    
def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Which one do you take?")
    
    choice = input('> ')
    
    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")
       
def start1():
    print("Are you a novice or an expert player?")
    novice_player = False
    
    player_type = input('> ')
    
    if player_type == "novice":
        print("You are a novice player.")
        novice_player = True 
        start()
    
    else:
#        print("You've got balls! You are an expert player!")
        start()
        
start1()

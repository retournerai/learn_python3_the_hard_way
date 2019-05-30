from sys import exit # use exit attribute (function) in the import module from python sys package

def gold_room(): # function name parameter
    print("This room is full of gold. How much do you take?") # show text message
    
    choice = input('> ') # variable = user input prompt
    if "0" in choice or "1" in choice: # if-statement is '0' in variable (choice) or 1 then
        # variable = integrer (choice 1 or 2). 'int' tells Python it can be processed as an integrer number
        how_much = int(choice) 
    else: # if-statement is other than '0' or '1' (2 till 9...why????) then
        dead("Man, learn to type a number.") # call dead function and show text message
        
    if how_much < 50: # if-statement name parameter number (smaller than 50)
        print("Nice, you're not greedy, you win!") # show text message
        exit(0) # good normal exit without errors.
    else: # if-statement is other than '< 50' then
        dead("You greedy bastard!") # call dead function and show text message
        
        
def bear_room(): # function name (parameter)
    print("There is a bear here.") # show text message
    print("The bear has a bunch of honey.") # show text message
    print("The fat bear is in front of another door.") # show text message
    print("How are you going to move the bear?") # show text message
    bear_moved = False # variable = False
    
    while True: # infinitive loop   
        choice = input("> ") # variable = user input prompt
    
        if choice == "take honey": # if-statement variable prompt input (choice) = equal to 'take honey' then...
            dead("The bear looks at you then slaps your face off.") # call dead function and show text message
        # else-if statement variable prompt input (choice) = equal to 'taunt bear' and bear_moved = not 'True' then...
        elif choice == "taunt bear" and not bear_moved: # PAY ATTENTION TO 'and not'
            print("The bear has moved from the door.") # show text message
            print("You can go through it now.") # show text message
            bear_moved = True # variable = changed from 'False' to 'True'
        elif choice == "taunt bear" and bear_moved: # else if 'choice' prompt was 'taunt bear' AND bear_moved is 'True' then 
            dead("The bear gets pissed off and chews your leg off.") # call 'dead' function and show text message 
        elif choice == "open door" and bear_moved: # else if choice prompt was "door open" AND bear_moved = 'True' then
            gold_room() # call 'gold_room' function
        else: # if-statement is other than 'Open door', 'taunt bear', 'take money' then
            print("I got no idea what that means.") # show text message
        
        
def cthulhu_room(): # function name (parameter)
    print("Here you see the great evil Cthulhu.") # show text message
    print("He, it, whatever stares at you and you go insane.") # show text message
    print("Do you flee for your life or eat your head?") # show text message
    
    choice = input("> ") # variable = user input prompt
    
    if "flee" in choice: # if-statement in prompt input ('choice') = equal to 'flee' then...
        start() # call start function. It basically re-starts the script from zero. 
    elif "head" in choice: # else-if statement in prompt input (choice) = equal to 'head' then...
        dead("Well that was tasty!") # call 'dead' function and show text message
    else: # if-statement is other than 'flee' or 'head' then
        cthulhu_room() # call 'cthulhu_room' function
        
        
def dead(why): # function name (parameter)
    print(why, "Good job!") # show argument ('why') followed by message
    exit(0) # good normal exit without errors.

   
def start(): # function name (parameters none): 
    print("You are in a dark room.") # show text message
    print("There is a door to your right and left.") # show text message
    print("Which one do you take?") # show text message
    
    choice = input('> ') # variable = user input prompt
    
    if choice == "left": # if-statement is equal to 'left' prompt entry then
        bear_room() # call bear_room function
    elif choice == "right": # if-statement is equal to 'right' prompt entry then
        cthulhu_room() # call cthulhu_room function
    else: # if-statement is other than 'left' or 'right' then
        dead("You stumble around the room until you starve.") # call dead function and show text message
        
# call 'start function'        
start()

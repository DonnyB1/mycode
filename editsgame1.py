#!/usr/bin/env python3

import rooms from mhmm.py 

def showInstructions():
    
    """Show the game instructions when called"""
    #print a main menu and the commands
    print1by1('''
    The BACkBACK BACK BACKK ROOms
   
    ========
    
    How'd you get here? No worries there's no simple way out but you can escape
    unlessss....you run into trouble? KEEEKW
    ========
    
    Make it through or get folded, whichever comes first
    Commands:
      map [see "The Map"]
      go  [North, South, East, West]
      use [item in inventory]
      get [item]
    ''')
def showStatus():
    """determine the current status of the player"""
    #print the player's current status
    print('---------------------------')
    print(f"The {Character_name}" ' is in the ' + currentRoom)
    #print the current inventory
    print('Inventory : ' + str(inventory))
    #print an item if there is one
    if "item" in rooms[currentRoom]:
        print('You see a ' + rooms[currentRoom]['item'])
        print("---------------------------")

#an inventory, which should be empty
inventory = []


rooms = {
            'Office' : {
                  'North' : ["You went north and entered room 3, Now why the hell does this feel like Deja Vu? As you begin to question so much you notice an indented spot on the wall with a strange symbol"],
                  'South' : ["You've gone south and entered Room2, the intense sound of the lights flickering...and flickering....aAAAgggh",
                  'East'  : ["You went east and entered Room 1, Why does everything look the same? Yellow carpeted interior, striped pattern on the walls, even the room entrances are all evenily highted"],
                  'West'  : ["You went west and entered room 4, all you see is more of the same thing, you begin to think your going MADDDD,....oh hey is that something in the corner?]
                  'Item'  : ["A Key with a Stramge symbol on it"]        
                },

            'Corridor' : {
                  'North' : ["You entered the north Hall, your vision weakened by thick fog you begin to question your sanity you think you begin to hear footsteps approaching"]
                  'South' : ["You entered the south Hall, same as before yet the air has gotten thicker? You smell a foul odor but dare not search for the owner"],
                  'East'  : ["You entered the west Exit 2, In front you see a big exit with the number 2 on it, Can you trust this one? How is this one....is this one even different?"],
                  'West'  : ["You entered the east exit 1, In front you see a big exit with the number 1 on it, Can you trust it, is it that simple?"],
                  'Bouncing Betty'   : ["Bouncing Betty", "You stepped on a bouncing betty darn ya gotta be quicker then that"],
                  'Claymore'   : ["You tripped a claymore, hey its not his fault you walked in his line of fire."]
            },
            'Factory' : {
                  'North' : ['You went north and entered the top floor, you see a way down...do you take it?'],
                  'South' : ['You entered the south entrance of the factory, you see a portal do you dare?],
                  'East'  : ["You went east and entered the Indoor Forest, A indoor forrest, maybe you have gone too far maybe not"],
                  'West'  : ["You went west but got caught by a spell, something something...darksiddeee this repeats over and over in your head, what a fitting end."],
                             
               },
            'Indoor Forest'  :  {
                  'North' : ["You arrived t the North, Ah look a treasure chest seems legit, but can you really trust it you begin to way your options."]"
                  'South' : ["You went south and ran into a monster with a name tag BakBrekr, speciality in fixing baks...free of charge."],
                  'East' : ["You arrived in the East entrance after traversing the twisted path, you see a ominous portal, do you dare?"] ,
                  'West' : ["You went west and entered a reverse forest, stuck in a enteranl loop maybe you shouldn't have cosplayed scooby doo."],
                  'Item' : ["Red Pill, leads to early death why would you eat something random?"]
                           
            }
            
         }

A=Yes
B=No

def instructions():
    player movement
#Base movement inputs for player    
currentroom == #Rooms Directory
move == move = ''
  while move == '':
    move = input('>')
if move[] in #current area = [currentroom] 

#delete item after picking up
# if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')
      #delete the item from the room
      del rooms[currentRoom]['item']
      
while True:
    showStatus()

    #get the player's next 'move'
    move = ''
    while move == '':  
        move = input('>')

    # split allows an items to have a space on them
    # get fien spray is returned ["get", "fien spray"]          
    move = move.lower().split(" ", 1)
    
    # shows the map when called
    if move[0] == 'map':
        
        
        #Tech issue with the map loading
        
        
 #if 'go' is typed first
    if move[0] == 'go':
        #checks that they are allowed wherever they want to go
        if move[1] in rooms[currentRoom]:
            #set the current room to the new room
            currentRoom = rooms[currentRoom][move[1]]
        #there is no door (link) to the new room #curtesy of Tyler
        else:
            print('You can\'t go that way!')

    #if they type 'get' first
    if move[0] == 'get' :
        #if the room contains an item, and the item is the one they want to get
        if "item" in rooms[currentRoom] and move[1].upper() in rooms[currentRoom]['item'].upper():
            #add the item to their inventory
            inventory += [move[1]]
            #display a helpful message
            print(move[1] + ' has been found!')
            #delete the item from the room
            del rooms[currentRoom]['item']
        #otherwise, if the item isn't there to get
        else:
            #tell them they can't get it
            print('Can\'t get ' + move[1] + '!')
            
            
if move[0] == "use":
        if "Key" in inventory and currentRoom == "Office" and move[1] == "key":
            print("You use the key with the wierd insignia, dang what are the odds this actually work\n")
            print("You've found the get outta jail free card, nah fr you found a way out take it this place is CRAzzzzy")
            #player win condition 1
            rooms["Office"]["South"]= "Room2"
            inventory.remove("Key")
            
if move[0] == "Use":
        if "fien off spray" in inventory and currentRoom == "" and move[1] == "fien off spray":
            print1by1("You use fien spray darn this really does work!\n")
            rooms[""][""]= "Factory
            inventory.remove("fien off spray")
            
            
#help command prompt
else:
print("For a full list of commands type [help]")
Command = input()
if Command.lower() == "help":
    print('help - Current Available Commands')
    print('n,s,e,w - moves in that direction')
    print('inv - Opens and checks your current inventory')
    print('map - Prints current location on map')
    print('Other words like [crouch][use][Yes][No] can be used throughout the game, try when given to see if they work!'

print("You've awoken in a mysterious place, you can sit around and waste, or find a way out")
print("You are carrying, nothing current ya bum") 
    #player movement based of input of n, s, e, w
    while Location == "Office":
    if Command.lower() == "n":
        print("You went north and entered room 3, Now why the hell does this feel like Deja Vu? As you begin to question so much you notice an indented spot on the wall with a strange symbol")
        Location = "Office"
    elif Command.lower() == "s":
        print("You've gone south and entered Room2, the intense sound of the lights flickering...and flickering....aAAAgggh")
        Location = "Office"
        elif Command.lower() == "e":
        print("You went east entering Room 1, Why does everything look the same? Yellow carpeted interior, striped pattern on the walls, even the room entrances are evenily highted")
        Location = "Office"
    elif Command.lower() == "w":
        print("You went west and entered room 4,  you see more of the same thing, you begin to think your going MADDDD.")
        Location = "Office"
        #transitions to next room
    else Command.lower() == "w"
        print("you entered the Corridor")
        Location = "Corridor"
    
while Location == "Corridor":
    Command = input()
    if Command.lower() == "n":
        print("You entered the north Hall, your vision weakened by thick fog you begin to question your sanity you think you begin to hear footsteps approaching.")
        Location = "Corridor"
    elif Command.lower() == "s":
        print("You entered the south Hall, same as before yet the air has gotten thicker? You smell a foul odor but dare not search for the owner")
        Location = "Corridor"
    elif Command.lower() == "e":
        print("You entered the west Exit 2, In front you see a big exit with the number 2 on it, Can you trust this one? How is this one....is this one even different?"")
        if yes input(print("Alas you fell for the oldest trick in the book HAAAA, you died btw")) #if yes death if no continue
        if no continue
        Location = "Corridor"
        #transitions to next room
    elif Command.lower() == "w":
        print("You entered the east exit 1, In front you see a big exit with the number 1 on it, Can you trust it, is it that simple?)
        if yes input ("You found a path to the factory nj!")#if yes switch to next room if no 
        Location = "Corridor"
        
while Location == "Factory":
    Command = input()
    if Command.lower() == "n":
        print("You went north and entered the top floor, you see a way down...do you take it?")
        if yes input(print("Just because you saw a way down didnt mean it was right, you fell to your death kekw.")
        if no continue#if yes player death if no continue
        Location = "Factory"
    elif Command.lower() == "s":
        print("You entered the south entrance of the factory, you see a portal do you dare?")
        if yes input(print("a hand reached from the portal and snatched you up WOOOOOOOOOO fun ride but your likely not coming back so gg")
        if no continue #if yes player death if no continue
        Location = "Factory"
    elif Command.lower() == "e":
        print("You went east and entered the Indoor Forest, A indoor forrest, maybe you have gone too far maybe not.")
        Location = "Indoor Forest"
    elif Command.lower() == "w":
        print("You went west and got caught in a illusion, something something...darksiddeee, this repeats over and over in your head, what a fitting end."")
        Location = "Factory"
        
while Location == "Indoor Forrest":
    Command = input()
    if Command.lower() == "n":
        print("You arrived to the North, Ah look a treasure chest seems legit, but can you really trust it you begin to way your options.")
        if yes input(print("ha i knew we'd get someone with that, congrats you fed the mimic.")
        if no continue#if yes player death from monster mimic if no continue
        Location = "Indoor Forrest"
    elif Command.lower() == "s":
        print("You went south and ran into a monster with a name tag BakBrekr, speciality in fixing baks...free of charge.")
        #if going this location results in players death automatically
        Location = "Factory"
    elif Command.lower() == "w":
        print("You arrived in the west entrance after traversing a twisted path, you see a ominous portal, do you dare?")
        if yes input(print("Wow you actually got out, you really dont know how lucky you are.")
        if no continue#if yes players escapes and wins if no continue
        Location = "Indoor Forest"
    elif Command.lower() == "e":
        print("You went east and entered a reverse forest, stuck in a enteranl loop maybe you shouldn't have cosplayed scooby doo."")
        Location = "Factory"
        
        
        break
        

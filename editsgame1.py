#!/usr/bin/env python3
#!/usr/bin/env python3

import rooms from mhmm.py
import map from gamemap.py


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
        #if yes death if no continue
        Location = "Corridor"
        #transitions to next room
    elif Command.lower() == "w":
        print("You entered the east exit 1, In front you see a big exit with the number 1 on it, Can you trust it, is it that simple?)
        #if yes switch to next room if no
        Location = "Corridor"

while Location == "Factory":
    Command = input()
    if Command.lower() == "n":
        print("You went north and entered the top floor, you see a way down...do you take it?")
        #if yes player death if no continue
        Location = "Factory"
    elif Command.lower() == "s":
        print("You entered the south entrance of the factory, you see a portal do you dare?")
        #if yes player death if no continue
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
        #if yes player death from monster mimic if no continue
        Location = "Indoor Forrest"
    elif Command.lower() == "s":
        print("You went south and ran into a monster with a name tag BakBrekr, speciality in fixing baks...free of charge.")
        #if going this location results in players death automatically
        Location = "Factory"
    elif Command.lower() == "w":
        print("You arrived in the west entrance after traversing a twisted path, you see a ominous portal, do you dare?")
        #if yes players escapes and wins if no continue
        Location = "Indoor Forest"
    elif Command.lower() == "e":
        print("You went east and entered a reverse forest, stuck in a enteranl loop maybe you shouldn't have cosplayed scooby doo."")
        Location = "Factory"


        break

#!/usr/bin/python3

#lows tryto make somehtin close to a backroom

#have character go through areas looking for items to get out or help get out

#think of potential used words phrases, you can have that if typed quick enough coudl protect you from threats.

#see if you could have a script that would give the player a warning if "something" slipped unto the room/area

#give the player description letting them know of maybe somethings coming?

#see if itll be fun or not to randomize the monster(s). Ex: when the player moves the mosnter coudl randomly spawn in the room u go to instead of it being in disignated areas.

#something soemthing somehting

#ahh i have to writ e script and draw now i forgot :(

#think of potential areas, places, names, events, maybe puzzles or something to do 

#rough draft up on paper so it sounds right first


#idead stick up here^

#code starts down here V
#dont forget to add comments, forgot last time kekw




#!/usr/bin/python3
#REMEMBER TO CD AND SAVE TO THE CORRECT DIRECTROY, STOP PRESSING RANDOM BUTTONS AGAIN WE CANT AFFORD TO KEEP LOSING THIS DATA AND STARTING OVER!!!!!

# Replace RPG starter project with this code when new instructions are live

def showInstructions():
  #print a main menu and the commands
  print('''
Backrooms JAme
  go [direction]
  get [item]
''')

  #Monster/Antagonist-
  #Rooms, Areas-Base room(the continued office light noise, carpted, random moist floors

print('---------------------------')

print('You are in the ' + currentRoom)

#print the current inventory
print('Inventory : ' + str(inventory))

#print an item if there is one
if "item" in rooms[currentRoom]:
    print('You see a ' + rooms[currentRoom]['item'])
    print("---------------------------")
#hmm, look up 2 ways to switch this up if its gonna be based more off decision versus like a rpg dont think much iventory would be needed

#an inventory
inventory = []

rooms = {

             'Office' : {
                  'south' : 'Room2',
                  'east'  : 'Room1',
                  'item'  : 'key',
                  'north' : 'Room3',
                  'west'  : 'Room4',
                  'item'  : 'secret get back FIEN spray',
                  'trap'  : 'broken glass',
                  'item'  : '',
                  'riddle': '',
                },

            'Corridor' : {
                  'north' : 'Hall',
                  'south' : 'Hall2',
                  'east'  : 'Exit 1',
                  'west'  : 'Exit 2',
                  'item'  : 'Mr.Helpalot',
                  'item'  : 'stank stinky mask',
                  'item'  : 'smell good spary',
                  'trap'  : 'shark pit',
                  'trap'  : 'claymore',
                },
            'Factory' : {
                  'north' : 'Top floor room',
                  'south' : 'Something something',
                  'east'  : 'Indoor Forest',
                  'west'  : 'Outdoor Forest',
                  'item'  : 'feel good potion',
                  'item'  : 'Proposteriouly goodlookin cloak',
                  'trap'  : 'bouncing betty',
                  'riddle': '',
               },
            'Indoor Forest' : {
                  'north' : 'treasure chest??'
                  'south' : 'monster bakBrekr',
                  'east'  : 'twisted path',
                  'west'  : 'portal of nothing',
                  'item'  : 'red pill??',

               },
            'Reverse Forest' : {
                  'north' : 'River',
                  'south' : 'Door 1.2',
                  'east'  : 'Door 1',
                  'west'  : 'Upstairs path downstairs',
                  'item'  : 'green pill',
                  'item' : 'cookie?',
            }
         }

#start the player in the Hall
currentRoom = 'Hall'


#You coudl randomize the starting point but you might have to rework the 'areas' because spawing into complete darkness or wate... welll gg


showInstructions()

#loop forever
while True:

  move = ''
  while move == '':
    move = input('')

  # Lowercase answer
  move = move.lower().split(" ", 1)

if room equal


  #if they type 'go' first
  if move[0] == 'go':
    #check that they are allowed wherever they want to go
    if move[1] in rooms[currentRoom]:
      #set the current room to the new room
      currentRoom = rooms[currentRoom][move[1]]
    #there is no door (link) to the new room
    else:
        print('No silly, that way be nothing')
#Maybe add some light humor, notable references
  #if they type 'get' first
  if move[0] == 'get' :
      else:
          print('it together player or else ill do it for ya')
    #if the room contains an item, and the item is the one they want to get
    if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
      #add the item to their inventory
      inventory += [move[1]]
      #display a helpful message
      print(move[1] + ' got!')

      #delete the item from the room
      del rooms[currentRoom]['item']
    #otherwise, if the item isn't there to get
    else:
      #can't get it
      print('Can\'t get ' + move[1] + '!')
#See that stuff looks to messy and extra

#thx to code master chad  use this f- string   (print(f"{variableA} and {variableB}")
#Could win by maybe solving certain riddles/puzzles, or escaping through certain zones, or finding maybe a super secret escape room
  ## Define how a player can win

  if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
    print('You escaped the house... YOU WIN!')
  break

#NOw this lol add some wording to make the player tense on purpose to make them run out of time
#maybe have monsters give random phrase u have to mimic bak or elsssssse

  ## If a player enters a room with a monster
  elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
    print('A monster has got you... GAME OVER!')
    break










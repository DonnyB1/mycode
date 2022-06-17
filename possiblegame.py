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


  #Monster/Antagonist-
  #Rooms, Areas-Base room(the continued office light noise, carpted, random moist floors

#an inventory
inventory = []

rooms = {
#Area locations, add a map?

#Character Health has sanity
#Too many (2) encounters with monster without correct way to hide/"fight" off monsters = death

             'Office' : {
                 'south' : 'Room2',"desc:("You've gone south and entered Room2, "the intense sound of the lights flickering...and flickering....aAAAgggh")
                  'east'  : 'Room1',"desc:("You've gone east and entered Room 1, "Why does everything look the same?? Yellow, carpeted interior, striped pattern on the walls, even the room entrances are all evenily highted"
#Key item to advancee to next room
                  'item'  : 'key',"desc:("You've found a key; "I wonder what it for, it has a funny insignia on it"
                  'north' : 'Room3',"desc;(You went north and entered room 3, "Now why the hell does this feel like Deja Vu? As you begin to question so much you notice an indented spot on the wall with a strange symbol"
                  'west'  : 'Room4',"desc:(You went west and entered room 4, all you see is more of the same thing, you begin to think your going MADDDD,....oh hey is that something in the corner?)

#Item needed to save the character from a potential encounter with monster
                  'item'  : 'secret get back FIEN spray', "desc:"I mean it speaks for itself. Directions say to make sure you aim the right way or you'll spray yourself duhhh."
                  'trap'  : 'broken glass',"You didnt watch your step and you stepped on some broken glass. Maybe let whatever could be around know your ever move right? Why dont you bang on the wall next?" "You stepped on more broken glass, I guess your not good at the game of picking your feet up""You stepped on more broken glass, too many times and you'll meet a early end""You stepped on glass, you feel light headed lol, told you watch your step. As you begin losing strength, you wonder "Maybe I shouldve watched my step" too late kekw."
                  'item'  : '',
                  'text': 'If you want to become so much more, all you have to do is explore. What awiats you in these halls? Hard to say, depends on which numbe you are by the time you see this. Is this a Helpful hint, or is this someone leading you to the end? Hmmmmmmmmmmmmmmmm....dont think you got many options :)',
                },

            'Corridor' : {
                  'north' : 'Hall',"desc:"You entered the north Hall, your vision is weakened by thick fog you begin to question your sanity as you think you begin to hear footsteps approaching"
                  'south' : 'Hall2',"desc:"you entered the south Hall, same as before yet the air has gotten thicker? You smell a foul odor but dare not search for the owner"
                  'east'  : 'Exit 1',"desc:"you entered the east exit 1, In front you see a big exit with the number 1 on it, "Can you trust it, is it that simple? #leads to hall with left or right way. either leads player to death.
                  'west'  : 'Exit 2',"desc:"you entered the west Exit 2, In front you see a nig exit with the number 2 on it, "Can you trust this one? How is this one....is this one even different?" #correct exit to leave to next area"
                  'item'  : 'Mr.Helpalot',"desc:Remains docile if you take mask""Becomes agro if you dont, will ask you a riddle that if answered wrong = players death. Answered right = player earns "stank stinky mask".
                  'item'  : 'stank stinky mask',"desc:A mask found on a skeleton with an id reading "Mr.Helpalot" (item can disguise player from a monster encounter once"
                  'item'  : 'smell good spary',"desc:If used by player attracts monster to it = death""It says smell good but that didnt mean use it lol"
                  'trap'  : 'shark pit',"you fell into a pit of water, well you can assume what comes next...you see 2 big sharks approaching at fast speed...the end is near"
                  'trap'  : 'claymore',"you tripped a claymore...should learn to watch your step goober"
                },
            'Factory' : {
                  'north' : 'Top floor room',"You went north and entered the top floor, you see a way down...do you take it? # taking way out leads to player death
                  'south' : 'Something something',"You went south and got caught in a spell, "something something...darksiddeee" this repeats over and over in your head, what a fitting end.
                  'east'  : 'Indoor Forest',"You went east and entered the Indoor Forest""A indoor forrest, maybe you have gone too far maybe not"
                  'west'  : 'Reverse Forest',"You went west and entered the Reverse Forest""Everything feels upside down, everythign is moving funny...I think im gonna be sick"
                  'item'  : 'feel good potion',"does nothing but make you feeel good...mentally"
                  'item'  : 'Proposteriouly goodlookin cloak',"what better to wear than something that can help ya not be noticed...sign me UP COaCH"
                  'trap'  : 'bouncing betty',"You stepped on a bouncing betty" "If you move...BOOOM ha now why'd you think you were faster than me lol""if player types crouch "you crouch and avoid the explosion...i knew all that COD would pay off.
                  'riddle': '',
               },
            'Indoor Forest' : {
                  'north' : 'treasure chest??'"It reads treasure chest and look it, but can you really trust it?"if player takes treasure chest player killed by monster = mimic"
                  'south' : 'monster bakBrekr',"Monster with a speciality in fixing your back...free of charge"
                  'east'  : 'twisted path',"You went south and entered a twisted path...caught in the loop your stuck here forever."
                  'west'  : 'portal of nothing',"You head west and see a Portal, but where does it go? Only 1 way to find out".#lets the player teleport to area of choice"
                  'item'  : 'red pill??',"If taken/eaten leads to players death."

               },
            'Reverse Forest' : {
                  'north' : 'River',"You go north and see a river, strange yoou dont recall hearing water before. # if entered player is stuck
                  'south' : 'Door 1.2',"Simple exit for the player to win if player has correct items"
                  'east'  : 'Door 1',"leads player back to first area"
                  'west'  : 'Upstairs path downstairs',"Leads players into loop on stairs"
                  'item'  : 'green pill',"Actually a monster that kills player, very cheeeky"
                  'item' : 'cookie?',"A cookie for your thoughts..wink wink. Helps players sanity if attacked by monster.
                           }
         }


#You coudl randomize the starting point but you might have to rework the 'areas' because spawing into complete darkness or wate... welll gg


showInstructions()


#thx to code master chad  use this f- string   (print(f"{variableA} and {variableB}")
#Could win by maybe solving certain riddles/puzzles, or escaping through certain zones, or finding maybe a super secret escape room


#NOw this lol add some wording to make the player tense on purpose to make them run out of time
#maybe have monsters give random phrase u have to mimic bak or elsssssse










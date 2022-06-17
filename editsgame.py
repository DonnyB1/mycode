""" This is the main file, it contains the functions for the rooms as well as the startup sequences."""
#!/usr/bin/env python3


import actions
import room_info as rooms
import character_and_items as char

"""TODO LIST:
-Implement save features(Save module?)
-Add some spunk into the descriptions, make it fun yet concise!!
"""

# output
def print_frog_title():
    print("   ____                ___     __              __              ")
    print("  / __/______  ___ _  / _ |___/ /  _____ ___  / /___ _________ ")
    print(" / _// __/ _ \/ _ `/ / __ / _  / |/ / -_) _ \/ __/ // / __/ -_)")
    print("/_/ /_/  \___/\_, / /_/ |_\_,_/|___/\__/_//_/\__/\_,_/_/  \__/ ")
    print("             /___/                                             ")

# input
def check_start():
    print_frog_title()
    print("                 A game by Mopi Productions ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    print("For a list of commands type 'h', 'help', or '?'")


def load_room(room):
    char.current_room = room
    room_dict = {
        "burrow": burrow,
        "burrow_basement": burrow_basement,
        "front_of_house": front_of_house
    }
    func = room_dict.get(room, lambda: "ERROR")  # To be quite frank I don't really understand lambda: ERROR yet
    func()


def burrow():
    print("You are in your burrow. The front door is to the north.")
    while True:
        action = actions.get_action(rooms.burrow)
        if action[0] == "mopi":
            load_room(action[1])
        if action == "down":
            if rooms.burrow.variables["trapdoor_opened"] and "lantern" in char.character_inventory:
                load_room("burrow_basement")
                break
            elif not rooms.burrow.variables["rug_moved"]:
                print("You cant go that way!")
            elif rooms.burrow.variables["rug_moved"] and not rooms.burrow.variables["trapdoor_opened"]:
                print("The trapdoor is shut.")
            elif "lantern" not in char.character_inventory:
                print("It's far too dark down there, you should stay up here until you find a light source.")
        elif action == "north":
            if rooms.burrow.variables["door_unlocked"]:
                load_room("front_of_house")
            else:
                print("The front door is locked!")
        elif action in rooms.directions:
            print("You cant go that way!")
        elif action[0] == "examine":
            if action[1] in ("rug", "carpet", "lump"):
                if not rooms.burrow.variables["rug_moved"]:
                    print("Upon further examination, the 'lump' appears to be handle shaped. You should try moving "
                          "the rug.")
                else:
                    print("Your beloved family heirloom has been rudely shoved against a wall. What would Aunt Frogatha think?")
            elif action[1] == "door":
                print("Your door is locked. You'd unlock it, but you've lost the key.")
            elif action[1] == "cabinet":
                if rooms.burrow.variables["cabinet_opened"]:
                    if rooms.burrow.variables["jar_taken"]:
                        print("It's an open cabinet with barren shelves.")
                    else:
                        print("It's an open cabinet with barren shelves excepting a single empty jar.")
                else:
                    print("It's a closed cabinet where you keep your dishware.")
        elif action[0] == "move":
            if action[1] in ("rug", "carpet"):
                if not rooms.burrow.variables["rug_moved"]:
                    print("You moved the rug, and underneath you found a trapdoor! This isn't a new discovery.")
                    rooms.burrow.variables["rug_moved"] = True
                else:
                    print("You've already kicked the rug into the corner! Better to not do any more damage.")
        elif action[0] == "use":
            if action[1] == "trapdoor" and rooms.burrow.variables["rug_moved"]:
                print("You opened the trapdoor.")
                rooms.burrow.variables["trapdoor_opened"] = True
            elif action[1] == "door":
                if not rooms.burrow.variables["door_unlocked"] and "key" not in char.character_inventory:
                    print("The door is locked, and you seem to have misplaced your key.")
                elif not rooms.burrow.variables["door_unlocked"] and "key" in char.character_inventory:
                    print("The door is locked, you should using your key.")
                else:
                    load_room("burrow_basement")
                    break
        elif action[0] == "open":
            if action[1] == "trapdoor" and rooms.burrow.variables["rug_moved"]:
                print("You opened the trapdoor.")
                rooms.burrow.variables["trapdoor_opened"] = True
            elif action[1] == "door":
                if not rooms.burrow.variables["door_unlocked"] and "key" in char.character_inventory:
                    print("You unlocked the front door! Welcome to the outside ")
                elif "key" not in char.character_inventory:
                    print("The door is locked, and you seem to have misplaced your key.")
                else:
                    print("The door is already open!")
            elif action[1] == "cabinet":
                if not rooms.burrow.variables["jar_taken"]:
                    print("You opened the cabinet, there is an empty jar inside.")
                    rooms.burrow.room_contents.append("jar")
                else:
                    print("You opened the cabinet, it is empty")
        elif action[0] == "close":
            if action[1] == "trapdoor" and rooms.burrow.variables["rug_moved"]:
                print("You closed the trapdoor.")
                rooms.burrow.variables["trapdoor_opened"] = False
            elif action[1] == "door":
                print("The door is already closed, you like it that way.")
        else:
            continue

def burrow_basement():
    print("You are in your basement. There is a trapdoor above you.")
    while True:
        action = actions.get_action(rooms.burrow_basement)
        if action == "up":
            if rooms.burrow.variables["trapdoor_opened"]:
                load_room("burrow")
                break
            else:
                print("The trapdoor is shut.")
        elif action in rooms.directions:
            print("You can't go that way!")
        elif action[0] == "examine":
            if action[1] == "key_hook":
                if "key" in rooms.burrow_basement.room_contents:
                    print("It is a handmade key hook your Uncle Frogert made. Its single hook remains unoccupied.")
                else:
                    print("It is handmade key hook your Uncle Frogert made. It holds an old key.")
            elif action[1] == "icebox":
                print("It is an icebox where you store your cold foods, but it hasn't been filled in months.")
        elif action[0] == "move":
            if action[1] == "icebox" and not rooms.burrow_basement.variables["icebox_moved"]:
                pass
            elif action[1] == "icebox":
                pass
        elif action[0] == "use":
            if action[1] == "icebox" and not rooms.burrow_basement.variables["icebox_opened"]:
                rooms.burrow_basement.variables["icebox_opened"] = True
                if not rooms.burrow_basement.variables["fish_sticks_taken"]:
                    print("You opened the icebox, there's a lonely box of fish sticks inside with colorful writing on it.")
                    rooms.burrow_basement.room_contents.append("fish_sticks")
                else:
                    print("You opened the icebox, it's empty devoid of a few lonely ice cubes. ")
            elif action[1] == "icebox":
                print("You closed the icebox like a good roommate.")
                rooms.burrow_basement.variables["icebox_opened"] = False
                if "fish_sticks" in rooms.burrow_basement.room_contents and not rooms.burrow.variables["fish_sticks_taken"]:
                    rooms.burrow_basement.room_contents.remove("fish_sticks")
        elif action[0] == "open":
            if action[1] == "trapdoor" and not rooms.burrow.variables["trapdoor_opened"]:
                print("You opened the trapdoor.")
                rooms.burrow.variables["trapdoor_opened"] = True
            elif action[1] == "trapdoor":
                print("The trapdoor is already opened.")
            elif action[1] == "icebox" and not rooms.burrow_basement.variables["icebox_opened"]:
                rooms.burrow_basement.variables["icebox_opened"] = True
                if not rooms.burrow_basement.variables["fish_sticks_taken"]:
                    print("You opened the icebox, there's a lonely box of fish sticks inside with colorful writing on it.")
                    rooms.burrow_basement.room_contents.append("fish_sticks")
                else:
                    print("You opened the icebox, it's empty devoid of a few lonely ice cubes. ")
        elif action[0] == "close":
            if action[1] == "trapdoor" and rooms.burrow.variables["rug_moved"]:
                print("You closed the trapdoor.")
                rooms.burrow.variables["trapdoor_opened"] = False
            elif action[1] == "icebox" and rooms.burrow_basement.variables["icebox_opened"]:
                print("You closed the icebox like a good roommate.")
                rooms.burrow_basement.variables["icebox_opened"] = False
                if "fish_sticks" in rooms.burrow_basement.room_contents and not rooms.burrow.variables["fish_sticks_taken"]:
                    rooms.burrow_basement.room_contents.remove("fish_sticks")
        else:
            continue

def front_of_house():
    print("You are in front of your burrow")
    while True:
        break

"""
def room_template():
    print("ROOM. EXITS")
    while True:
        action = actions.get_action(rooms.ROOM)
        if action[0] == "mopi":
            load_room(action[1])
        if action == DIRECTION:

        elif action in rooms.directions:
            print("You cant go that way!")
        elif action[0] == "examine":

        elif action[0] == "move":

        elif action[0] == "use":

        elif action[0] == "open":

        elif action[0] == "close":

        else:
            continue
"""

def main():
    check_start()

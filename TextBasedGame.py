# Jeremy Dawson
# IT140
# Professor Wright

# status function will print current room and current inventory for the player
def status():
    print("------------------------------")
    print(f"You are in the {current_room}")  # Shows players current room
    print()
    print(f"Inventory: {', '.join(inventory) if inventory else 'empty inventory'}")  # Displays current inventory
    if "item" in rooms[current_room]:  # If there is an item in the dictionary of the current_room
        print(f"Item in room: {rooms[current_room]["item"]}")  # Print the item that is located in the room
    print("------------------------------")

def game_lost(): # displays the losing message if winning conditions are not met
    print("╔════════════════════════════════════════════╗")
    print("║              G A M E  O V E R !            ║")
    print("╠════════════════════════════════════════════╣")
    print("║        You did not have all items!         ║")
    print("║    The cemetery guard overpowers you...    ║")
    print("║                                            ║")
    print("║     Collect all items before entering!     ║")
    print("╚════════════════════════════════════════════╝")

def game_won(): # prints game winning message if winning conditions are met
    print("╔════════════════════════════════════════════╗")
    print("║              V I C T O R Y !               ║")
    print("╠════════════════════════════════════════════╣")
    print("║    You have collected all the items and    ║")
    print("║      the guard has been vanquished!        ║")
    print("║       The crusade is complete...           ║")
    print("║                                            ║")
    print("║                 For now!                   ║")
    print("╚════════════════════════════════════════════╝")

def game_name():  # prints splash screen with game name using raw string
    print(r""" 
       █████████  █████                                    █████                   
      ███░░░░░███░░███                                    ░░███                    
     ███     ░░░  ░███████   █████ ████ ████████   ██████  ░███████                
    ░███          ░███░░███ ░░███ ░███ ░░███░░███ ███░░███ ░███░░███               
    ░███          ░███ ░███  ░███ ░███  ░███ ░░░ ░███ ░░░  ░███ ░███               
    ░░███     ███ ░███ ░███  ░███ ░███  ░███     ░███  ███ ░███ ░███               
     ░░█████████  ████ █████ ░░████████ █████    ░░██████  ████ █████              
      ░░░░░░░░░  ░░░░ ░░░░░   ░░░░░░░░ ░░░░░      ░░░░░░  ░░░░ ░░░░░               



       █████████                                             █████                 
      ███░░░░░███                                           ░░███                  
     ███     ░░░  ████████  █████ ████  █████   ██████    ███████   ██████   █████ 
    ░███         ░░███░░███░░███ ░███  ███░░   ░░░░░███  ███░░███  ███░░███ ███░░  
    ░███          ░███ ░░░  ░███ ░███ ░░█████   ███████ ░███ ░███ ░███████ ░░█████ 
    ░░███     ███ ░███      ░███ ░███  ░░░░███ ███░░███ ░███ ░███ ░███░░░   ░░░░███
     ░░█████████  █████     ░░████████ ██████ ░░████████░░████████░░██████  ██████ 
      ░░░░░░░░░  ░░░░░       ░░░░░░░░ ░░░░░░   ░░░░░░░░  ░░░░░░░░  ░░░░░░  ░░░░░░  

                                                                                                                                              

    """)



def instructions(): # prints the command instructions for the user using multi-line string
    print("""
╔════════════════════════════════════════════════════════════════════════════╗
║                                INSTRUCTIONS                                ║
║════════════════════════════════════════════════════════════════════════════║
║  To move through rooms type the following directional commands:            ║
║  go north, go south, go east, or go west                                   ║
║                                                                            ║
║  To pick up an item, type the command get [item name] (with no brackets).  ║
║                                                                            ║
║  To quit the game type quit.                                               ║
║                                                                            ║
║  To view the instructions at anytime, type instructions                    ║
║                                                                            ║
║  To win, you must collect all items before you reach the cemetery guard!   ║
╚════════════════════════════════════════════════════════════════════════════╝
    """)



# the dictionary links a room to adjacent rooms and lists the item, if any, in that room.
rooms = {
    'Narthex': {'east': 'Sanctuary'},
    'Sanctuary': {'south': 'Control Room', 'north': 'Library', 'east': 'Tool Shed', 'west': 'Narthex', 'item': 'note'},
    'Control Room': {'east': 'Basement', 'north': 'Sanctuary', 'item': 'flashlight'},
    'Library': {'east': 'Kitchen', 'south': 'Sanctuary', 'item': 'rope'},
    'Kitchen': {'west': 'Library', 'item': 'sandwich'},
    'Basement': {'west': 'Control Room', 'item': 'dagger'},
    'Tool Shed': {'west': 'Sanctuary', 'north': 'Church Cemetery', 'item': 'shovel'},
    'Church Cemetery': {'south': 'Tool Shed'}
}

current_room = "Narthex"  # set the starting room
inventory = []  # set starting inventory to an empty list

game_name() # displays game name graphic
input("PRESS ENTER TO START!" .center(80))  # alerts user enter to start the game.  center aligned under graphic
print()

instructions()
def main():
    global current_room

    while True:
        status() # call status function to display inventory and current room
        print() # add blank space to readability

        if len(inventory) == 6 and current_room == "Church Cemetery": # checks for winning conditions
            game_won() # calls winning message function if conditions are true
            break # ends loop after printing winning message

        elif len(inventory) != 6 and current_room == "Church Cemetery": # if win conditions are not met
            game_lost() # call function to print losing message
            break # end loop.

        move = input("Enter command: ").lower().split() # make user command lower case and split by whitespace
        if len(move) == 0: # if user enters no command print warning followed by command syntax
            print()
            print("[X] Invalid command. please use go [direction], get [item] or instructions [X]")
            print()

            continue # back to beginning of loop after invalid command. skips final else error message.

        if move[0] == "go" and len(move) > 1: # checking for go in command and making sure they type a direction
            if move[1] in rooms[current_room]: # if the direction exists in the rooms dictionary
                current_room = rooms[current_room][move[1]] # change current_room
            else:
                print()
                print("[!] Cannot move that direction [!]") # prints error message if conditions not met


        elif move[0] == "get" and len(move) > 1: # check for get in command and that user enters item
            if "item" in rooms[current_room]  and move[1] == rooms[current_room]["item"]:
                inventory.append(move[1]) # add item to inventory list
                del rooms[current_room]["item"] # delete item from dictionary for the current room
                print()
                print(f"[!] {move[1]} added to inventory [!]") # print success message
            else:
                print()
                print(f"[X] There is no {move[1]} to get! [X]") # error message if item does not exist

        elif move[0] == "quit": # if user types quit
            print()
            print("Thank you for playing. Goodbye!") # print goodbye message
            break

        elif move[0] == "instructions": # if user types instructions
            instructions() # call instructions function

        else:
            print()
            print("[X] Invalid command! Please use go [direction] or get [item] [X]")

        print()
main()

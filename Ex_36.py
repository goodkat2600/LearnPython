from sys import exit


def start():
    print "You have come to a dungeon seeking great riches. Navigate through the dungeon to the treasure room."
    print "At the end of the narrow hallway is a door."
    print "To your left is an air duct."
    print "Do you:\n1. Open the door?\n2. Crawl through the air duct?"
    choice = raw_input("> ")

    if choice == "1":
        print "As you walk through the door you step onto a large cobweb waking a huge spider."
        dead("The spider paralyses you and spins you into a cocoon.")

    elif choice == "2":
        print "You crawl through the dusty vent. Rats everywhere but you make it through."
        room1()

    else:
        dead("You failed to follow the rules and now you must die!")


def dead(cause):
    print cause, "Well played!"
    exit(0)


def room1():
    print "You stand before two doors, one to your left and one to your right."
    print "Which door do you choose to open?"
    choice = raw_input("> ")

    while True:

        if "left" in choice:
            treasure_room()

        elif "right" in choice:
            bear_room()

        else:
            print "Please choose \"left\" or \"right\", dipshit."


def bear_room():
    print "You wake the sleeping bear in the room."
    dead("The bear eats your face.")


def treasure_room():
    print "The room is full of treasure!"
    print "You stuff your backpack and pockets with coins and gemstones."
    print "You make your way out of the dungeon the way from which you came. You win!"
    exit(0)


start()

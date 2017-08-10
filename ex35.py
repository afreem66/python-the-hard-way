from sys import exit


def gold_room():
    print("this room is full of gold. how much do you take?")

    choice = input("> ")
    if "0" in choice or "1" in choice:
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice you're not greedy, you win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("there is a bear in here")
    print("the bear had a bunch of honey")
    print("the fat bear is in front of another door")
    print("How are you going to move the bear")
    bear_moved = False

    while True:
        choice = input("> ")

        if choice == "take honey":
            dead("the bear looks at you then slaps your face off")
        elif choice == "taunt bear" and not bear_moved:
            print("the bear has moved frmo the door")
            print("you can go through it now")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("the bear gets pissed off and chews your leg off")
        elif choice == "open door" and bear_moved:
            gold_room()
        else:
            print("I got no idea what that means")


def cthulu_room():
    print("here you see the great evil cthulu")
    print("he, it, whatever stares at you and you go insane")
    print("Do you flee for your life or eat your head?")

    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("well that was tasty")
    else:
        cthulu_room()


def dead(why):
    print(why, "Good job!")
    exit(0)


def start():
    print('you are in a dark room')
    print('there is a door to your right and left')
    print("which one do you take")

    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulu_room()
    else:
        dead("you stumble around the room until you starve")

start()

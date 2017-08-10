print('''you enter a dark room with two doors.
      do you got through door #1 or door #2''')

door = input("> ")

if door == "1":
    print("there's a giant bear here eating cheese cake")
    print("What do you want to do?")
    print("1. Take the cake")
    print("2. Scream at the bear")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off good job")
    elif bear == "2":
        print("The bear eats your legs off. good job")
    else:
        print(f"Well, doing {bear} is probably better")
        print("bear runs away")

elif door == "2":
    print("you're staring into the endless abyss of cthulhu's retina")
    print("1. blueberries")
    print("2. yellow jacket clothespins")
    print("3. understanding revolvers yelling melodies")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("your body survives powered by a mind of jello")
        print("good job")
    else:
        print("The insanity rots your eyes into a pool of muck")
        print("good job")
else:
    print("you stumble around and fall on a knife and die. good job!")


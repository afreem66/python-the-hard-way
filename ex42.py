from sys import exit
from random import randint


class Game(object):

    def __init__(self, start):
        self.quips = [
            "You died. You kinda suck at this.",
            "Your mom would be proud. If she were smarter",
            "Such a luser.",
            "I have a small puppy that is better at this"
        ]
        self.start = start

    def play(self):
        next = self.start

        while True:
            print("\n------------")
            room = getattr(self, next)
            next = room()

    def death(self):
        print(self.quips[randint(0, len(self.quips)-1)])
        exit(1)

    def princess_lives_here(self):
        print("""You see a bautiful Princess with a shiny crown.
              She offers you some cake.""")

        eat_it = input("> ")

        if eat_it == "eat it":
            print("""You explode like a pinata full of frogs.
                  "The princess cackles and eats the frogs. Yumy!""")
            return 'death'

        elif eat_it == "do not eat it":
            print("""She throws the cake at you and it cuts off your head.
                  The last thing you see is her munching on your torso. Yum!""")
            return 'death'

        elif eat_it == "make her eat it":
            print("""The Princess screams as you cram the cake in her mouth"
                  Then she smiles and cries and thanks you for saving her.
                  She points to a tiny door and says, 'The Koi needs cake too.'
                  She gives you the very last bit of cake and shoves you in.""")
            return 'gold_koi_pond'

        else:
            print("The princess looks at you confused and just points at the cake")
            return 'princess_lives_here'

    def gold_koi_pond(self):
        print("""There is a garden with a koi pond in the center.
              You walk close and see a massive fin poke out.
              You peek in and a creepy looking huge koi stares at you.
              It opens its mouth waiting for food.""")

        feed_it = input("> ")

        if feed_it == 'feed it':
            print("""The koi jumps up, and rather than eating the cakes,
                  eats your arm.
                  You fall in and the Koi shrugs then eats you
                  You are then pooped out sometime later.""")
            return 'death'

        elif feed_it == 'do not feed it':
            print("""The koi grimaces, then thrashes around for a second.
                  It rushes to the other end of the pond,
                  braces against the wall...  then it *lunges* out of the
                  water, up in the air and over your entire body,
                  cake and all you are then pooped out a week later.""")
            return 'death'

        elif feed_it == 'throw it in':
            print("""The Koi wiggles, then leaps into the air and eats the cake.
                  You can see it's happy, it then grunts, thrashes...
                  and finally rolls over and poops a magic diamond into the air
                  at your feet.""")

            return 'bear_with_sword'

        else:
            print("The Koi gets annoyed and wiggles a bit.")
            return 'gold_koi_pond'

    def bear_with_sword(self):
        print("""Puzzled, you are about to pick up the fish poop diamond when
              a bear bearing a load bearing a sword walks in.
              Hey! That's my diamond! Where'd you get that!?
              It holds its paw out and looks at you.""")

        give_it = input('> ')

        if give_it == "give it":
            print("""THe bars swipes at your hand to grab the diamond and
                  rips your hand off in the process. It then looks at
                  your bloody stump and says 'Oh crap, sorry about that.'
                  It tries to put your hand back on but you collapse.
                  The last thing you see is the bear shrug and eat you.""")
            return 'death'

        elif give_it == "say no":
            print("""The bear looks shocked. Nobdy every told a bear
                  with a broadsword no. It asks,
                  'is it beacuse it's not a katana? I could go get one!'
                  It then runs off and now you notice a big iron gate.
                  'Where the hell did that coem from?' You say.""")
            return 'big_iron_gate'

        else:
            print("The bear looks puzzled as to why you'd do that.")
            return 'bear_with_sword'

    def big_iron_gate(self):
        print("You walk up to a big iron gate and see there's a handle")

        open_it = input("> ")

        if open_it == 'open it':
            print("""You open it and you are free!
                  There are mountains. And berries! And...
                  Oh, but then the bear comes wiht his katana and stabs you.
                  'Who's laughing now!? Love this katana.'""")

            return 'death'

        else:
            print("That doesn't seem sensible. I mean, the door's right there.")
            return 'big_iron_gate'

a_game = Game("princess_lives_here")
a_game.play()

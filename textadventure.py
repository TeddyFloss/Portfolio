# ...
# MonoTeddy
# Text Adventure (Escape/Horror Edition)
# 7/11/17 -
# ...

from time import sleep
from os import system

system("cls")
name = input("What is your name?")
print(" ")
print("Hello" + " " + name)
sleep(2)
print("...")
# to make into an integer in the way that's not the usual do var = int(var)
start = input("Do you want to play a game?")

if start is "yes" or " yes":  #is is not necessarily better that ==
    print()
    print("Good. Let's begin.")
    print(" ")
    dream = input("Tell me, what's your biggest dream in life. It doesn't have to be possible. Tell me your hearts desire.")
    if dream is "be happy":
                print("That's...")
                sleep(3)
                print("...")
                sleep(3)
                print()
                sleep(3)
                print("I see, you must go.")
                sleep(3)
                system("cls")
                print("Game Over")
                sleep(10)
    else:
                    print()
                    print("You've...")
                    sleep(3)
                    print("...")
                    sleep(3)
                    print("You've lied to me." + "'" + dream + "''"  + "is not your hearts desire. I despise lies.")
                    sleep(3)
                    print("Maybe some time in a cell might teach you the benefits of honesty.")
                    sleep(3)
                    system("cls")
                    sleep(1)
                    print("*You find yourself in a darkened cell. It has a peculiar smell*")
else:
    print("No? You really have no choice here. Don't be foolish, let's continue.")
    print()
    dream = input("Tell me, what's your biggest dream in life. It doesn't have to be possible. Tell me your hearts desire.")
    print()
    print("You've...")
    sleep(3)
    print("...")
    sleep(3)
    print("You've lied to me." + "'" + dream + "''"  + "is not your hearts desire. I despise lies.")
    sleep(3)
    print("Maybe some time in a cell might teach you the benefits of honesty.")
    sleep(3)
    system("cls")
    sleep(1)
    print("*You find yourself in a darkened cell. It has a peculiar smell*")

print()
firstchoice = input("Look around or Wait")
if firstchoice is "look around" or " look around":
    print()
    print("*You can't see very well in the dark, but you can make out the shape of a bed and a tiny window*")
    print()
    print("*Panic has begun to set in. The dark is stifling *") # Storyline 1
    secondchoice = input("Relax or Accept Adrenaline")
    if secondchoice is "relax" or " relax":
        print()
        print("*You've calmed down, and have accpeted your fate as a denizen of the cell.*")
        sleep(3)
        system("cls")
        print("Game Over")
        sleep(4)
        system("cls")
        message = "I would've thought you had more resolve.Pity."
        for c in message:
            if c != "/n":
                print(c, end = "", flush = True)
                sleep(0.1)
    elif secondchoice is "accept adrenaline":
        print("*The adrenaline gives you an unnatural boost in strength. You rip the window straight out the wall.*")
        print("...")
        print("*You hear the telltale click of an intercom system*")
        print()
        print("Very imperssive")
        print()
        print("Your strength shows a will to live that I respect. You may go")
        system("cls")
        print("Game Over")
        sleep(4)
        system("cls")
        message2 = "Humans are surprisingly resilient"
        for c in message2:
            if c != "/n":
                print(c, end = "", flush = True)
                sleep(0.1)


elif firstchoice is "wait" or " wait":
    print()
    print("*You hear some quiet shuffling, light floods the room through a previously unseen window*")
    secondchoice2 = input("Go to window or Watch")
    if secondchoice2 is "got to window" or " go to window":
        print("*You peer through the window and the blinding light burn your eyes. Your yell of pain alerts whoever is outside.*")
        print()
        print("They quickly cover the window again. Darkness falls. That was your only chance. You will be here forever...")
        sleep(3)
        system("cls")
        print("Game Over")
        sleep(4)
        system("cls")
        message3 = "If only you'd thought about this more carefully. Shame."
        for c in message3:
            if c != "/n":
                print(c, end = "", flush = True)
                sleep(0.1)
    elif secondchoice2 is "watch" or " watch":
        print("*You peet through the shadows at the shape flitting across the window.*")
        print()
        print("*At the right time your run towards the window and bang on it, hard.*")
        print()
        print("*The startled individual kicks the window hard enough for it to shatter.*")
        print(...)
        print("*You smirk. Escape has been achieved.*")
        sleep(3)
        system("cls")
        print("Game Over")
        sleep(4)
        system("cls")
        message3 = "You've showcased a despicable sense of cunning. How interesting."
        for c in message3:
            if c != "/n":
                print(c, end = "", flush = True)
                sleep(0.1)

     #Storyline 2
else:
    print("*You mutter gibberish for a bit before reconsidering your choice*") # Nonsense choice

firstchoice2 = input("Look around or Wait")
if firstchoice2 is "look around": #Storyline 1
    print("*You can't see very well in the dark, but you can make out the shape of a bed and a tiny window*")
    print()
    print("*Panic has begun to set in. The dark is stifling *")
    secondchoice3 = input("Relax or Accept Adrenaline")
    if secondchoice3 is "relax" or " relax":
        print()
        print("*You've calmed down, and have accpeted your fate as a denizen of the cell.*")
        sleep(3)
        system("cls")
        print("Game Over")
        sleep(4)
        system("cls")
        message = "I would've thought you had more resolve.Pity."
        for c in message:
            if c != "/n":
                print(c, end = "", flush = True)
                sleep(0.1)
    elif secondchoice3 is "accept adrenaline":
        print("*The adrenaline gives you an unnatural boost in strength. You rip the window straight out the wall.*")
        print("...")
        print("*You hear the telltale click of an intercom system*")
        print()
        print("Very imperssive")
        print()
        print("Your strength shows a will to live that I respect. You may go")
        system("cls")
        print("Game Over")
        sleep(4)
        system("cls")
        message2 = "Humans are surprisingly resilient"
        for c in message2:
            if c != "/n":
                print(c, end = "", flush = True)
                sleep(0.1)
elif firstchoice2 is "wait" or " wait":
    print("*You hear some quiet shuffling, light floods the room through a previously unseen window*") #Storyline 2
    print()
    print("*You hear some quiet shuffling, light floods the room through a previously unseen window*")
    secondchoice2 = input("Go to window or Watch")
    if secondchoice2 is "got to window" or " go to window":
        print("*You peer through the window and the blinding light burn your eyes. Your yell of pain alerts whoever is outside.*")
        print()
        print("They quickly cover the window again. Darkness falls. That was your only chance. You will be here forever...")
        sleep(3)
        system("cls")
        print("Game Over")
        sleep(4)
        system("cls")
        message3 = "If only you'd thought about this more carefully. Shame."
        for c in message3:
            if c != "/n":
                print(c, end = "", flush = True)
                sleep(0.1)

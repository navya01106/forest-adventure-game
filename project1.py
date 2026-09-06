name = input("enter your name ")
print(f"hello {name}")
choice = input("are you ready to go on an adventure?!\n press 1 for yes and 0 for no")


def river():
    print("You made the choice and came here.\n all you see is a river with the moonlight shining across its waves, but the water is gurgling loudly, and you don't even see a ship or a lighthouse to call for help.")


def cave():
    print("It's dark. It's gloomy. You have just entered a cave.\n you hear the snap of a twig you just stepped on the stone walls are so close they seem to swallow your breath. You hear the clicking of bats. Would you want to move forward?")


def cave_up():
    print("This feels like a dead end. We have to go back now. But the candle is going to go off soon, so you have to make a decision quickly.")


def cave_down():
    print("This was the right way out. You have now reached a village, and you can ask people for help. Congratulations!")


if choice == "1":
    print("hello! you have just woken up in a dark forest surrounded by dark green trees and dark woods where no human soul is to be seen, there doesn't seem to be a house for a distance")
    print("now you don't really remember how you got here or what happened to you, but all you see is the darkness of the forest. Now the choice is yours. You can either go LEFT or RIGHT.")

    choose = int(input("Type 1 for left and 0 for right."))
    if choose == 1:
        river()
    else:
        cave()
        choice3 = input("Would you like to move further in the cave, or would you like to go back to where you started and choose the left option in the menu.\n to move further, type 'yes', and for going back, type 'no'.").lower()

        if choice3 == 'yes':
            choice4 = input("You have moved forward a little bit, but you still don't see anything. \nThere is only a candle in your hand, and it shows two parts: one to climb up and one to go down, but it's slippery and it's all dark, so it's a risky choice.\n You still have to keep your courage and choose one type 'up' to climb up and 'down' to climb down.").lower()

            if choice4 == 'up':
                cave_up()
            else:
                cave_down()
        else:
            print("You have come back to where it all started, but now the candle has gone out.")
else:
    print("Thank you for your precious time. Hope to see you soon.")

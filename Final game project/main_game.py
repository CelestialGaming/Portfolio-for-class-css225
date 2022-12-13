#main_game.py
#David Serna
#11/1/2022
#This file will control the rest of the game.

#Remember to put all your files into the same folder on your computer!
#Otherwise, these import statements won't be able to find them properly.

#Import the main character and section files here
import main_character
import section_1


def main():
    #Intro text to the user
    #The empty input functions are only here so the player has to type something to move on
    #(like pressing a button in a video game to move the dialogue along)
    print("Greetings, your name is Marven. You're alive for some reason!")
    print("5 years ago, you and your friend Krassie found a magical bridge that led you to another world")
    print("This world is a potato based world. However, one fateful day occured when a rotten evil potato grew as you explored")
    print("He used to be the king of the potato world, and now he turned rotten and you must defeat him. Your friend Krassie")
    print("who you thought had passed away is still alive but trapped with the potato king. You must bring peace to the kingdom")
    print("and defeat this potato king. Let this adventure start! and oh the bridge is also in tatters so please repair that")
    input('press "ENTER" to continue\n')

    #And do/say anything else to get your game started

    print("Let's go!")
    #Then call your first section.
    section_1.start()

if __name__ == "__main__":
    main()
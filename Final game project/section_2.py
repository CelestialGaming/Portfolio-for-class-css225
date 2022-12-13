import section_3
import main_character
player = main_character.main_character()


def start():
    print("""You are in the potato kingdom after doing some timey-whimy bridge thing that not many people can
    understand! Doctor whooing in this world. Anyways, sorry the narrator wrote this while sleepy. So in this section
    you need to do two things. 
    
    One, get a key from an abandon building that you would know
    Two, a sword. Yeah seriously a sword to defeat the enemy boss.
    
    Don't know where to find them? too bad. Good luck.""")


    input()

def start():
    print("""You're standing at crossroads used to be. In order to progress, you must find the following:
    A Key to the castle
    And the legendary potato Sword that can be wielded by a person that shall bring justice! or just a regular
    potato themed sword.""")

    # you can add a while loop here to repeat the inputs like you stated on line 38
    # you will have to add checks or flags to see if the user has collected what you want them to
    # for example,
    # while 'wand' not in main_character.items and 'hammer' not in main_character.items:
    # this will allo you to check if the user has
    print("Where would you like to go?")
    choice = int(input("""
    2. Head to nearby stones beyond yellow tape where the sword rests  
    1. Head to the Abandoned guardmen's house   
    3. Head to the Castle to face the evil potato man"""))

    if choice == 1:
        print("""You head to the nearby stones. There is yellow tape and beyond them shall be the stones where the
        legendary potato sword should be housed and last rested.""")
        choice = input("Would you like to go beyond the yellow tape? Y/N")
        #If the player chooses to speak with wood workers, the player gets wood to build bridge
        # main_character.items.append('wood')
        main_character.items.append('legendary_sword')
    elif choice == 2:
        print("You head to the guard's old house where all the keys are stored there.")
        choice = input(" Would you like to look around? Y/N")
        #Give the player the choice to look around, if player chooses to look around, the player gets a key to castle
        main_character.items.append('key_to_castle')
    elif choice == 3:
        print("You headed to the forest, would you like to look around? Y/N")
        # Give the player the choice to look around, if player chooses to look around, the player gets a
    else:
        print("You try to cross the bridge")






section_3.start()
#import main_character and section_2 here
import main_character
import section_2

#Header comments go here
player = main_character.main_character()


#This start function is called by main_game.
#This will control the whole section.
#It'll need the player character as an input in order to interact with them.
def start():
    print("""You're standing at crossroads used to be. In order to progress, you must find the following:
    A hammer
    A wand
    And wood in the woods""")

    # you can add a while loop here to repeat the inputs like you stated on line 38
    # you will have to add checks or flags to see if the user has collected what you want them to
    # for example,
    # while 'wand' not in main_character.items and 'hammer' not in main_character.items:
    # this will allo you to check if the user has
    print("Where would you like to go?")
    choice = int(input("""
    2. Head to nearby roads  
    1. Head to the Savanna Biome   
    3. Head to the Forest
    4. Bridge"""))

    if choice == 1:
        print("You head to the nearby roads. There is a wood mill nearby with wood workers.")
        choice = input("Would you like to speak to the wood workers? Y/N")
        #If the player chooses to speak with wood workers, the player gets wood to build bridge
        main_character.items.append('wood')
    elif choice == 2:
        print("You head to the Savanna biome nearby, would you like to look around? Y/N")
        #Give the player the choice to look around, if player chooses to look around, the player gets a hammer
        main_character.items.append('hammer')
    elif choice == 3:
        print("You headed to the forest, would you like to look around? Y/N")
        # Give the player the choice to look around, if player chooses to look around, the player gets a wand
        main_character.items.append('wand')
    else:
        print("You try to cross the bridge")
        #If the player doesn't have A wand, hammer, or wood then repeat the choices where to go
            #If player has met all the requirements,
            #Add the new pokemon to the player's team

    #Give the player some options of things to do here.
    #Be sure to put their choice in a variable!
    
    #Then use an if/elif/else statement to do something based on the player's choice.
    
    #One of the options should move the story to the next section with code like this:
    section_2.start()
    
    #Add pseudocode here to describe the rest of the functionality of this section of your game.
    #You may also draw and submit flowcharts if you prefer.

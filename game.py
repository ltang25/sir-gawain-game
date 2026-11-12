from js import gawainInput, gawainPrint
async def browser_input(prompt=""):
    return await gawainInput(prompt)
def print(*values, sep=" ", end="\n"):
    gawainPrint(sep.join(str(v) for v in values) + end)

import random



playing = True



# setup 

gold = 500

player_choice = 0



food = True

sword = False

girdle = False



ending = "None"

choice_input = "What will you choose: "

text_divider = "================================================================================"



# functions

def print_stats():

    print(text_divider)

    print("💰 GOLD:", gold)



    inventory = []



    if food:

        inventory.append("🥩 Food")

    if sword:

        inventory.append("🗡️ Sword")

    if girdle:

        inventory.append("👚 Girdle")



    if inventory:

        print("🎒 INVENTORY: " + "  •  ".join(inventory))

    else:

        print("🎒 INVENTORY: EMPTY")



async def press_enter():

    await browser_input("\n[Press ENTER to continue...]")



async def get_player_choice(max_options):

    while True: 

        try:

            player_choice = int(await browser_input(choice_input)) 

            if player_choice <= max_options and player_choice > 0:

                print(text_divider)
                return player_choice



            else:

                print(f"Invalid option. Please enter a number between 1 and {max_options}.")



        except ValueError: 

            print("Please enter a number.")



def scene_one_dialogue_one():

    print("You, Sir Gawain, are sitting with the knights of the round table, \npreparing to eat your Yuletide feast.")

    print("Suddenly, the doors burst open.")

    print(text_divider)
    
    print(r"""

                         --- THE GREEN KNIGHT ---
                         
                         ,   A           {}
                        / \, | ,        .--.
                       |    =|= >      /.--.\
                        \ /` | `       |====|
                         `   |         |`::`|
                             |     .-;`\..../`;-.
                            /\\/  /  |...::...|  \
                             |:'\|   /'''::'''\  |
                             \ /\;-,/\   ::   /\--;
                             |\ <` >  >._::_.<,<__>
                             | `""`  /   ^^   \|  |
                             |       |        |\::/
                             |       |        |/|||
                             |       |___/\___| '''
                             |        \_ || _/
                             |        <_ >< _>
                             |        |  ||  |
                             |        |  ||  |
                             |       _\.:||:./_
                             |      /____/\____\

        """)

    print(text_divider)

    print("A knight walks in, wearing all green.")

    print("He insults you guys and proposes a game: one of you will strike him with his axe, \nif they agree to receive the same hit a year and a day later.")

    print("No one volunteers.")

    print("The Green Knight shames your honor.")

    print("King Arthur steps up to play.")

    print(text_divider)

    print("Can you really let him play?")

    print("You know you're the least worthy of the table.")

    print("This could be your chance to prove yourself.")

    print(text_divider)

    print("Do you...")

    print(" ")

    print("   [1] Try to hide in the bathroom (50% success rate)   [-100 Gold]")

    print("   [2] Volunteer to play the game                       [Free]")

    print(" ")

    print(text_divider)



def scene_one_dialogue_two():

    print("You volunteer to play the game.")

    print("The other knights whisper amongst themselves.")

    print("You can't back down now.")

    print("You take the axe into your hands.")

    print("And... you bring it down onto the Green Knight's neck.")

    print("His head slices cleanly off and rolls onto the floor.")

    print(text_divider)
    

    print(r"""
    
                         .-;`\..../`;-.
                        /  |...::...|  \
                       |   /'''::'''\   |
                       ;--'\   ::   /\--;
                       <__>,>._::_.<,<__>
                       |  |/   ^^   \|  |
                       \::/|        |\::/
                       |||\|        |/|||
                       ''' |___/\___| '''
                            \_ || _/
                            <_ >< _>
                            |  ||  |
                            |  ||  |
                           _\.:||:./_
                          /____/\____\

                                           {}
                                          .--.
                                         /.--.\
                                         |====|
                                         |`::`|
                                         \____/

    """)

    print(text_divider)

    print("You stop holding your breath, thinking you beat him.")

    print("Uh oh... he grabs his head by the hair and starts talking.")

    print("He tells you to find him in a year and one day at the Green Chapel.")

    print("The Green Knight gets on his horse and leaves.")

    print("Now, the feast begins.")

    print(text_divider)



def scene_two_dialogue_one():

    print("After a year of dread, you've finally set out to find the Green Knight.")

    print("You're walking through the forest, hoping to find a good place to sleep.")

    print("You see something by the bushes ahead.")

    print("It's still light out, so you go see what it is.")

    print(text_divider)
    

    print(r"""

                            |\_/|,,_____,~~`
                            (.".)~~     )`~}}
                             \o/\ /---~\\ ~}}
                               _//    _// ~}

    """)

    print(text_divider)

    print("A little fox is curled up, pleadingly staring up at you.")

    print("His foot is clearly wounded from nearby hunters... Maybe there's people nearby. \nHe's probably hungry.")

    print("You feel bad, but you only have a little bit of food left, \nand you need to keep your energy up.")

    print(text_divider)

    print("Do you...")

    print(" ")

    print("   [1] Leave the fox alone      [Free]")

    print("   [2] Give the fox your food   [-Food]")

    print(" ")

    print(text_divider)



def scene_two_dialogue_two():
    

    print(r"""

                        .        +          .      .          .
                .            _        .                    .
            ,              /;-._,-.____        ,-----.__
            ((        .    (_:#::_.:::. `-._   /:, /-._, `._,
            `                 \   _|`"=:_::.`.);  \ __/ /
                                ,    `./  \:. `.   )==-'  .
                .      ., ,-=-.  ,\, +#./`   \:.  / /           .
            .           \/:/`-' , ,\ '` ` `   ): , /_  -o
                .    /:+- - + +- : :- + + -:'  /(o-) \)     .
            .      ,=':  \    ` `/` ' , , ,:' `'--".--"---._/`7
            `.   (    \: \,-._` ` + '\, ,"   _,--._,---":.__/
                        \:  `  X` _| _,\/'   .-'
            .               ":._:`\____  /:'  /      .           .
                                \::.  :\/:'  /              +
            .                 `.:.  /:'  }      .
                    .           ):_(:;   \           .
                                /:. _/ ,  |
                            . (|::.     ,`                  .
                .               |::.    {\
                                |::.\  \ `.
                                |:::(\    |
                        O       |:::/{ }  |                  (o
                        )  ___/#\::`/ (O "==._____   O, (O  /`
                    ~~~w/w~"~~,\` `:/,-(~`"~~~~~~~~"~o~\~/~w|/~
                ~~~~~~~~~~~~~~~~~~~~~~~\\W~~~~~~~~~~~~\|/~~

    """)

    print(text_divider)

    print("Finally, you sleep.")

    print(text_divider)

    print("You wake up and keep walking through the forest.")

    print("You see something in the distance...")

    print(text_divider)



def scene_three_dialogue_one():
    

    print(r"""

             /\         /\                    .           /\
            /  \       /  \                   |@>        /  \
           /    \     / .  \                  |         /    \
          /      \   /  |@> \       /\       / \       /      \
         /     /\ \ /   |    \     /  \     /   \     /        \
        /     /  \ /  _ | _   \   /    \    | O |    /          _   _   _
       /     /    \  |_|_|_|   \ /      \   |___|   /          | |_| |_| |
            /      \  | O |     /        \  | |_|  /      /\   |         |
          _   _   _ \ |___|    /          \ |__|| /      /  \  |  O   O  |
         | |_| |_| |  | |_|   /             | |_|       /    \ |   __ _  |
         |         |  |__||  /              |_| |      /       |     |   |
         | O  O  O |  | |_| /               |__ |     /        | O  O  O |
         |  _      |  _   _   _        ______   |   _   _   _  |  _      |
         | |__|_ | |_| |_| |_| |______|      |_____| |_| |_| |_| |__|_ |_|
         |  |   _| |        _  |  |  HAUTDESERT  _||        _  |  |    | |
         |   _| _  ||_|   _|_  | _|_   |||||| |_| _||_|   _|_  |   _| _| |
        |   __|  |_|  |_       | | |__ |++++|   |_||  |_      ||  __|  |_|
        | _________|___________|-------------------|___________|_________|
                                       /_/_/
                                      /_/_/

    """)

    print(text_divider)

    print("You walk up to the door.")

    print(text_divider)

    print("A man answers the door. His name is Lord Bertilak of Hautdesert.")

    print("The lord's wife offers to bathe you after your long journey.")

    print(text_divider)
    

    print(r"""

                            --- LADY & LORD BERTILAK ---
                                              _                  
                                    mMm     _[_]_              
                                   /(_)\     (_)            
                                  //)^(\\   //:\\         
                                 /(/&@&\)\  \|~|/           
                                / /-~`~-\ \  |||           
                                `/       \   |||           
                                `--------'-'------

    """)

    print(text_divider)

    print("Do you...")

    print(" ")

    print("   [1] Accept her offer             [Free]")

    print("   [2] Ask her to cook you a meal   [-100 Gold]")

    print("   [3] Decline and bathe yourself   [-100 Gold]")

    print(" ")

    print(text_divider)



def scene_three_dialogue_two():

    print("For the first time in weeks, you finally wake up feeling well rested.")

    print("It's time to find the Green Chapel.")

    print("The lord's wife prepares you breakfast and you set out on your journey.")

    print(text_divider)



def scene_four_dialogue_one():  

    print(r"""

                    _    .  ,   .           .
                *  / \_ *  / \_         *        *   /\'__        *
                  /    \  /    \,             .    _/  /  \  *'.
             .   /\/\  /\/ :' __ \_  `          _^/  ^/    `--.
               /    \/  \  _/  \-'\      *    /.' ^_   \_   .'\  *
             /\  .-   `. \/     \ /==~=-=~=-=-;.  _/ \ -. `_/   \
            /  `-.__ ^   / .-'.--\ =-=~_=-=~=^/  _ `--./ .-'  `-
           /     `.  / /       `.~-^=-=~=^=.-'      '-._ `._

    """)

    print(text_divider)

    print("Finally, you see it.")

    print("The Green Chapel: a cave covered in grass and moss.")

    print("You hear the sounds of an axe being sharpened.")

    print("The Green Knight emerges from the cave and approaches you.")

    print("It is time to play the game.")

    print(text_divider)

    print("You're almost trembling with nerves.")

    print("This is your last chance to escape.")

    print("But you must keep your word.")

    print(text_divider)



async def scene_one():

    global gold, playing

    # play intro music

    print(" ")

    print(text_divider)

    print("WELCOME TO GAME")

    print(text_divider)

    print(r"""
                
                                          o
                                      _---|         _ _ _ _ _
                                   o   ---|     o   ]-I-I-I-[
                  _ _ _ _ _ _  _---|      | _---|    \ ` ' /
                  ]-I-I-I-I-[   ---|      |  ---|    |.   |
                   \ `   '_/       |     / \    |    | /^\|
                    [*]  __|       ^    / ^ \   ^    | |*||
                    |__   ,|      / \  /    `\ / \   | ===|
                 ___| ___ ,|__   /    /=_=_=_=\   \  |,  _|
                 I_I__I_I__I_I  (====(_________)___|_|____|____
                 \-\--|-|--/-/  |     I  [ ]__I I_I__|____I_I_|
                  |[]      '|   | []  |`__  . [  \-\--|-|--/-/
                  |.   | |' |___|_____I___|___I___|---------|
                 / \| []   .|_|-|_|-|-|_|-|_|-|_|-| []   [] |
                <===>  |   .|=-=-=-CAMELOT-=-=-=-=|   |    / \
                ] []|`   [] ||.|.|.|.|.|.|.|.|.|.||-      <===>
                ] []| ` |   |/////////\\\\\\\\\\.||__.  | |[] [
                <===>     ' ||||| |   |   | ||||.||  []   <===>
                 \T/  | |-- ||||| | O | O | ||||.|| . |'   \T/
                  |      . _||||| |   |   | ||||.|| |     | |
               ../|' v . | .|||||/____|____\|||| /|. . | . ./
               .|//\............/...........\........../../\\\

    """)

    print(text_divider)

    await press_enter()

    print(text_divider)

    print(" ")

    print("FITT I")

    print(" ")

    print(text_divider)

    print_stats()

    print(text_divider)

    scene_one_dialogue_one()

    player_choice = await get_player_choice(2)

    if player_choice == 1:

        gold -= 100

        print(" ")

        print("   [-] 💰 100 Gold")

        print(" ")

        if random.random() < 0.5:

            print(text_divider)

            print("COWARDLY ENDING")

            print(text_divider)

            print("You sucessfully hid from the Green Knight!")

            print("But now, you will be known as cowardly.")

            print("Think about your actions carefully...")

            print(text_divider)

            print("GAME OVER")

            print(text_divider)

            playing = False

        else:

            print(text_divider)

            print("You failed to hide from the Green Knight...")

            print("The knights scorn you when you return, and King Arthur volunteers you to play the game.")

            scene_one_dialogue_two()



    elif player_choice == 2:

        scene_one_dialogue_two()



async def scene_two():

    global gold, food, playing

    # play music

    print(" ")

    print(text_divider)

    print(" ")

    print("FITT II")

    print(" ")

    print(text_divider)

    print_stats()

    print(text_divider)

    scene_two_dialogue_one()

    player_choice = await get_player_choice(2)

    if player_choice == 1:

        gold -= 150

        print("The fox knows you chose to ignore him.")

        print("A malicious glint shows up in his eyes.")

        print("You have a bad feeling about this...")

        print(text_divider)

        print("You settle down for the night, sitting by a big tree.")

        print("You feel a bit lighter than usual. Maybe the energy from the food.")

        print("Except... you pat your pockets.")

        print("150 gold is missing!")

        print("It must've been that fox.")

        print("You really should've given him the food.")

        print(" ")

        print("   [-] 💰 150 Gold")

        print(" ")

        print_stats()

        print(text_divider)

        scene_two_dialogue_two()

    elif player_choice == 2:

        food = False

        print(" ")

        print("   [-] 🥩 Food")

        print(" ")

        print(text_divider)

        print("The fox happily gobbles up your food")

        print("Your stomach growls, but you're happy to watch the fox eat.")

        print_stats()

        print(text_divider)

        scene_two_dialogue_two()

async def scene_three():

    global gold, food, sword, girdle, playing

    # play music

    print(" ")

    print(text_divider)

    print(" ")

    print("FITT III")

    print(" ")

    print(text_divider)

    print_stats()

    print(text_divider)

    scene_three_dialogue_one()

    player_choice = await get_player_choice(3)

    if player_choice == 1:

        print("You are enjoying your nice warm bath.")

        print("The lord walks in and is furious!")

        print("You probably should've thought about how he would feel.")

        print("He kicks you out of the castle.")

        if food == False:

            print("You have no food left. Stupid fox.")

            print("You starve to death.")

            print(text_divider)

            print("STARVATION ENDING")

            print(text_divider)

        else:

            print("You take out your remaining food.")

            print("A colony of foxes starts chasing you!")

            print("They must've smelled the food.")

            print("You recognize the leader.")

            print("Maybe you should've given him the food earlier.")

            print("You die.")

            print(text_divider)

            print("FOX ATTACK ENDING")

            print(text_divider)



        print("GAME OVER")

        print(text_divider)

        playing = False



    elif player_choice == 2:

        gold -= 100

        print(" ")

        print("   [-] 💰 100 Gold")

        print(" ")

        print(text_divider)

        sword = True

        print("They grumble but agree to cook you a meal.")

        print("Maybe that was a bit too demanding of you.")

        print(text_divider)

        print("In the dining room, you see a shiny sword hanging on the wall.")

        print("You ask to see it.")

        print("They give it to you, and say you can borrow it for your journey.")

        print("Such gracious hosts!")

        print(" ")

        print("   [+] 🗡️ Sword")

        print(" ")

        print(text_divider)

        print_stats()

        print(text_divider)

        scene_three_dialogue_two()

    elif player_choice == 3:

        gold -= 100

        girdle = True

        print(" ")

        print("   [-] 💰 100 Gold")

        print(" ")

        print(text_divider)

        print("You politely decline and bathe yourself.")

        print(text_divider)

        print("Later that night, you find a green girdle on your nightstand.")

        print("The lady tells you that she finally had time to do the laundry since you bathed yourself.")

        print("She says that the girdle is magical and will protect you from harm.")

        print("Green isn't really your color, but it's a nice gift.")

        print(text_divider)

        print(" ")

        print("   [+] 👚 Girdle")

        print(" ")

        print(text_divider)

        print_stats()

        print(text_divider)

        scene_three_dialogue_two()



async def scene_four():

    global gold, food, sword, girdle, playing, ending

    # play music

    print(" ")

    print(text_divider)

    print(" ")

    print("FITT IV")

    print(" ")

    print(text_divider)

    print_stats()

    print(text_divider)

    if sword == True:

        scene_four_dialogue_one()

        print("Do you...")

        print(" ")

        print("   [1] Try to fight the Green Knight with the sword                [-Sword]")

        print("   [2] Accept your fate. You offer your neck to the Green Knight   [-200 Gold]")

        print(" ")

        player_choice = await get_player_choice(2)

        if player_choice == 1:

            sword = False

            print(text_divider)

            print(" ")

            print("   [-] 🗡️ Sword")

            print(" ")

            print_stats()

            print(text_divider)

            print("You swing your sword, trying to strike the Green Knight.")

            print("You miss. Kind of embarrassing.")

            print("It's over. The Green Knight stares at you in disappointment.")

            print("He reveals that he was Lord Bertilak all along.")

            print("He scolds you for breaking the rules of the game.")

            print("You really messed up this time.")

            print("He shakes his head and rides off into the distance.")

            print("Time for you to return home.")

            print(text_divider)

            ending = "fight"

        elif player_choice == 2:

            if gold >= 200:

                gold -= 200

                print(text_divider)

                print(" ")

                print("   [-] 💰 200 Gold")

                print(" ")

                print_stats()

                print(text_divider)

                print("You stand up tall, waiting to be struck by the axe.")

                print("If only you had a magical garment to protect you.")

                print("Too bad you only have the sword.")

                if food == False:

                    print(text_divider)

                    print("In the corner of your eye, you see a flash of orange. \nIt's the fox that you fed a few nights ago.")

                    print("He brushes past the Green Knight just as the axe comes down.")

                    print("The axe barely misses your neck, cutting off a chunk of your hair instead.")

                    print("Seems like sacrificing your food was the right choice.")

                    print("The Green Knight reveals that he was Lord Bertilak all along.")

                    print("He commends you for your selflessness towards the fox, who he had injured while hunting.")

                    print("Although, he wishes you were more respectful towards his wife.")

                    print("You shouldn't have made demands towards your gracious hosts.")

                    print("He lets you go home.")

                    print(text_divider)

                    ending = "bravery_sword_one"

                else:

                    print(text_divider)

                    print("The axe comes down on your arm, slicing it off.")

                    print("You're extremely surprised.")

                    print("The Green Knight reveals that he was Lord Bertilak all along.")

                    print("He scolds you for demanding that his wife make you dinner the other night.")

                    print("You should've been more respectful towards your gracious hosts.")

                    print("He lets you go home.")

                    print(text_divider)

                    ending = "bravery_sword_two"

            else:     

                print(text_divider) 

                print("You don't have enough gold for this option.")

                print("   [!] Not enough gold!")

                print("   You must take the other one.")

                sword = False

                print(text_divider)

                print(" ")

                print("   [-] 🗡️ Sword")

                print(" ")

                print(text_divider)

                print_stats()

                print(text_divider)

                print("You swing your sword, trying to strike the Green Knight.")

                print("You miss. Kind of embarrassing.")

                print("It's over. The Green Knight stares at you in disappointment.")

                print("He reveals that he was Lord Bertilak all along.")

                print("He scolds you for breaking the rules of the game.")

                print("You really messed up this time.")

                print("He shakes his head and rides off into the distance.")

                print("Time for you to return home.")

                print(text_divider)

                ending = "fight"





    elif girdle == True:

        scene_four_dialogue_one()

        print("Do you...")

        print(" ")

        print("   [1] Give the girdle to the Green Knight as a friendship offering   [-Girdle]")

        print("   [2] Accept your fate. You offer your neck to the Green Knight      [-200 Gold]")

        print(" ")

        player_choice = await get_player_choice(2)

        if player_choice == 1:

            girdle = False

            print(text_divider)

            print(" ")

            print("   [-] 👚 Girdle")

            print(" ")

            print_stats()

            print(text_divider)

            print("The Green Knight looks at you in confusion.")

            print("Maybe he doesn't like girdles.")

            print("Clearly, he thinks you have a few screws loose.")

            print("His gaze changes to pity.")

            print("He reveals that he was Lord Bertilak all along.")

            print("He lets you go, calling off the game.")

            print("Uh oh... Now everyone will think you're too dumb to play a game.")

            print("Next time, don't try to be different.")

            print("At least you didn't get hit.")

            print(text_divider)

            ending = "truce"

        elif player_choice == 2:

            if gold >= 200:

                gold -= 200

                print(" ")

                print("   [-] 💰 200 Gold")

                print(" ")

                print_stats()

                print(text_divider)

                print("The axe comes down...")

                print("and strikes the green girdle.")

                print("It must be magic.")

                print("The Green Knight reveals that he was Lord Bertilak all along.")

                print("This game has more layers than you thought.")

                print("Staying chivalrous has served you well.")

                print("Now, it's time to go home.")

                print(text_divider)

                ending = "bravery" 

            else:

                print("You don't have enough gold for this option.")

                print("   [!] Not enough gold!")

                print("   You must take the other one.")

                girdle = False

                print(" ")

                print("   [-] 👚 Girdle")

                print(" ")

                print(text_divider)

                print_stats()

                print(text_divider)

                print("The Green Knight looks at you disdainfully.")

                print("Maybe he doesn't like girdles.")

                print("He reveals that he was Lord Bertilak all along.")

                print("He scorns you for trying to get out of the deal with a woman's garment.")

                print("Especially since it was going to protect you anyways.")

                print("Was this really your last resort?")

                print("Next time, don't try to be different.")

                print("He lets you go.")

                print(text_divider)

                ending = "truce"



async def scene_five():

    global playing, ending 

    print(" ")

    print(text_divider)

    print(" ")

    print("FITT V")

    print(" ")

    print(text_divider)

    print("It's been a long journey, but you've made it home.")

    print("You approach the doors of Camelot.")

    print("It's time to return to the table.")

    print(text_divider)
 
    print(r"""
    
                                     {} {}
                             !  !  ! II II !  !  !
                          !  I__I__I_II II_I__I__I  !
                         I_/ |__|__|_|| ||_|__|__|\_I    
           .--.        I//|  |  |  | || || |  |  |  |\\I        .--.
          /-   \    ! /|/ |  |  |  | || || |  |  |  | \|\ !    /=   \
          \=__ /    I//|  |  |  |  | || || |  |  |  |  |\\I    \-__ /
           }  {  ! /|/ |  |  |  |  | || || |  |  |  |  | \|\ !  }  {
          {____} I//|  |  |  |  |  | || || |  |  |  |  |  |\\I {____}
    _!__!__|= |=/|/ |  |  |  |  |  | || || |  |  |  |  |  | \|\=|  |__!__!_
    _I__I__|  ||/|__|__|__|__|__|__|_|| ||_|__|__|__|__|__|__|\||- |__I__I_
    -|--|--|- ||-|--|--|--|--|--|--|-|| ||-|--|--|--|--|--|--|-||= |--|--|-
     |  |  |- || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||= |  |  |
     |  |  |- || |  |  |  |  |  |  | || || |  |  |  |  |  |  | ||- |  |  | 
    _|__|__|  ||_|__|__|__|__|__|__|_|| ||_|__|__|__|__|__|__|_||  |__|__|_
    -|--|--|= ||-|--|--|--|--|--|--|-|| ||-|--|--|--|--|--|--|-||- |--|--|-
    -|--|--|| |  |  |  |  |  |  |  | || || |  |  |  |  |  | || ||  |  | 
    ~~~~~~~~~~~^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^~~~~~~~~~~~

    """)

    print(text_divider)



    if ending == "fight":

        print(" ")

        print(text_divider)

        print(" ")

        print(" ✦ DISHONOR ENDING ✦ ")

        print(" ")

        print(text_divider)

        print("You tell the knights about your journey.")

        print("Well... most of it.")

        print("You try to leave out the part where you tried to attack the Green Knight.")

        print("Except, word travels fast.")

        print("Everyone already knows you broke your promise.")

        print("The knights shake their heads in disappointment.")

        print("Maybe you should've thought about what honor really means.")

        print("You can say bye to your reputation.")

        print("However little you had in the first place.")



    elif ending == "truce":

        print(" ")

        print(text_divider)

        print(" ")

        print(" ✦ COWARDLY ENDING ✦ ")

        print(" ")

        print(text_divider)

        print("You tell the knights how you escaped the Green Knight.")

        print("When they ask you how, you go silent.")

        print("The truth is going to come out one way or another.")

        print("You might as well confess what you did.")

        print("Soon, the entire round table is laughing at you.")

        print("They've never seen such a cowardly knight.")

        print("You've tarnished their reputation.")

        print("King Arthur pats you on the shoulder.")

        print("He tells you to just sit there quietly next time.")


    elif ending == "bravery":

        print(" ")

        print(text_divider)

        print(" ")

        print(" ✦ HONOR ENDING ✦ ")

        print(" ")

        print(text_divider)

        print("The knights are proud to hear that you faced the Green Knight.")

        print("You show everyone the magical green girdle.")

        print("Maybe green is your color after all.")

        print("King Arthur congratulates you on your bravery.")

        print("The knights cheer.")

        print("For once, you actually feel worthy of the round table.")

        print("Seems like doing the right thing paid off.")

        print("Congratulations! You've proven yourself to be an honorable knight.")



    elif ending == "bravery_sword_one":

        print(" ")

        print(text_divider)

        print(" ")

        print(" ✦ KINDNESS ENDING ✦ ")

        print(" ")

        print(text_divider)

        print("The knights notice that your hair looks a little different.")

        print("You tell them about the Green Knight, the axe, and the little fox.")

        print("They can hardly believe your story.")

        print("You gave away your last piece of food to a random animal.")

        print("And somehow, that animal ended up saving your life.")

        print("Who would've thought?")

        print("King Arthur praises you for your kindness and bravery.")

        print("That fox wasn't so useless after all.")

        print("The hair will grow back. You're proud.")

        print("Your kindness has been rewarded.")



    elif ending == "bravery_sword_two":

        print(" ")

        print(text_divider)

        print(" ")

        print(" ✦ INJURY ENDING ✦ ")

        print(" ")

        print(text_divider)

        print("You explain what happened at the Green Chapel.")

        print("Everyone looks horrified.")

        print("King Arthur congratulates you for keeping your promise.")

        print("But he reminds you to be kind and respectful.")

        print("You think back to the hungry fox in the forest.")

        print("Maybe you should've given him that food.")

        print("And maybe demanding dinner from your hosts wasn't the best idea.")

        print("You survived the Green Knight's game.")

        print("But you'll have to live with the consequences of your choices.")

        print("You've single-handedly (ha ha ha) embarrassed the knights.")



    print(text_divider)

    print("GAME OVER")

    print(text_divider)



while playing:

    await scene_one()

    if not playing:

        break



    await press_enter()



    await scene_two()

    if not playing:

            break

    await press_enter()



    await scene_three()

    if not playing:

            break



    await press_enter()



    await scene_four()

    if not playing:

            break



    await press_enter()



    await scene_five()



    playing = False



#!/usr/bin/python
#coding:utf-8
# an object describing our player
player = { 
    "name": "p1", 
    "gender": "g1",
    "pathway": "p1",
    "secretman": "s1",
    "treasure":["t1"]
}

treasure = {
    "treasure1" : "Fancy Coxntroller",
    "treasure2" : ["Arduino Tutorial", "Secret Sensors"],
    "treasure3" : "Mooncake"
}

wrongfood = {
    "wrongfood":"wrongfood"
}

collaboration = {
    "findtreasure": "findtreasure"
}

driver = {
    "driver": "driver"
}

import random # random numbers
import sys # system stuff for exiting

'''def rollDice(minNum, maxNum, difficulty):
    # any time a chance of something might happen, let's roll a die
    result = random.randint(minNum,maxNum)
    print "You roll a: " + str(result) + " out of " + str(maxNum)

    if result <= difficulty:
        print "trying again...."
        
        raw_input("press enter >")
        rollDice(minNum, maxNum, difficulty)

    return result'''

def printGraphic(name):
   if (name == "title"):         
        print '                                                                                                                                                   '
        print '     _______  ______    _______  _______  _______  __   __  ______    _______       __   __  __   __  __    _  _______  ___   __    _  _______     '
        print '    |       ||    _ |  |       ||   _   ||       ||  | |  ||    _ |  |       |     |  | |  ||  | |  ||  |  | ||       ||   | |  |  | ||       |    '
        print '    |_     _||   | ||  |    ___||  |_|  ||  _____||  | |  ||   | ||  |    ___|     |  |_|  ||  | |  ||   |_| ||_     _||   | |   |_| ||    ___|    '
        print '      |   |  |   |_||_ |   |___ |       || |_____ |  |_|  ||   |_||_ |   |___      |       ||  |_|  ||       |  |   |  |   | |       ||   | __     '
        print '      |   |  |    __  ||    ___||       ||_____  ||       ||    __  ||    ___|     |       ||       ||  _    |  |   |  |   | |  _    ||   ||  |    '
        print '      |   |  |   |  | ||   |___ |   _   | _____| ||       ||   |  | ||   |___      |   _   ||       || | |   |  |   |  |   | | | |   ||   |_| |    '
        print '      |___|  |___|  |_||_______||__| |__||_______||_______||___|  |_||_______|     |__| |__||_______||_|  |__|  |___|  |___| |_|  |__||_______|    '
        print '                                                                                                                                                   '                                                                                                                                                          
                                                                                                                                                                 
   if (name == "strongman"):
        print "                                               "    
        print "                    ,#####,                    "    
        print "                    #_   _#                    "    
        print "                    |a` `a|                    "    
        print "                    |  u  |                    "    
        print "                    \  =  /                    "    
        print "                    |\___/|                    "    
        print "           ___ ____/:     :\____ ___           "   
        print "         .'   `.-===-    /-===-.`   '.         "   
        print "        /      .-'''''-.-'''''-.      |        "    
        print "       /'             =:=             '|       "     
        print "     .'  ' .:    o   -=:=-   o    :. '  `.     "
        print "     (.'   /'. '-.....-'-.....-' .'    '.）    "
        print "     /' ._/   '.     --:--     .'   、_. '|    "
        print "    |  .'|      '.  ---:---  .'      |'.  |    "
        print "    |  : |       |  ---:---  |       | :  |    "
        print "     \ : |       |_____._____|       | : /     "
        print "     /   (       |----|------|       )   |     "
        print "    /... .|      |    |      |      |. ...|    "
        print "   |::::/''     /     |       \     ''|::::|   "
        print "   '""""       /'    .L_      `\       """"'   "     
        print "              /'-.,__/` `、__..-'\             "     
        print "             ;      /     \      ;             "     
        print "             :     /       \     |             "     
        print "             |    /         \.   |             "     
        print "             |`../           |  ,/             "     
        print "             ( _ )           |  _)             "     
        print "             |   |           |   |             "     
        print "             |___|           \___|             "     
        print "              \  /            |__|             "     
        print "              |oo|           \__.//___)        "     
        print "              |==|                             "     
        print "              \__/                             "     

   if(name == "sunglassesman"):
        print '       .------\ /------.      '
        print '       |       -       |      '
        print '       |               |      '
        print '       |               |      '
        print '       |               |      '
        print '    _______________________   '
        print '    ===========.===========   '
        print '      / ~~~~~     ~~~~~ \     '
        print '     / |####|     |####| \          '
        print '     W  ----  / \  ----  W    '
        print '     \.      |o o|      ./    '
        print '      |                 |     '
        print '      \    #########    /     '
        print '       \  ## ----- ##  /      '
        print '        \##         ##/       '
        print '         \_____v_____/        '

   if(name == "gameover"):
        print '                                                                                     '
        print '     _______  _______  __   __  _______    _______  __   __  _______  ______         '
        print '    |       ||   _   ||  |_|  ||       |  |       ||  | |  ||       ||    _ |        '
        print '    |    ___||  |_|  ||       ||    ___|  |   _   ||  |_|  ||    ___||   | ||        '
        print '    |   | __ |       ||       ||   |___   |  | |  ||       ||   |___ |   |_||_       '
        print '    |   ||  ||       ||       ||    ___|  |  |_|  ||       ||    ___||    __  |      '
        print '    |   |_| ||   _   || ||_|| ||   |___   |       | |     | |   |___ |   |  | |      '
        print '    |_______||__| |__||_|   |_||_______|  |_______|  |___|  |_______||___|  |_|      '
        print '                                                                                     '

   if(name == "congratulations"):
        print'     _______  _______  __    _  _______  ______    _______  _______  __   __  ___      _______  _______  ___   _______  __    _  _______  __      '
        print'    |       ||       ||  |  | ||       ||    _ |  |   _   ||       ||  | |  ||   |    |   _   ||       ||   | |       ||  |  | ||       ||  |     '
        print'    |     __||   _   ||   |_| ||    ___||   | ||  |  |_|  ||_     _||  | |  ||   |    |  |_|  ||_     _||   | |   _   ||   |_| ||  _____||  |     '
        print'    |    |   |  | |  ||       ||   | __ |   |_||_ |       |  |   |  |  |_|  ||   |    |       |  |   |  |   | |  | |  ||       || |_____ |  |     '
        print'    |    |__ |  |_|  ||  _    ||   ||  ||    __  ||       |  |   |  |       ||   |___ |       |  |   |  |   | |  |_|  ||  _    ||_____  ||__|     '
        print'    |       ||       || | |   ||   |_| ||   |  | ||   _   |  |   |  |       ||       ||   _   |  |   |  |   | |       || | |   | _____| | __      '
        print'    |_______||_______||_|  |__||_______||___|  |_||__| |__|  |___|  |_______||_______||__| |__|  |___|  |___| |_______||_|  |__||_______||__|     '
        print'                                                                                                                                                  '

def gameOver():
    raw_input("< press enter to continue >")
    print " "
    if(player["gender"] == "Male"):
        print "GG, Good Game, boy"
    elif(player["gender"] == "Female"):
        print "GG, Good Game, girl"
    print " "
    printGraphic("gameover")
    print "-------------------------------"
    print "To be continued!"
    print "Name: " + player["name"]
    print "Gender: " + player["gender"]
    print " "
    raw_input("< press to restart >")
    print " "
    main()

def GameOver1():
    print "You cannot find a treasure in your home!"
    print " "
    gameOver()

def GameOver2():
    print "When you get to the studio, you notice that you are already late for the Code Literacy class and Bruno said"
    print "'Hey you are late. Did you do your assignment by the way? Show us your assignment'"
    print "You open the terminal and file Treasure_Hunting.py, then some words come into your eyes"
    print " "
    raw_input("< press enter to continue >")
    print " "
    introStoryAgain()

def EatWrongFood():
    print "Didn't your mom tell you that it's dangerous to eat food from people that you do not know?"
    print "You feel blackout for a long time. When you wake up, you realized that you are in the SVA IxD studio and Bruno said to you"
    print "'Your assignment is very interesting, that being said taht you can skip the class and go to museum'"
    print "'Then get a " + wrongfood["wrongfood"] + " and feel blackout, it just looks like what happened to you now'"
    print "You say, 'No, I'm just a little tired.'"
    print "'Ok then, let's continue.' Bruno said."
    print "'Ok' You don't know what happened and then lick out the leftover of " + wrongfood["wrongfood"] + " at the corner of your mouth and continue to listen the class."
    print " "
    gameOver()

def congratulations():
    raw_input("< press enter to continue >")
    print " "
    print "----------------------------------------------"
    print "Congratulations! You get the treasure finally!"
    print "----------------------------------------------"
    print " "
    printGraphic("congratulations")
    print " "
    print "-------------------------------"
    print "Here are your info"
    print "Name: " + player["name"]
    print "Gender: " + player["gender"]
    print "Pathway: " + player["pathway"]
    print "Secretman you met: " + player["secretman"]
    if(player["secretman"] == "Bruno" or player["secretman"] == "Yohe"):
        print "Treasure you got: " + player["treasure"][0]
    elif (player["secretman"] == "Eric" and collaboration["findtreasure"] == "1"):
        print "Treasure you got: " + player["treasure"][0] + " & " + player["treasure"][1]
    elif (player["secretman"] == "Eric" and collaboration["findtreasure"] == "2"):
        print "Treasure you got: " + player["treasure"][0]
    print " "
    raw_input("< press enter to Exit >")
    return

def EricAndArduino():
    print "Wow! It is a photoresistor inside of the Starry Night's moon, and Arduino makes the painting moved."
    print "Behind the painting, you find your treasure, it is a book of Arduino Tutorial!"
    print "Then there is a man who is coming to you, it is the man that you met at the beginning!"
    print "Then the man wears off the sunglasses, it is Eric! OMG!"
    if (collaboration["findtreasure"] == "1"):
        print "And he said, now you get secret sensors and Arduino tutorial, let's do the assignment better!"
    elif (collaboration["findtreasure"] == "2"):
        print "And he said, now you get the Arduino tutorial, let's do the assignment better!"
    player["pathway"] = "MoMA"
    player["secretman"] = "Eric"
    if(collaboration["findtreasure"] == "1"):
        player["treasure"][0] = "Secret Sensors"
        player["treasure"].append("Arduino Tutorial")
    elif(collaboration["findtreasure"] == "2"):
        player["treasure"][0] = "Arduino Tutorial"
    print " "
    congratulations()

def BrunoAndFancyController():
    print "There is a hole on the wall and it is very late, so that it can shed a moonlight on the other side of the wall"
    print "And you see there is something in the lightened area."
    print "It is a fluorescent word, 'Turn back'"
    print " "
    raw_input("< press enter to continue >")
    print " "
    print "And when you turn back, you find that sunglasses man you met at the beginning standing behind you just now!"
    print "Then he wears off the sunglasses, it is Bruno! OMG!"
    if (driver["driver"] == "3"):
        print "And the sunglasses became back to a metal, he is that driver!" # post-credits scene
    print " "
    raw_input("< press enter to continue >")
    print " "
    print "He gives his Fancy Controller to you and said"
    print "'How could you stay in a toilet so long? That's awesome.'"
    print "'Here is a Fancy Controller, and you can play around it using your laptop, the world colored for you.'"
    player["pathway"] = "Metropolitan Museum"
    player["secretman"] = "Bruno"
    player["treasure"][0] = "Fancy Controller"
    print " "
    congratulations()

def MoMath():
    print "You decide to walk to the National Museum of Mathematics since it is right next to the Madison Square Park"
    print "On the way to the museum, you are hungry and you find the fact that the Shack Shack is right over there."
    print "Do you want to get a burger?"
    print "1. Yes, I would like to get a Shake Shack Burger."
    print "2. No, I don't like a Shaskr Shack Burger so I will just go to the museum right away."
    print " "
    hamburger = raw_input("please choose the number >")
    print " "
    if (hamburger == "1"):
        print "Which burger you want to get?"
        print "1. A Shake Shack Burger"
        print "2. A Mushroom Burger"
        print " "
        whichhamburger = raw_input("please choose the number >")
        print " "
        print "After you get the burger, you head to the museum."
    elif (hamburger == "2"):
        print "You head to the museum right away."
    print "When you arrive at the museum, you see the 'Shapes of Space'"
    print "And fit together shapes on differently curved surfaces and observe the differences among them."
    print "While you are trying to fit together, you just meet a guy who wears a sunglasses."
    print "You figured that you met him before! The man wear off the sunglasses, it is Yohe! OMG!"
    print "And he said, 'now you get the treasure, the mooncake'"
    player["pathway"] = "National Museum of Mathematics"
    player["secretman"] = "Yohe"
    player["treasure"][0] = "Mooncake"
    print " "
    congratulations()

def MoMath2():
    print "Do you want to get a burger?"
    print "1. Yes, I would like to get a Shake Shack Burger."
    print "2. No, I don't like a Shake Shack Burger so I will just go to the museum right away."
    print " "
    hamburger = raw_input("please choose the number >")
    print " "
    if (hamburger == "1"):
        print "Which burger you want to get?"
        print "1. A Shake Shack Burger"
        print "2. A Mushroom Burger"
        print " "
        whichhamburger = raw_input("please choose the number >")
        print " "
        print "After you get the burger, you head to the museum."
    elif (hamburger == "2"):
        print "You head to the museum right away."
    print "When you arrive at the museum, you see the 'Shapes of Space'"
    print "And fit together shapes on differently curved surfaces and observe the differences among them."
    print "While you are trying to fit together, you just meet a guy who wears a sunglasses."
    print "You figured that you met him before! The man wear off the sunglasses, it is Yohe! OMG!"
    print "And he said, 'now you get the treasure, the mooncake'"
    player["pathway"] = "National Museum of Mathematics"
    player["secretman"] = "Yohe"
    player["treasure"][0] = "Mooncake"
    print " "
    congratulations()

def MoMA():
    print "You decide to go to the MoMA and ride a Citi Bike to get to the MoMA"
    print "Then you go to the MOMA right away"
    print "When you arrived, there is a stanger who gives you a lollipop, do you want one?"
    print "1. Yes"
    print "2. No"
    print " "
    lollipop = raw_input("please choose the number >")
    print " "
    if (lollipop == "1"):
        wrongfood["wrongfood"] = "lollipop"
        print " "
        EatWrongFood()
    elif (lollipop == "2"):
        print "'Really? that's awesome, it is made by raw chocolate, are you sure that you don't want to try it out?'"
        print "1. No, bye"
        print "2. Really? It heard nice, let me try it"
        print ""
        lollipop2 = raw_input("please choose the number >")
        print " "
        if (lollipop2 == "1"):
            print "The woman shakes her head and say, 'you are not lucky.' Then eat it herself."
            print "You keep going and enter into the painting and sculpture department in floor five."
            print "You saw Sofia! She is looking at a dancing mommy with full interest."
            print "What would you do?"
            print "1. Join her and see what will happens."
            print "2. To find the your treasure first"
            print ""
            collaboration["findtreasure"] = raw_input("please choose the number >")
            print " "
            if (collaboration["findtreasure"] == "1"):
                print "When mommy ends its dancing, he takes an arduino kits out and give to you and Sofia."
                print "The mommy said it contains a lot of precious sensors that cannot be bought outside."
                print "Such as mystery sensor that can detect others' curiosity and you can see their story in Serial.Port(9600),"
                print "Also cooking sensor that can detect if food is delicious and send microwave to make it yummy."
                print "Then you tells the story about treasure hunting and the sunglasses man you met to Sofia"
                print "And she said she also met that one with sunglasses and also follow its instruction to this museum"
                print "Then she watches mommy dancing in terms of clues in map"
                print " "
                raw_input("< press enter to continue >")
                print " "
                print "You and Sofia follow the treasure mark in your hand and then stand in front of the painting of Starry Night of Van Gogh."
                print "Is thre the treasure?"
                print "What would you do?"
                print "1. Use the painting brush draw the moon more bright"
                print "2. Use flashlight to lighten the moon of the paint"
                print "3. Eat the mooncake which is right next to the painting"
                print " "
                StarryNight = raw_input("please choose the number >")
                print " "
                if (StarryNight == "1"):
                    print "There are some strong men entered into the room and carry you away as if you are a little bunny."
                    print " "
                    printGraphic("strongman")
                    print " "
                    gameOver()
                elif (StarryNight == "2"):
                    print " "
                    EricAndArduino()
                elif (StarryNight == "3"):
                    wrongfood["wrongfood"] = "Mooncake"
                    print " "
                    EatWrongFood()
            elif (collaboration["findtreasure"] == "2"):
                print "You follow the treasure mark in your hand and then stand in front of the painting of Starry Night of Van Gogh."
                print "Is the treasure here?"
                print "What would you do?"
                print "1. Use the painting brush draw the moon more bright"
                print "2. Use flashlight to lighten the moon of the paint"
                print "3. Eat the mooncake which is right next to the painting"
                print " "
                StarryNight = raw_input("please choose the number >")
                print " "
                if (StarryNight == "1"):
                    print "There are some strong men entered into the room and carry you away as if you are a little bunny."
                    print " "
                    printGraphic("strongman")
                    print " "
                    gameOver()
                elif (StarryNight == "2"):
                    print " "
                    EricAndArduino()
                elif (StarryNight == "3"):
                    wrongfood["wrongfood"] = "Mooncake"
                    print " "
                    EatWrongFood()
        elif (lollipop2 == "2"):
            wrongfood["wrongfood"] = "lollipop"
            print " "
            EatWrongFood()

def EnterToilet():
    if (player["gender"] == "Male"):
        print "When you enter in, a woman sees you frightenedly and then runs out with scream."
    elif (player["gender"] == "Female"):
        print "When you enter in, a man sees you frightenedly and then runs out quickly."
        print "You try to make yourself looks decent, and then open the lid of the toilet following the instruction of the map."
    print "Then you find a waterproof script with words, 'Go gentle into that good night, the truth is hidden inside the moonlight'"
    print "What would you do then?"
    print "1. Just wait a while to see what happened"
    print "2. What's the hell? It is totally a trick, I'm going to studio."
    print " "
    wait1 = raw_input("please choose the number >")
    print " "
    if (wait1 == "1"):
        print "Nothing happened, still wait?"
        print "1. Still wait"
        print "2. No, I'm hungry, I want to go home for dinner."
        print " "
        wait2 = raw_input("please choose the number >")
        print " "
        if (wait2 == "1"):
            print "Nothing happened, still wait?"
            print "1. Still wait"
            print "2. It's too late, the subway might be off-the-line, I need to go home soon."
            print " "
            wait3 = raw_input("please choose the number >")
            print " "
            if (wait3 == "1"):
                print "Nothing happened, it's 11:30 pm yet. Do you want to sleep here or go home now?"
                print "1. Keep calm and carry on waiting"
                print "2. Bye, I miss my bed"
                print " "
                wait4 = raw_input("please choose the number >")
                print " "
                if (wait4 == "1"):
                    print " "
                    BrunoAndFancyController()
                elif (wait4 == "2"):
                    print " "
                    GameOver1()
            elif (wait3 == "2"):
                print " "
                GameOver1()
        elif (wait2 == "2"):
            print " "
            GameOver1()
    elif (wait1 == "2"):
        print " "
        GameOver2() 

def MetroComes():
    print "Oh, Metro comes, you get off and enter into the museum."
    print "You follows the route in the map, and then find the place of treasure mark in the Metro."

    if (player["gender"] == "Male"):
        print "There is a lady's toilet! Would you enter into?"
    elif (player["gender"] == "Female"):
        print "There is a man's toilet! Would you enter into?"
    print "1. Enter into the wrong toilet"
    print "2. It's too embarrased, I don't want to try, I wanna go to studio"
    print " "
    toilet = raw_input("please choose the number >")
    print " "
    if (toilet == "1"):
        print " "
        EnterToilet()
    if (toilet == "2"):
        print " "
        GameOver2()

def Shapes():
    print "No, the driver smiles secretly and let you try again"
    print " "
    print "1. Mirror"
    print "2. Statue"
    print "3. Sunglasses"
    print " "
    shape = raw_input("please choose the number >")
    print " "

    if (shape == "1"):
        print " "
        Shapes()
    elif (shape == "2"):
        print " "
        Shapes()
    elif (shape == "3"):
        print "'Exactly! we made it a pair of Sunglasses that can be worn with space suit, and then took a photo'"
        print " "
        MetroComes()

def Metro():
    print "You decide to go to Metropolitan Museum and take a Uber"
    print "When you get on the car, you find the driver is so talktive"
    print "What would you do?"
    print " "
    print "1. Let the driver shut up"
    print "2. 'I'm sorry I cannot speak english well'"
    print "3. Happily talk with the driver"
    print " "
    driver["driver"] = raw_input("please choose the number >")
    print " "

    if (driver["driver"] == "1"):
        print "Driver stop the car and let you get out, you show the middle finger to the driver and get off the Uber'"
        print "Then you find you are just at the front of the National Museum of Mathematics!"
        print "What would you do?"
        print " "
        print "1. Go National Museum of Mathematics"
        print "2. 'Damn!' You are toally upset and just go home"
        print " "
        GetOffUber = raw_input("please choose the number >")
        print " "
        
        if(GetOffUber == "1"):
            print "You decide to enter into the National Museum of Mathematics, but you are hungry"
            print "Then you find the fact that the Shack Shack is right over there"
            print " "
            MoMath2()
        elif (GetOffUber == "2"):
            print " "
            GameOver1()
    elif (driver["driver"] == "2"):
        print "You two keep silent all the way, and then Metro comes."
        print " "
        MetroComes()
    elif (driver["driver"] == "3"):
        print "From his story, you know he is the one who takes the moon trip of SpaceX by Elon Musk"
        print "They discovered a very strange metal, and this metal can change shape, and he asks"
        print "'What kind of shapes you think we let it be?'"
        print " "
        print "1. Mirror"
        print "2. Statue"
        print "3. Sunglasses"
        print " "
        shape = raw_input("please choose the number >")
        print " "

        if (shape == "1"):
            print " "
            Shapes()
        elif (shape == "2"):
            print " "
            Shapes()
        elif (shape == "3"):
            print "'Exactly! we made it a pair of Sunglasses that can be worn with space suit, and then took a photo'"
            print " "
            MetroComes()

def museums():
    print "He tells you there are three different treasures in three museums, but you can only choose one,"
    print "Which museum would you choose to go?"
    print " "
    print "1. Metro (Metropolitan Museum)"
    print "2. MoMA (Museum of Modern Art)"
    print "3. MoMath (National Museum of Mathematics)"
    print " "
    Museum = raw_input("please choose the number >")
    
    if (Museum == "1"):
        print " "
        Metro()
    elif (Museum == "2"):
        print " "
        MoMA()
    elif (Museum == "3"):
        print " "
        MoMath()


def introStoryAgain():
    print "One day, You are on the way to the SVA IxD studio"
    print "You meet a person with the sunglasses and the tile hat in the Madison Square Park."
    print " "
    raw_input("< press enter to continue>")
    print " "
    printGraphic("sunglassesman")
    print " "
    print "He passes by and gives you an elaborate book"
    print "Then he whispers a secret of treasure hunting"
    print "---------------------------------------------------------------------------"
    print "'Go gentle into that good night, the truth is hidden inside the moonlight.'"
    print "---------------------------------------------------------------------------"
    print "What would you do?"
    print "1. Believe him and go to find treasure in museums."
    print "2. Ignore him and go straight to studio."
    print "3. Give him some money."
    print " "
    pathway = raw_input("please choose the number >")
    print " "
    # the player can choose the number
    if (pathway == "1"):
        print " "
        museums()
    elif(pathway == "2"):
        print "When you get studio, the class Code Literacy begins and Bruno said"
        print "'Hey How about your assignment?'"
        print "You open the terminal and file Treasure_Hunting.py, then some words come into your eyes"
        print " "
        raw_input("< press enter to continue >")
        print " "
        introStoryAgain()
    elif(pathway == "3"):
        print "He rejected it and show you a middle finger, then fade away in the crowd. And you then go to studio."
        print " "
        raw_input("< press enter to continue >")
        print " "
        print "When you get studio, the class Code Literacy begins and Bruno said"
        print "'Hey How about your assignment?'"
        print "You open the terminal and file Treasure_Hunting.py, then some words come into your eyes"
        print " "
        raw_input("< press enter to continue >")
        print " "
        introStoryAgain() # repeat over and over until the player chooses yes!

def introStory():
    # let's introduce them to our world
    print "Welcom to the Treasure Hunting! How would you like me to call you?"
    print " "
    player["name"] = raw_input("Please enter your prefered name >")
    print " "
    print "Ok! What's your gender?"
    print "1. Male"
    print "2. Female"
    print " "
    gender = raw_input("Please choose the number >")
    print " "
    if (gender == "1"): 
        player["gender"] = "Male"
    elif (gender == "2"): 
        player["gender"] = "Female"
    # intro story, quick and dirty (think star wars style)
    print " "
    print "Good to see you again! " + player["name"] + "!"
    print "The story so far..."
    print "--------------------------------------------------"
    print "One day, You are on the way to the SVA IxD studio"
    print "You meet a person with the sunglasses and tile hat in the Madison Square Park."
    print " "
    raw_input("< press enter to continue >")
    print " "
    printGraphic("sunglassesman")
    print " "
    print "He passes by and gives you an elaborate book"
    print "Then he whispers a secret of treasure hunting"
    print "---------------------------------------------------------------------------"
    print "'Go gentle into that good night, the truth is hidden inside the moonlight.'"
    print "---------------------------------------------------------------------------"
    print "What would you do?"
    print "1. Believe him and go to find treasure in museums."
    print "2. Ignore him and go straight to studio."
    print "3. Give him some money."
    print " "
    pathway = raw_input("please choose the number >")
    print " "

    # the player can choose the number
    if (pathway == "1"):
        print "He tells you there are three different treasures in three museums, but you can only choose one,"
        museums()
    elif(pathway == "2"):
        print "When you get studio, the class Code Literacy begins and Bruno said"
        print "'Hey How about your assignment?'"
        print "You open the terminal and file Treasure_Hunting.py, then some words come into your eyes"
        print " "
        raw_input("< press enter to continue >")
        print " "
        introStoryAgain()
    elif(pathway == "3"):
        print "He rejected it and show you a middle finger, then fade away in the crowd. And you then go to studio."
        print " "
        raw_input("< press enter to continue >")
        print " "
        print "When you get studio, the class Code Literacy begins and Bruno said"
        print "'Hey How about your assignment?'"
        print "You open the terminal and file Treasure_Hunting.py, then some words come into your eyes"
        print " "
        raw_input("< press enter to continue >")
        print " "
        introStoryAgain() # repeat over and over until the player chooses yes!



# main! most programs start with this.
def main():
    printGraphic("title") # call the function to print an image
    print " "
    print " "
    print "-------------Please Max Your Window to Play the Game-------------"
    print " "
    print " "
    raw_input("< press enter to continue >")
    print " "
    introStory() # start the intro

main() # this is the first thing that happens
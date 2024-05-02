play = input("Welcome to the Rezzgarden markets!\n a cool text adventure would you like to play? y/n ")
while play == "y": #im going to have to nest these fuckers for awhile i want to start with 6 (for now) scenarios
                   # then have them all kind of come to their own narrative end
    print("The bustling market is a smorgasboard of chirps and gutteral growls")
    print("All the species of the systems come here to bargain and find elusive deals")
    answer1 = int(input("You start to feel hungry do you:\n 1.Grab a bite to eat at Squanch Eatery  2.Ignore it and continue formatting your data stick\n Make choice:"))
    if answer1 == 1:
        answer2 = int(input('A portly Yorlork male covered in grease waves his tentacles in anticipation as your hungry eyes\n glaze over the wide assortment of delicacies\n 1. Squiddo Sticks 2. Yorbol Liver Pie'))
        if answer2 == 1:

            answer4 = int(input('Squiddo for the kiddo eh?" says a blonde man wearing a monolense i.d decoder \n"you got the palate of a wee baby yeh?" He presses a lasgun deep into your side you feel the ionic coils sizzle on your bare flesh\n "Alright i know why your here kiddo move slowly into my hoverloader nice and easy\n 1.Go with the strange man 2.Attempt to fight your way out'))
            if answer4 == 1:
                print("He escorts you to the hoverloader and an associate blindfolds you gags you and shoves you in the back. looks like you got caught GAME OVER")
                quit()
            elif answer4 == 2:
                print("You whip lightning fast disable the mans wrist. He pulls out a knife to attack \nbut the Yorlork restaurant owner pulls out a rifle and kills both of you. \nIts wrong to start violence in a place of buisness GAME OVER")
            quit()

        elif answer2 ==2:
            answer3 = int(input('"Ah a good choice." Says a scruffy woman "you must be from offworld with such exotic tastes"\n1.Im a spacer 2.Nope ive lived in the Rezz my whole life'))
            if answer3 == 1:
                print("The woman gives you her ship for you guys to get married and have an exotic honey moon GAME OVER")
            if answer3 == 2:
                print("you fall in love and buy a house together in the rezz garden and you give up your bounty hunting ways GAME OVER")
                quit()
    elif answer1 == 2:
        answer5 = int(input("Your data stick chirps and buzzes it seems you figured out the logic of your virus and finally built the penetration tester\n 1. Use your datastick to hack into SeaSystems user database 2. Mill around and check your brain mail "))
        if answer5 == 1:
            answer6 = int(input("You comb through the data and find Karlboro Skarsgaards genetic profile is online. That means hes in the building you think to yourself\n 1. Crash through SeaSystems 2nd floor with your mobility boots and eliminate karlboro 2. use your pen tester to pass security to pretend be an employee and sneakily make your way up the stairwell"))
            if answer6 == 1:
                    print("You violently burst through the window throw explosives kill multiple employees and poison dart karlboro right in the neck. However the police are on their way YOU WIN...? TO BE CONTINUED")
                    quit()
            elif answer6 == 2:
                    print("You sneak past security but karen from marketing asks if you could work on some projects you begin working on them and despite breaking in they decide to hire you. You have dental insurance now and are happy with your work GAME OVER")
        elif answer5==2:
            answer7 = int(input("you get bombarded by thought prompts INCREASE THE SIZE OF YOUR PLEASURE ROD 1.Think yes to buy 2.Quit program"))
        if answer7 == 1:


            print("Wow you think to yourself ITS ALWAYS BEEN REAL your weiner inflates to a gargantuan proportion Congratulations who needs to be a cool sci fi bounty hunter when you have got a huge Schlong. GAME OVER")
            quit()
        if answer7 == 2:
            print("The amount of unchecked brainmails in your file zipping through your brain so fast gives you Deep psychological damage")
            print("The thought police find your location and forcefully take you to the Wellness Psychiatric Centre on the moon Get well soon! GAME OVER")
            quit()
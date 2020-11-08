import sys,getopt,Character,Game
if __name__ == '__main__':
    argument_list = sys.argv[1:]
    short_options = "p:s:"
    long_options = ["players=", "stages="]
    try:
        arguments, values = getopt.getopt(argument_list, short_options, long_options)
    except getopt.error as err:
        print(str(err))
        sys.exit(1)
    numPlayers = 1
    numStages = 1
    error = False
    for current_argument, current_value in arguments:
        try:
            int(current_value)
            if current_argument in ("-p", "--players"):
                if((((int(current_value))<=4)and(int(current_value))>=1)):
                    numPlayers = int(current_value)
                else:
                    print("The number of players must be between 1 and 4.",end=" ")
                    error = True
            elif current_argument in ("-s", "--stages"):
                if ((((int(current_value)) <= 10) and (int(current_value)) >= 1)):
                    numStages = int(current_value)
                else:
                    print("The number of stages must be between 1 and 10.", end=" ")
                    error = True
        except:
            print("Debe escribir números enteros")
            sys.exit(2)
    if error:
        print("Finishing program.")
        sys.exit(2)
    print(("A game with %s stage(s) will be set for %s player(s)") % (numStages,numPlayers))
    print("***********      AVAILABLE CHARACTERS        ***********")
    print("1.-",end=" ")
    Character.Character.Bookworn.printInfo(self=Character)
    print("2.-", end=" ")
    Character.Character.Worker.printInfo(self=Character)
    print("3.-", end=" ")
    Character.Character.Whatsapper.printInfo(self=Character)
    print("4.-", end=" ")
    Character.Character.Procrastinator.printInfo(self=Character)
    userCharacters = []
    for i in range(numPlayers):
        print("Player",i+1,". Please, choose a character (1-4): ",end="")
        option = input()
        if (option=="1"):
            character = Character.Character.Bookworn()
            character.player = i+1
            userCharacters.append(character)
        elif (option=="2"):
            character = Character.Character.Worker()
            character.player = i + 1
            userCharacters.append(character)
        elif (option=="3"):
            character = Character.Character.Whatsapper()
            character.player = i + 1
            userCharacters.append(character)
        elif (option=="4"):
            character = Character.Character.Procrastinator()
            character.player = i + 1
            userCharacters.append(character)
        else: print("That option does not exist")
    if (len(userCharacters) >1):
        print("********************************************************")
        i = 1
        for character in userCharacters:
            print(i,end=".- ")
            i+=1
            character.printInfo()
        print("********************************************************")
    Game.Game.executeStage(self=Game.Game,numStages=numStages,characters=userCharacters)








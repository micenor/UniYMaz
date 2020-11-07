import Enemy,time,sys,Character,math
from random import choice,randrange
class Game():
    def executeStage(self, numStages,characters):
        available_characters = [Character.Character.Bookworn,Character.Character.Worker,Character.Character.Whatsapper,Character.Character.Procrastinator]
        available_enemies = [Enemy.Enemy.Partial_Exam, Enemy.Enemy.Theoretical_Class, Enemy.Enemy.Teacher]
        alive_characters = characters
        for i in (range(1,numStages+1)):
            if (i == 4): available_enemies.append(Enemy.Enemy.Final_Exam)
            stage_enemies = []
            print("         ************************")
            print(("         *       STAGE %i       *") % i)
            print("         ************************")
            print("")
            print("         ---- CURRENT MONSTERS ----")
            print("    ++++++++++++++++++++++++++++++++++++++")
            for n in range(4):
                enemy = choice(available_enemies)
                stage_enemies.append(enemy())
                print(("    %s: Stats: %iHP and %iDMG") % (enemy.name, enemy.life, enemy.damage))
            print("    ++++++++++++++++++++++++++++++++++++++")
            while((len(stage_enemies)!=0) and (len(alive_characters)!=0)):
                print("    ------------------------")
                print("    -    PLAYERS TURN      -")
                print("    ------------------------")
                for character in alive_characters:
                    if(len(stage_enemies)!=0):
                        while True:
                            print(("%s (Player %i). What are you going to do? ((A)ttack/(S)kill)") % (character.name,character.player))
                            option = input().upper()
                            if ((option!="A") and (option!="S")):
                                print("That option does not exist, ((A)ttack/(S)kill)")
                            else: break
                        enemy_target = choice(stage_enemies)
                        if (option=="A"):
                            damage = randrange(character.damage + 1)
                            enemy_target.life = enemy_target.life - damage
                            print(("%s (Player %i) did %i damage to %s. %s has %iHP left. ") % (character.name, character.player,damage,enemy_target.name,enemy_target.name,enemy_target.life))
                            if (enemy_target.life<=0):
                                stage_enemies.remove(enemy_target)
                                print("The enemy has died.")
                if((len(stage_enemies)!=0)):
                    print("    ------------------------")
                    print("    -    MONSTERS TURN     -")
                    print("    ------------------------")
                    for enemy in stage_enemies:
                        if (len(alive_characters)!=0):
                            character_target = choice(alive_characters)
                            option = choice(["A"])
                            if (option == "A"):
                                damage = randrange(enemy.damage + 1)
                                character_target.life = character_target.life - damage
                                print(("%s did %i damage to Player %i (%s). Player %s has %iHP left.") % (enemy.name, damage, character_target.player, character_target.name,character_target.player, character_target.life))
                                if (character_target.life <= 0):
                                    alive_characters.remove(character_target)
                                    print(("Player %i has died") % character_target.player)
                        else:
                            break
            for character in alive_characters:
                for character_class in available_characters:
                    if ((character.__class__ == character_class)):
                        if ((character.life + (character_class.life/4)>=character_class.life)):
                            character.life = character_class.life
                            break
                        else:
                            character.life = math.ceil(character.life + character_class.life / 4)
                            break
            if(len(stage_enemies)==0): print("Stage clear, all enemies defeated")
            if(len(alive_characters)==0):
                print("All characters have been defeated. Try again.")
                sys.exit(2)
        print("All the stages have been cleared. You won the game!")
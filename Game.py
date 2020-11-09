from random import choice, randrange

import Enemy
import sys


class Game():
    characters_list=[]
    alive_characters=0
    stage_enemies = []
    round
    actual_stage=0
    def executeStage(self, numStages,characters):
        available_enemies = [Enemy.Enemy.Partial_Exam, Enemy.Enemy.Theoretical_Class, Enemy.Enemy.Teacher]
        self.characters_list = characters
        self.alive_characters= len(self.characters_list)
        for i in (range(1,numStages+1)):
            self.round = 0
            self.stage_enemies.clear()
            self.actual_stage=i
            if (i == 4): available_enemies.append(Enemy.Enemy.Final_Exam)
            print("         ************************")
            print(("         *       STAGE %i       *") % i)
            print("         ************************")
            print("")
            print("         ---- CURRENT MONSTERS ----")
            print("    ++++++++++++++++++++++++++++++++++++++")
            for n in range(4):
                enemy = choice(available_enemies)
                self.stage_enemies.append(enemy())
                print(("    %s: Stats: %iHP and %iDMG") % (enemy.name, enemy.life, enemy.damage))
            print("    ++++++++++++++++++++++++++++++++++++++")
            while((len([en for en in self.stage_enemies if en.life > 0])!=0) and (len([char for char in self.characters_list if char.life > 0]) != 0)):
                self.round += 1
                print("    ------------------------")
                print("    -    PLAYERS TURN      -")
                print("    ------------------------")
                for character in [char for char in self.characters_list if char.life > 0]:
                    if(len([en for en in self.stage_enemies if en.life > 0])!=0):
                        while True:
                            print(("%s (Player %i). What are you going to do? ((A)ttack/(S)kill)") % (character.name,character.player))
                            option = input().upper()
                            if ((option!="A") and (option!="S")):
                                print("That option does not exist, ((A)ttack/(S)kill)")
                            elif (option == "S") :
                                if character.ability(self):
                                    break
                            else: break
                        if (option=="A"):
                            character.attack(self)
                print("    ------------------------")
                print("    -    MONSTERS TURN     -")
                print("    ------------------------")
                for enemy in [en for en in self.stage_enemies if en.life > 0]:
                    if (len([character for character in self.characters_list if character.life > 0])!=0):
                       enemy.attack(self)
                    else:
                        break
#*****************************************End of round***************************************************
                for hero in [char for char in self.characters_list if char.life > 0]:
                    if hero.cooldown>0:
                        hero.cooldown-=1
#*****************************************End of stage***************************************************
            for character in [char for char in self.characters_list if char.life > 0]:
                character_class = character.__class__
                if ((character.life + (character_class.life/4)>=character_class.life)):
                    character.life = character_class.life
                else:
                    character.life = character.life + character_class.life / 4
                if character.name=="Procrastinator":
                    character.cooldown=0
            if(len([en for en in self.stage_enemies if en.life > 0])==0):
                print("Stage clear, all enemies defeated")
            else:
                print("All characters have been defeated. Try again.")
                sys.exit(2)
        print("All the stages have been cleared. You won the game!")
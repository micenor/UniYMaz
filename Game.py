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
                monster = choice(available_enemies)
                self.stage_enemies.append(monster())
                print(("    %s: Stats: %iHP and %iDMG") % (monster.name, monster.life, monster.damage))
            print("    ++++++++++++++++++++++++++++++++++++++")
            while((len([en for en in self.stage_enemies if en.life > 0])!=0) and (len([char for char in self.characters_list if char.life > 0]) != 0)):
                self.round += 1
                print("    ------------------------")
                print("    -    PLAYERS TURN      -")
                print("    ------------------------")
                for hero in [char for char in self.characters_list if char.life > 0]:
                    if(len([en for en in self.stage_enemies if en.life > 0])!=0):
                        while True:
                            print(("%s (Player %i). What are you going to do? ((A)ttack/(S)kill)") % (hero.name,hero.player))
                            option = input().upper()
                            if ((option!="A") and (option!="S")):
                                print("That option does not exist, ((A)ttack/(S)kill)")
                            elif (option == "S") :
                                if hero.ability(self):
                                    break
                            else: break
                        if (option=="A"):
                            hero.attack(self)
                print("    ------------------------")
                print("    -    MONSTERS TURN     -")
                print("    ------------------------")
                for monster in [en for en in self.stage_enemies if en.life > 0]:
                    if (len([hero for hero in self.characters_list if hero.life > 0])!=0):
                       monster.attack(self)
                    else:
                        break
#*****************************************End of round***************************************************
                for hero in [char for char in self.characters_list if char.life > 0]:
                    if hero.cooldown>0:
                        hero.cooldown-=1
#*****************************************End of stage***************************************************
            for hero in [char for char in self.characters_list if char.life > 0]:
                character_class = hero.__class__
                if ((hero.life + (character_class.life/4)>=character_class.life)):
                    hero.life = character_class.life
                else:
                    hero.life = hero.life + character_class.life / 4
                if hero.name=="Procrastinator":
                    hero.cooldown=0
            if(len([en for en in self.stage_enemies if en.life > 0])==0):
                print("Stage clear, all enemies defeated")
            else:
                print("All characters have been defeated. Try again.")
                sys.exit(2)
        print("All the stages have been cleared. You won the game!")
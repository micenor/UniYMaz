import Enemy
from random import randrange


class Game():
    available_enemies = [Enemy.Enemy.Partial_Exam, Enemy.Enemy.Theoretical_Class, Enemy.Enemy.Teacher]
    alive_characters = []

    def executeStage(self, i):
        if (i == 4): self.available_enemies.append(Enemy.Enemy.Final_Exam)
        stage_enemies = []
        print("         ************************")
        print(("         *       STAGE %i       *") % i)
        print("         ************************")
        print("")
        print("         ---- CURRENT MONSTERS ----")
        print("    ++++++++++++++++++++++++++++++++++++++")
        for n in range(3):
            enemy = self.available_enemies[randrange(self.available_enemies.__len__())]
            stage_enemies.append(enemy)
            print(("    %s: Stats: %iHP and %iDMG") % (enemy.name, enemy.life, enemy.damage))
        print("    ++++++++++++++++++++++++++++++++++++++")

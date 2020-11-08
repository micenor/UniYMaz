class Character():
    class Bookworn():
        life = 25
        damage = 9
        player = 0
        name = "Bookworn"
        cooldown = 0
        def ability(self,game):
            if (self.cooldown==0):
                dead = [char for char in game.characters_list if char.life <= 0]
                if (len(dead)!=0):
                    while True:
                        i = 1
                        for c in dead:
                            print(i, ".-", end=" ")
                            c.printInfo()
                            i += 1
                        try:
                            choice = int(input("Who do you want to revive?: "))
                            if (1 <= choice<= len(dead)):
                                chosen = dead[choice-1]
                                chosen.life = chosen.__class__.life
                                print("The ",self.name ," (Player ", chosen.player," ) has been revived.")
                                return True
                            else:
                                print("Incorrect choice. Choice must be between 1 and ",len(dead),".",end=" ")
                        except:
                            print("Error, you must enter a number")
                else:
                    print("All players are alive, so the skill will not be used.")
                    return False
            else:
                print("The skill is currently in cooldown for %s more rounds." % (self.cooldown))
                return False
        def printInfo(self):
            print("The bookworn -> Stats 25 HP and 9DMG")
            print("         Skill: Revives one player (4 rounds)")


    class Worker():
        life = 40
        damage = 10
        player = 0
        name = "Worker"
        """implementar habilidad"""
        def printInfo(self):
            print("The worker -> Stats: 40HP and 10DMG")
            print("         Skill: 1.5 * (DMG + DMG roll) damage to one enemy (3 rounds)")

    class Whatsapper():
        life = 20
        damage = 6
        player = 0
        name = "Whatsapper"
        """implementar Habilidad"""
        def printInfo(self):
            print("The whatsapper -> Stats: 20HP and 6DMG")
            print("         Skill: Heals 2*DMG to one player (3 rounds)")

    class Procrastinator():
        life = 30
        damage = 6
        player = 0
        name = "Procrastinator"
        """implementar pasiva"""
        def printInfo(self):
            print("The procrastinator-> Stats: 30HP and 6DMG")
            print("         Passive: Adds +1 DMG each round. Resets at the beginning of each level.")
            print("         Skill: DMG + DMG roll + stage level to all the enemies after the third round of each stage and once per stage.")
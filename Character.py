from random import choice, randrange
import math
class Character():
    class Bookworn():
        life = 25
        damage = 9
        player = 0
        name = "Bookworn"
        cooldown = 0
        def ability(self,game):
            if (self.cooldown==0):
                dead = [character for character in game.characters_list if character.life <= 0]
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
                                print(("The %s (Player %i) has been revived.") % (chosen.name,chosen.player))
                                self.cooldown = 4
                                return True
                                break
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
        def attack(self,game):
            monster_target = choice([enemy for enemy in game.stage_enemies if enemy.life > 0])
            damage = randrange(self.damage + 1)
            monster_target.life = monster_target.life - damage
            if (monster_target.life < 0):
                monster_target.life=0
            print(("%s (Player %i) did %i damage to %s. %s has %iHP left. ") % (
            self.name, self.player, damage, monster_target.name, monster_target.name, monster_target.life))

        def printInfo(self):
            print("The bookworn -> Stats 25 HP and 9DMG")
            print("         Skill: Revives one player (4 rounds)")


    class Worker():
        life = 40
        damage = 10
        player = 0
        name = "Worker"
        cooldown = 0
        def ability(self,game):
            if (self.cooldown==0):
                monster_target = choice(game.stage_enemies)
                damage = 1.5 * (self.damage + randrange(self.damage + 1))
                monster_target.life = monster_target.life - damage
                if (monster_target.life < 0):
                    monster_target.life = 0
                print(("%s (Player %i) did %i damage to %s. %s has %iHP left. ") % (
                    self.name, self.player, damage, monster_target.name, monster_target.name, monster_target.life))
                self.cooldown = 3
                return True
            else:
                print("The skill is currently in cooldown for %s more rounds." % (self.cooldown))
                return False

        def attack(self,game):
            monster_target = choice([enemy for enemy in game.stage_enemies if enemy.life > 0])
            damage = randrange(self.damage + 1)
            monster_target.life = monster_target.life - damage
            if (monster_target.life < 0):
                monster_target.life=0
            print(("%s (Player %i) did %i damage to %s. %s has %iHP left. ") % (
            self.name, self.player, damage, monster_target.name, monster_target.name, monster_target.life))

        def printInfo(self):
            print("The worker -> Stats: 40HP and 10DMG")
            print("         Skill: 1.5 * (DMG + DMG roll) damage to one enemy (3 rounds)")


    class Whatsapper():
        life = 20
        damage = 6
        player = 0
        name = "Whatsapper"
        cooldown = 0
        def ability(self,game):
            if (self.cooldown==0):
                alive = [hero for hero in game.characters_list if hero.life > 0]
                while True:
                    i = 1
                    for character in alive :
                        print(i, ".-", end=" ")
                        character.printInfo()
                        i += 1
                    try:
                        choice = int(input("Who do you want to heal?: "))
                        if (1 <= choice <= len(alive)):
                            chosen = alive[choice - 1]
                            test = chosen.life + 2 * self.damage
                            if test>chosen.__class__.life:
                                chosen.life=chosen.__class__.life
                            else:
                                chosen.life += 2*self.damage
                            self.cooldown = 3
                            return True
                            break
                        else:
                            print("Incorrect choice. Choice must be between 1 and ", len(alive), ".", end=" ")
                    except:
                        print("Error, you must enter a number")
            else:
                print("The skill is currently in cooldown for %s more rounds." % (self.cooldown))
                return False

        def attack(self,game):
            monster_target = choice([enemy for enemy in game.stage_enemies if enemy.life > 0])
            damage = randrange(self.damage + 1)
            monster_target.life = monster_target.life - damage
            if (monster_target.life < 0):
                monster_target.life=0
            print(("%s (Player %i) did %i damage to %s. %s has %iHP left. ") % (
            self.name, self.player, damage, monster_target.name, monster_target.name, monster_target.life))

        def printInfo(self):
            print("The whatsapper -> Stats: 20HP and 6DMG")
            print("         Skill: Heals 2*DMG to one player (3 rounds)")


    class Procrastinator():
        life = 30
        damage = 6
        player = 0
        name = "Procrastinator"
        cooldown = 0
        def ability(self,game):
            if ((self.cooldown==0) and (game.round >=3)):
                damage = self.damage + randrange(self.damage + 1) + game.actual_stage
                for monster_target in [en for en in game.stage_enemies if en.life > 0]:
                    monster_target.life = monster_target.life - damage
                    if (monster_target.life < 0):
                        monster_target.life = 0
                    print(("%s (Player %i) did %i damage to %s. %s has %iHP left. ") % (
                        self.name, self.player, damage, monster_target.name, monster_target.name, monster_target.life))
                self.cooldown = -1
                return True
            else:
                if game.round<3:
                    print("The skill is currently in cooldown for %s more rounds." % (3-game.round))
                else:
                    print("The skill has been used, wait until next stage to use again.")
                return False

        def attack(self,game):
            monster_target = choice([enemy for enemy in game.stage_enemies if enemy.life > 0])
            damage = randrange(self.damage + 1) + (game.round-1)
            monster_target.life = monster_target.life - damage
            if (monster_target.life < 0):
                monster_target.life=0
            print(("%s (Player %i) did %i damage to %s. %s has %iHP left. ") % (
            self.name, self.player, damage, monster_target.name, monster_target.name, monster_target.life))

        def printInfo(self):
            print("The procrastinator-> Stats: 30HP and 6DMG")
            print("         Passive: Adds +1 DMG each round. Resets at the beginning of each level.")
            print("         Skill: DMG + DMG roll + stage level to all the enemies after the third round of each stage and once per stage.")
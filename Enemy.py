from random import randrange,choice
class Enemy():
    class Partial_Exam():
        life = 20
        damage = 6
        name = "Partial Exam"
        def attack(self,game):
            hero_target = choice([character for character in game.characters_list if character.life > 0])
            damage = randrange(self.damage + 1)
            hero_target.life = hero_target.life - damage
            if hero_target.life < 0:
                hero_target.life = 0
            print(("%s did %i damage to Player %i (%s). Player %s has %iHP left.") % (
                self.name, damage, hero_target.player, hero_target.name, hero_target.player,
                hero_target.life))
            if (hero_target.life <= 0):
                print(("The %s (Player %i) has been defeated. It can not make any move until revived.") % (
                hero_target.name, hero_target.player))

    class Final_Exam():
        life = 40
        damage = 12
        name = "Final Exam"
        def attack(self,game):
            hero_target = choice([character for character in game.characters_list if character.life > 0])
            damage = randrange(self.damage + 1)
            hero_target.life = hero_target.life - damage
            if hero_target.life < 0:
                hero_target.life = 0
            print(("%s did %i damage to Player %i (%s). Player %s has %iHP left.") % (
                self.name, damage, hero_target.player, hero_target.name, hero_target.player,
                hero_target.life))
            if (hero_target.life <= 0):
                print(("The %s (Player %i) has been defeated. It can not make any move until revived.") % (
                hero_target.name, hero_target.player))

    class Theoretical_Class():
        life = 8
        damage = 4
        name = "Theoretical Exam"
        def attack(self,game):
            hero_target = choice([character for character in game.characters_list if character.life > 0])
            damage = randrange(self.damage + 1) + game.actual_stage
            hero_target.life = hero_target.life - damage
            if hero_target.life < 0:
                hero_target.life=0
            print(("%s did %i damage to Player %i (%s). Player %s has %iHP left.") % (
            self.name, damage, hero_target.player, hero_target.name, hero_target.player,
            hero_target.life))
            if (hero_target.life <= 0):
                print(("The %s (Player %i) has been defeated. It can not make any move until revived.") % (hero_target.name, hero_target.player))

    class Teacher():
        life = 15
        damage = 7
        name = "Teacher"
        def attack(self,game):
            hero_target = choice([character for character in game.characters_list if character.life > 0])
            damage = randrange(self.damage + 1)
            if (damage==7):
                damage=14
            hero_target.life = hero_target.life - damage
            if hero_target.life < 0:
                hero_target.life = 0
            print(("%s did %i damage to Player %i (%s). Player %s has %iHP left.") % (
                self.name, damage, hero_target.player, hero_target.name, hero_target.player,
                hero_target.life))
            if (hero_target.life <= 0):
                print(("The %s (Player %i) has been defeated. It can not make any move until revived.") % (
                hero_target.name, hero_target.player))
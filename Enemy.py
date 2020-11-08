from random import randrange,choice
class Enemy():
    class Partial_Exam():
        life = 20
        damage = 6
        name = "Partial Exam"
        def attack(self,game):
            character_target = choice([character for character in game.characters_list if character.life > 0])
            damage = randrange(self.damage + 1)
            character_target.life = character_target.life - damage
            print(("%s did %i damage to Player %i (%s). Player %s has %iHP left.") % (
            self.name, damage, character_target.player, character_target.name, character_target.player,
            character_target.life))
            if (character_target.life <= 0):
                print(("Player %i has died") % character_target.player)

    class Final_Exam():
        life = 40
        damage = 12
        name = "Final Exam"
        def attack(self,game):
            character_target = choice([character for character in game.characters_list if character.life > 0])
            damage = randrange(self.damage + 1)
            character_target.life = character_target.life - damage
            print(("%s did %i damage to Player %i (%s). Player %s has %iHP left.") % (
            self.name, damage, character_target.player, character_target.name, character_target.player,
            character_target.life))
            if (character_target.life <= 0):
                print(("Player %i has died") % character_target.player)

    class Theoretical_Class():
        life = 8
        damage = 4
        name = "Theoretical Exam"
        def attack(self,game):
            character_target = choice([character for character in game.characters_list if character.life > 0])
            damage = randrange(self.damage + 1)
            character_target.life = character_target.life - damage
            print(("%s did %i damage to Player %i (%s). Player %s has %iHP left.") % (
            self.name, damage, character_target.player, character_target.name, character_target.player,
            character_target.life))
            if (character_target.life <= 0):
                print(("Player %i has died") % character_target.player)

    class Teacher():
        life = 15
        damage = 7
        name = "Teacher"
        def attack(self,game):
            character_target = choice([character for character in game.characters_list if character.life > 0])
            damage = randrange(self.damage + 1)
            if (damage==7):
                damage=14
            character_target.life = character_target.life - damage
            print(("%s did %i damage to Player %i (%s). Player %s has %iHP left.") % (
            self.name, damage, character_target.player, character_target.name, character_target.player,
            character_target.life))
            if (character_target.life <= 0):
                print(("Player %i has died") % character_target.player)
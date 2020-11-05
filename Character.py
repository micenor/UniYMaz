class Character:
    class Bookworn:
        life = 25
        damage = 9
        """implementar habilidad"""
        def printInfo(self):
            print("1.- The bookworn -> Stats 25 HP and 9DMG")
            print("         Skill: Revives one player (4 rounds)")

    class Worker:
        life = 40
        damage = 10
        """implementar habilidad"""
        def printInfo(self):
            print("2.- The worker -> Stats: 40HP and 10DMG")
            print("         Skill: 1.5 * (DMG + DMG roll) damage to one enemy (3 rounds)")

    class Whatsapper:
        life = 20
        damage = 6
        """implementar Habilidad"""
        def printInfo(self):
            print("3.- The whatsapper -> Stats: 20HP and 6DMG")
            print("         Skill: Heals 2*DMG to one player (3 rounds)")

    class Procrastinator:
        life = 30
        damage = 6
        """implementar pasiva"""
        def printInfo(self):
            print("4.- The procrastinator-> Stats: 30HP and 6DMG")
            print("         Passive: Adds +1 DMG each round. Resets at the beginning of each level.")
            print(
                "         Skill: DMG + DMG roll + stage level to all the enemies after the third round of each stage and once per stage.")
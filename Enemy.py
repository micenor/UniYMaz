class Enemy():
    class Partial_Exam():
        life = 20
        damage = 6
        name = "Partial Exam"

    class Final_Exam():
        life = 40
        damage = 12
        name = "Final Exam"
        """Solo sale a partir de al ronda 4"""

    class Theoretical_Class():
        life = 8
        damage = 4
        name = "Theoretical Exam"
        """Suma +1 por cada nivel (nivel 2 +2 etc)"""
    class Teacher():
        life = 15
        damage = 7
        name = "Teacher"
        """Si hace 7 de daño, hace 14 en realidad"""
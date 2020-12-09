class Student: 

    def __init__(self, age, major, gpa):
        self.age = age
        self.major = major
        self.gpa = gpa


    def on_honor_roll(self):
        if self.gpa >= 3.5:
            return True
        else:
            return False

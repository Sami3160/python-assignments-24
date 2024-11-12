class Sami:
    def skill(self):
        return "Sami is good at Python."

class Malhar:
    def skill(self):
        return "Malhar is good at Java."

class Atharv(Sami, Malhar):
    def show_skills(self):
        return f"{self.skill()} and {super().skill()}"

atharv = Atharv()
print(atharv.show_skills())
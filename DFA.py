class DFA:
    def __init__ (self, energy = 0, hygiene = 0, fun = 0):
    
    def Tidur(self, a):
        if a == "Siang":
            self.energy +=10
        elif a == "Malam":
            self.energy +=15
    
    def Makan(self, a):
        if a == "Hamburger":
            self.energy += 5
        elif a == "Pizza":
            self.energy += 10
        elif a == "Steak and Beans":
            self.energy += 15

txt = str(raw_input())
x = txt.split(,3)
print(x)
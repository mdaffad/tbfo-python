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
    def Minum(self, a):
        if a == "Air":
            self.hygiene -= 5
        elif a == "Kopi":
            self.energy += 5
            self.hygiene-= 10
        elif a == "Jus":
            self.energy += 10
            self.hygiene-=5
    
    def Buang (self, a):
        if a == "Kecil":
            self.hygiene+=5
        elif a == "Besar"
            self.Besar +=10
            self.energy+=-5
    def Bersosialisasi(self):
        self.fun += 15
        self.energy-=10
        self.hygiene-=5
    def Bermain(self, a);
        if a == "Media":
            self.fun +=10
            self.energy-=10
        elif a == "Komputer":
            self.fun +=15
            self.energy-=10
    def Mandi (self):
        self.hygiene+=15
        self.energy -=5
    def Cuci (self):
        self.hygiene+=5
    def Mendengarkan (self)
        self.fun += 10
        self.energy -= 5
    def Membaca(self,a):
        if a == "Koran":
            self.fun+=5
            self.energy-=5
        elif a == "Novel":
            self.fun += 10
            self.energy -=5
  
txt = str(raw_input())
x = txt.split(,3)
print(x)
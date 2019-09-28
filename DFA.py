class State:
    # Konstruktor 
    def __init__ (self, energy = 0, hygiene = 0, fun = 0):
        # default : Semua nilai = 0 
        self.energy = energy
        self.fun = fun
        self.hygiene = hygiene
    
    # Trantition
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
        elif a == "Steak":
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
        elif a == "Besar":
            self.Besar +=10
            self.energy+=-5
    def Bersosialisasi(self):
        self.fun += 15
        self.energy-=10
        self.hygiene-=5
    def Bermain(self, a):
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
    def Mendengarkan (self):
        self.fun += 10
        self.energy -= 5
    def Membaca(self,a):
        if a == "Koran":
            self.fun+=5
            self.energy-=5
        elif a == "Novel":
            self.fun += 10
            self.energy -=5

finish = False
Q = State()

while (not finish):  
    txt = str(raw_input())
    x = txt.split()

    temp = State(Q.energy, Q.hygiene, Q.fun)
    if x[0] == "Tidur":
        Q.Tidur(x[1])
    elif x[0] == "Makan":
        Q.Makan(x[1])
    elif x[0] == "Minum":
        Q.Minum(x[1])
    elif x[0] == "Buang":
        Q.Buang(x[2])
    elif x[0] == "Bersosialisasi":
        Q.Bersosialisasi()
    elif x[0] == "Bermain":
        Q.Bermain(x[1])
    elif x[0] == "Mandi":
        Q.Mandi()
    elif x[0] == "Cuci":
        Q.Cuci()
    elif x[0] == "Mendengarkan":
        Q.Mendengarkan()
    elif x[0] == "Membaca":
        Q.Membaca(x[[1]])
    if 0 <= Q.hygiene <= 15 and 0 <= Q.energy <= 15 and 0 <= Q.fun <= 15:
        print("Hygiene = " + str(Q.hygiene) + "\n" + "Energy = " + str(Q.energy) + "\n" + "Fun = " + str(Q.fun))
    else:
        print("Masukan tidak valid\n")
        Q = temp
    if Q.hygiene == 15 and Q.energy == 15 and Q.fun == 15:
        finish = True

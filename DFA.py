class State:
    # Konstruktor 
    def __init__ (self, energy = 10, hygiene = 0, fun = 0):
        # default : Semua nilai = 0 kecuali hygiene sudah 10
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
            self.hygiene +=10
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

# Konstruksi objek state
Q = State(10)
# inisialisasi kondisi awal
finish = False
Aksi = True

# DFA
while (not finish):  
    # Mengembalikan Nilai awal Aksi
    Aksi = True

    print("\n")

    # Input raw string untuk menyimpan semua teks dalam satu baris
    txt = str(raw_input())

    # splitting raw string agar mempermudah proses
    x = txt.split()

    # menyimpan state sementara (temp) agar mengembalikan
    # state jika state merupakan aksi tidak valid

    temp = State(Q.energy, Q.hygiene, Q.fun)
    
    # Proses seleksi Aksi (transisi DFA)
    if txt == "Tidur Siang" or txt == "Tidur Malam":
        Q.Tidur(x[1])
    elif txt == "Makan Hamburger" or txt == "Makan Pizza" or txt == "Makan Steak and Beans":
        Q.Makan(x[1])
    elif txt == "Minum Air" or txt == "Minum Jus" or txt == "Minum Kopi":
        Q.Minum(x[1])
    elif txt == "Buang Air Kecil" or txt == "Buang Air Besar":
        Q.Buang(x[2])
    elif txt == "Bersosialisasi ke Kafe":
        Q.Bersosialisasi()
    elif txt == "Bermain Media Sosial" or txt == "Bermain Komputer":
        Q.Bermain(x[1])
    elif txt == "Mandi":
        Q.Mandi()
    elif txt == "Cuci Tangan":
        Q.Cuci()
    elif txt == "Mendengarkan Musik di Radio":
        Q.Mendengarkan()
    elif txt == "Membaca Koran" or txt == "Membaca Novel":
        Q.Membaca(x[[1]])
    
    # Apabila tidak terdapat transisi yang sesuai dengan nama
    else:
        print("\nAksi tidak valid\n")
        Aksi = False
    
    # Apabila terdapat nama transisi valid dan semua nilai state valid
    if 0 <= Q.hygiene <= 15 and 0 <= Q.energy <= 15 and 0 <= Q.fun <= 15 and Aksi:
        print("\nHygiene = " + str(Q.hygiene) + "\n" + "Energy = " + str(Q.energy) + "\n" + "Fun = " + str(Q.fun))
    
    # Apablia terdapat nama transisi valid dan ada nilai state yang tidak valid
    elif Aksi:
        print("\nAksi tidak valid\n")
        # reset ke state sementara
        Q = temp
    
    # Syarat permainan selesai
    if (Q.hygiene == 15 and Q.energy == 15 and Q.fun == 15):
        finish = True
        print("\nProgam Selesai\nSemua atribut bernilai maksimum")
    
    if (Q.hygiene == 0 and Q.energy == 0 and Q.fun == 0):
        finish = True
        print("\nProgam Selesai\nSemua atribut bernilai minimum")
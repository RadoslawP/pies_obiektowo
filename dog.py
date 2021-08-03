class Pies:
    def __init__(self, imie, wiek, waga):
        self.imie = imie
        self.wiek = wiek
        self.waga = waga

    def szczekanie(self):
        if self.waga > 10:
            print(self.imie, 'robi "HAU, HAU"')
        else:
            print(self.imie, 'robi "hau, hau"')

    def ludzkie_lata(self):
        print('Twój pies', self.imie, 'miałby jako człowiek', int(self.wiek)*7, 'lat(a).')

    def __str__(self):
        return 'Jestem psem o imieniu' + self.imie

class PiesTowarzyszacy(Pies):
    def __init__(self, imie, wiek, waga, opiekun):
        Pies.__init__(self, imie, wiek, waga)
        self.opiekun = opiekun
        self.pelni_sluzbe = False

    def chodzenie(self):
        print(self.imie, 'i jego opiekun', self.opiekun, 'wychodzą na spacer')

    def szczekanie(self):
        if self.pelni_sluzbe:
            print(self.imie, 'mówi: "Nie mogę szczekać, bo jestem na służbie."')
        else:
            Pies.szczekanie(self)

def wyswietl_psa(pies):
    print(pies.imie, "ma", pies.wiek, "lat i waży", pies.waga)

kodi = Pies('Kodi', 12, 18)
fafik = Pies('Fafik', 9, 6)
rufus = PiesTowarzyszacy('Rufus', 8, 20, 'Jan')

print('Imię tego psa to', rufus.imie)
print('Opiekun tego psa to', rufus.opiekun)

wyswietl_psa(rufus)
rufus.szczekanie()
rufus.pelni_sluzbe = True
rufus.szczekanie()
rufus.chodzenie()

wyswietl_psa(kodi)
wyswietl_psa(fafik)

kodi.szczekanie()
fafik.szczekanie()
kodi.ludzkie_lata()
fafik.ludzkie_lata()

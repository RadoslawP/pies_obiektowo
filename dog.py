class Hotel:
    def __init__(self, nazwa):
        self.nazwa = nazwa
#       self.buda_imiona = []
#       self.buda_psy = []
        self.buda = {}

    def zameldowanie(self, pies):
        if isinstance(pies, Pies):
            self.buda[pies.imie] = pies
#           self.buda_imiona.append(pies.imie)
#           self.buda_psy.append(pies)
            print(pies.imie, 'zameldował się w', self.nazwa)
        else:
            print('Przykro nam,', self.nazwa, 'przyjmuje tylko psy')

    def wymeldowanie(self, imie):
        if imie in self.buda:
            pies = self.buda[imie]
#        for i in range(0, len(self.buda_imiona)):
#            if imie == self.buda_imiona[i]:
#                pies = self.buda_psy[i]
#                del self.buda_imiona[i]
#                del self.buda_psy[i]
            print(pies.imie, 'wymeldował się z', self.nazwa)
            del self.buda[pies.imie]
            return pies
        else:
            print('Przykro nam,', imie, 'nie jest zameldowany w', self.nazwa)
            return None

    def pora_szczekania(self):
        for imie_psa in self.buda:
            pies = self.buda[imie_psa]
            pies.szczekanie()

    def zatrudnienie_wyprowadzacza(self, wyprowadzacz):
        if isinstance(wyprowadzacz, WyprowadzaczPsow):
            self.wyprowadzacz = wyprowadzacz
        else:
            print(wyprowadzacz.imie, 'nie jest wyprowadzaczem psów')

    def usluga_wyprowadzania(self):
        if self.wyprowadzacz != None:
            self.wyprowadzacz.wyprowadzanie_psow(self.buda)

class Osoba:
    def __init__(self, imie):
        self.imie = imie

    def __str__(self):
        return "Jestem osobą i mam na imię " + self.imie

class WyprowadzaczPsow(Osoba):
    def __init__(self, imie):
        Osoba.__init__(self, imie)

    def wyprowadzanie_psow(self, psy):
        for imie_psa in psy:
            psy[imie_psa].chodzenie()

class Kot():
    def __init__ (self, imie):
        self.imie = imie

    def miau(self):
        print(self.imie, 'Robi "miau"')

class Frisbee:
    def __init__(self, kolor):
        self.kolor = kolor

    def __str__(self):
        return 'Jestem frisbee, a mój kolor to ' + self.kolor

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

    def chodzenie(self):
        print(self.imie, 'idzie')

    def __str__(self):
        return 'Jestem psem o imieniu' + self.imie

class PiesAportujacy(Pies):
    def __init__(self, imie, wiek, waga):
        Pies.__init__(self, imie, wiek, waga)
        self.frisbee = None

    def szczekanie(self):
        if self.frisbee != None:
            print(self.imie, 'mówi: "Nie mogę szczekać, bo trzymam w pysku frisbee.""')
        else:
            Pies.szczekanie(self)

    def lapanie(self, frisbee):
        self.frisbee = frisbee
        print(self.imie, 'złapał frisbee w kolorze', frisbee.kolor + 'm')

    def zwracanie(self):
        if self.frisbee != None:
            frisbee = self.frisbee
            self.frisbee = None
            print(self.imie, 'zwraca frisbee w kolorze', frisbee.kolor + 'm')
            return frisbee
        else:
            print(self.imie, 'nie ma frisbee')
            return None

    def chodzenie(self):
        if self.frisbee != None:
            print('Nie mogę teraz iść, bo aportuję frisbee!')
        else:
            Pies.chodzenie(self)

    def __str__(self):
        str = 'Jestem psem o imieniu ' + self.imie
        if self.frisbee != None:
            str = str + ' i mam frisbee'
        return str

class PiesTowarzyszacy(Pies):
    def __init__(self, imie, wiek, waga, opiekun):
        Pies.__init__(self, imie, wiek, waga)
        self.opiekun = opiekun
        self.pelni_sluzbe = False

    def chodzenie(self):
        if self.pelni_sluzbe:
            print(self.imie, 'i jego opiekun', self.opiekun, 'wychodzą na spacer')
        else:
            Pies.chodzenie(self)

    def szczekanie(self):
        if self.pelni_sluzbe:
            print(self.imie, 'mówi: "Nie mogę szczekać, bo jestem na służbie."')
        else:
            Pies.szczekanie(self)

def wyswietl_psa(pies):
    print(pies.imie, "ma", pies.wiek, "lat i waży", pies.waga)

def kod_testowy():
    kodi = Pies('Kodi', 12, 18)
    fafik = Pies('Fafik', 9, 6)
    rufus = PiesTowarzyszacy('Rufus', 8, 20, 'Jan')
    rufus.pelni_sluzbe = True
    drab = PiesAportujacy('Drab', 5, 9)
    azor = Pies('Azor', 2, 4)

    hotel = Hotel('Hotel dla Psiaków')
    hotel.zameldowanie(kodi)
    hotel.zameldowanie(fafik)
    hotel.zameldowanie(rufus)
    hotel.zameldowanie(drab)

    jacek = WyprowadzaczPsow('Jacek')
    hotel.zatrudnienie_wyprowadzacza(jacek)

    hotel.usluga_wyprowadzania()

#   frisbee = Frisbee('czerwony')
#    drab.lapanie(frisbee)
#    kodi.chodzenie()
#    fafik.chodzenie()
#    rufus.chodzenie()
#    drab.chodzenie()

#   kicia = Kot('Kicia')

#    hotel.pora_szczekania()
#    hotel.zameldowanie(kicia)

#    pies = hotel.wymeldowanie(kodi.imie)
#    print('Wymeldował się', pies.imie + ', który ma', pies.wiek, 'lat i waży', pies.waga, 'kg.')
#    pies = hotel.wymeldowanie(fafik.imie)
#    print('Wymeldował się', pies.imie + ', który ma', pies.wiek, 'lat i waży', pies.waga, 'kg.')
#    pies = hotel.wymeldowanie(rufus.imie)
#    print('Wymeldował się', pies.imie + ', który ma', pies.wiek, 'lat i waży', pies.waga, 'kg.')
#    pies = hotel.wymeldowanie(drab.imie)
#    print('Wymeldował się', pies.imie + ', który ma', pies.wiek, 'lat i waży', pies.waga, 'kg.')
#    pies = hotel.wymeldowanie(azor.imie)

#    niebieskie_frisbee = Frisbee('niebieski')
#    print(drab)
#    drab.szczekanie()
#    drab.lapanie(niebieskie_frisbee)
#    drab.szczekanie()
#    print(drab)
#    frisbee = drab.zwracanie()
#    print(frisbee)

kod_testowy()



# print('Imię tego psa to', rufus.imie)
# print('Opiekun tego psa to', rufus.opiekun)

# wyswietl_psa(rufus)
# rufus.szczekanie()
# rufus.pelni_sluzbe = True
# rufus.szczekanie()
# rufus.chodzenie()

# wyswietl_psa(kodi)
# wyswietl_psa(fafik)

# kodi.szczekanie()
# fafik.szczekanie()
# kodi.ludzkie_lata()
# fafik.ludzkie_lata()

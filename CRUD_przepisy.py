
def dodaj_przepis():
        nazwa_przepisu = input("Podaj nazwe przepisu: ")
        skladniki = dodaj_petla(1)

        print("Teraz wypisz kolejne kroki. Wpisz KONIEC, by zakończyć: ")
        kroki = dodaj_petla(2)

        przepis = {"Skladniki": skladniki, "Kroki": kroki}
        przepisy[nazwa_przepisu] = przepis

        pokaz_przepis(nazwa_przepisu)
        print("")
        powrot()
def dodaj_petla(element):
    '''Funkcja uruchamia pętle w której na wejściu podaje sie skladniki i ich ilosc (arg = 1),
    lub kolejne kroki przepisu (arg = 2). Zwraca odpowiednio slownik skladnikow, lub liste krokow'''
    if element == 1:
        skladniki = {}
        print("Proszę o podanie składnikow i ich ilości. Wpisz KONIEC, by zakończyć: ")
        while True:
            nazwa_skladnika = input("Nazwa: ")
            if nazwa_skladnika == "KONIEC":
                del nazwa_skladnika
                break

            ilosc = input("Ilość: ")
            if ilosc == "KONIEC":
                del nazwa_skladnika
                del ilosc
                break
            skladniki[nazwa_skladnika] = ilosc
        return skladniki
    if element == 2:
        kroki = []
        licznik = 1
        while True:
            krok = input("Co należy zrobić w " + str(licznik) + " " + "kroku? ")
            if krok == "KONIEC":
                break
            kroki.append(krok)
            licznik += 1
        return kroki

def przegladaj_przepisy():
    print("Dostępne przepisy:")
    lista = widok_przepisow()
    wybor = int(input("Podaj nr przepisu: ")) - 1
    pokaz_przepis(lista[wybor])
    #start(startowa = input("Co teraz? \n1 - dodaj\n2 - przegladaj\n3 - edycja/usun"))
    powrot()

def operacje_na_przepisach():
    lista = widok_przepisow()
    wybor = int(input("Podaj nr przepisu: ")) - 1
    operacje_przepis(lista[wybor])
    powrot()

def widok_przepisow():
    lista_przepisow = list(przepisy.keys())
    lp = 1
    for i in range(len(lista_przepisow)):
        print(str(lp) +". " + lista_przepisow[i])
        lp+=1
    return lista_przepisow

def pokaz_przepis(nazwa_przepisu):
    surowce=list(przepisy[nazwa_przepisu]["Skladniki"].items())
    kroki = przepisy[nazwa_przepisu]["Kroki"]

    print(nazwa_przepisu)
    print("______________________")

    print("Składniki:")
    for i in range(len(surowce)):
        print(surowce[i][0] + " - " + surowce[i][1])

    print("\nEtapy przygotowania: ")
    for j in range(len(kroki)):
        print("Krok " + str(j+1) + " " + kroki[j])

    print("______________________")

def operacje_przepis(nazwa_przepisu):

    pokaz_przepis(nazwa_przepisu)
    wybor = input("Wpisz odpowiednią cyfrę i zatwierdź enterem, aby podjąć akcję:\n1 - edycja przepisu\n2 - usun przepis\n")
    if wybor == "1":
        edycja_przepisu(nazwa_przepisu)
    elif wybor == "2":
        if input("Aby usunac wpisz ""TAK"" :") == "TAK":
            del przepisy[nazwa_przepisu]
        else:
            powrot()

def edycja_przepisu(nazwa_przepisu):
    skladniki = list(przepisy[nazwa_przepisu]["Skladniki"].keys())
    ilosci = list(przepisy[nazwa_przepisu]["Skladniki"].values())
    kroki = przepisy[nazwa_przepisu]["Kroki"]
    s=1
    k=1
    pokaz_przepis(nazwa_przepisu)

    print("")
    wybor = input("Co chcesz edytować? \n1 - skladniki\n2 - kroki \n3 - nazwe\n0 - powrot\n")

    if wybor == "1":
        wyliczenie1(skladniki, ilosci)
        stary_element = int(input("Który skladnik do edycji? "))-1
        skladniki[stary_element] = input("Nazwa nowego skladnika: ")
        ilosci[stary_element] = input("Ilosc nowego skladnika: ")
        przepisy[nazwa_przepisu]["Skladniki"] = dict(zip(skladniki, ilosci))

    elif wybor == "2":
        wyliczenie1(kroki)
        wybor = int(input("Który krok do edycji? ")) - 1
        przepisy[nazwa_przepisu]["Kroki"][wybor] = input("nowy krok to: ")

    elif wybor == "3":
        nowa_nazwa = input("Nowa nazwa to: ")
        x = przepisy[nazwa_przepisu]
        przepisy[nowa_nazwa] = x
        del przepisy[nazwa_przepisu]
    elif wybor == "0":
        powrot()

def wyliczenie1(lista, *args):
    licznik = 1
    if bool(args) == True:
        lista1 = list(args)
        lista2 = lista
        test = zip(lista2, lista1[0])
        print(test)
        for i, j in test:
            print(str(licznik) + ". " + i + " - " + j)
            licznik += 1
    else:
        for i in lista:
            print(str(licznik) + ". " + i)
            licznik += 1


def odczyt_bazy():
    f = open("baza.txt", 'r')
    y = f.readline()
    f.close()
    exec(y, globals())
def zapis_bazy():
    f = open("baza.txt", 'w')
    f.write("przepisy = " + str(przepisy))
    f.close()

def wyjdz():
    zapis_bazy()
    print("Zmiany zapisane zapisane. Do widzenia")
    return 0

def przywroc_domyslne():
    global przepisy
    przepisy = {'Omlet': {'Skladniki': {'Jajka': '3 sztuki', 'Mąka pszenna': '4 łyżki', 'Odżywka białkowa': '20 g',
                                        'Cukier': '2 łyżeczki', 'Masło orzechowe': '25 g'},
                          'Kroki': ['Oddziel żółtka od białek', 'Ubij piane z białek z dodatkiem cukru',
                                    'Kolejno stopniowo dodaj: żółtka, mąkę i odżywkę białkową',
                                    'Smaż na niedużej ilości tłuszczu kokosowego, na wolny ogniu',
                                    'podawaj ze świeżymi owocami i masłem orzechowym dla podbicia kalorii']},
                'Gulasz': {'Skladniki': {'A': '1szt', 'B': '2szt', 'C': '3szt'}, 'Kroki': ['JEDEN', 'DWA', 'TRZY']}}
    powrot()

def powrot():
    wait = input("Wpisz cokolwiek by kontynuowac")
    startowa = input("CRUD - przepisy\n\n1 - dodaj przepis\n2 - przeglądaj przepisy\n3 - edytuj lub usuń przepis\n0 - wyjdz i zapisz\n4 - przywroc domyslne\n:")
    start(startowa)

def start(startowa = input("CRUD - przepisy\n\n1 - dodaj przepis\n2 - przeglądaj przepisy\n3 - edytuj lub usuń przepis\n0 - wyjdz i zapisz\n4 - przywroc domyslne\n:")):
    while True:
        if startowa == "0":
            wyjdz()
            exit()
        elif startowa == "1":
            dodaj_przepis()
        elif startowa == "2":
            przegladaj_przepisy()
        elif startowa == "3":
            operacje_na_przepisach()
        elif startowa == "4":
            przywroc_domyslne()
        else:
            start(startowa=input("Sprobuj innej komendy"))

odczyt_bazy()
start()
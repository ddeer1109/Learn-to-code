
def dodaj_przepis():
        nazwa_przepisu = input("Podaj nazwe przepisu: ")

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
            print(skladniki)

        kroki = []
        licznik = 1
        print("Teraz wypisz kolejne kroki. Wpisz KONIEC, by zakończyć: ")
        while True:

            krok = input("Co należy zrobić w " + str(licznik) + " " + "kroku? ")
            if krok == "KONIEC":
                print(kroki)
                break
            kroki.append(krok)
            print(str(licznik) +". " + kroki[len(kroki)-1])
            licznik+=1
            print(kroki)
            Kroki = kroki

        przepis = {"Skladniki": skladniki, "Kroki": Kroki}
        przepisy[nazwa_przepisu] = przepis
        print(przepisy[nazwa_przepisu])
        start(startowa = input("Co teraz\n1 - dodaj przepis\n2 - przeglądaj przepisy\n3 - edytuj lub usuń przepis"))


def przegladaj_przepisy():
    print("Dostępne przepisy:")
    lista = widok_przepisow()
    wybor = int(input("Podaj nr przepisu: ")) - 1
    pokaz_przepis(lista[wybor])
    start(startowa = input("Co teraz? \n1 - dodaj\n2 - przegladaj\n3 - edycja/usun"))

def operacje_na_przepisach():
    lista = widok_przepisow()
    wybor = int(input("Podaj nr przepisu: ")) - 1
    operacje_przepis(lista[wybor])
    start(startowa=input("Co teraz?\n1 - dodaj\n2 - przegladaj\n3 - edycja/usun"))

def widok_przepisow():
    lista_przepisow = list(przepisy.keys())
    lp = 1
    for i in range(len(lista_przepisow)):
        print(str(lp) +". " + lista_przepisow[i])
        lp+=1
    return lista_przepisow

def pokaz_przepis(nazwa_przepisu):

    surowce=list(przepisy[nazwa_przepisu]["Skladniki"].items())
    #print(str(surowce))
    kroki = przepisy[nazwa_przepisu]["Kroki"]
    #print(str(kroki) +"\n\n")

    print(nazwa_przepisu)
    print("______________________")
    print("Składniki:")
    for i in range(len(surowce)):
        print(surowce[i][0] + " - " + surowce[i][1])
    print("\nEtapy przygotowania: ")
    licznik = 0
    for j in range(len(kroki)):
        print("Krok " + str(j+1) + " " + kroki[j])
    print("_____________________")


def operacje_przepis(nazwa_przepisu):

    pokaz_przepis(nazwa_przepisu)
    wybor = input("Wpisz odpowiednią cyfrę i zatwierdź enterem, aby podjąć akcję:\n1 - edycja przepisu\n2 - usun przepis\n")
    if wybor == "1":
        edycja_przepisu(nazwa_przepisu)
    elif wybor == "2":
        usun_przepis(nazwa_przepisu, wybor)


def edycja_przepisu(nazwa_przepisu):
    skladniki = list(przepisy[nazwa_przepisu]["Skladniki"].keys())
    ilosci = list(przepisy[nazwa_przepisu]["Skladniki"].values())
    kroki = przepisy[nazwa_przepisu]["Kroki"]
    s=1
    k=1
    pokaz_przepis(nazwa_przepisu)

    print("")
    wybor = input("Co chcesz edytować? \n1 - skladniki\n2 - kroki \n3 - nazwe\n")
    if wybor == "1":
        wyliczenie1(skladniki, ilosci)
        stary_element = int(input("Który skladnik do edycji? "))-1
        skladniki[stary_element] = input("Nazwa nowego skladnika: ")
        ilosci[stary_element] = input("Ilosc nowego skladnika: ")
        przepisy[nazwa_przepisu]["Skladniki"] = dict(zip(skladniki, ilosci))

    elif wybor == "2":
        wyliczenie1(kroki)
        wybor = input("Który krok do edycji? ")
        przepisy[nazwa_przepisu]["Kroki"][int(wybor)] = input("nowy krok to: ")

    elif wybor == "3":
        nowa_nazwa = input("Nowa nazwa to: ")
        x = przepisy[nazwa_przepisu]
        przepisy[nowa_nazwa] = x
        del przepisy[nazwa_przepisu]


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


def usun_przepis(nazwa_przepisu, wybor):
    zatwierdzenie = input("Jesteś tego pewien? Wpisz tak i zatwierdź enterem, wpisz cokolwiek aby odrzucic: ")
    if zatwierdzenie == "tak" or "TAK":
        del przepisy[nazwa_przepisu]
    else:
        start(startowa="3")


def start(startowa = input("CRUD - przepisy\n\n1 - dodaj przepis\n2 - przeglądaj przepisy\n3 - edytuj lub usuń przepis")):
    while True:
        if startowa == "0":
            return 0
        elif startowa == "1":
            dodaj_przepis()
        elif startowa == "2":
            przegladaj_przepisy()
        elif startowa == "3":
            operacje_na_przepisach()
        else:
            start(startowa=input("Sprobuj innej komendy"))

przepisy = {}
przepisy["Omlet"] = {'Skladniki': {'Jajka': '3 sztuki', 'Mąka pszenna': '4 łyżki', 'Odżywka białkowa': '20 g', 'Cukier': '2 łyżeczki', 'Masło orzechowe': '25 g'}, 'Kroki': ['Oddziel żółtka od białek', 'Ubij piane z białek z dodatkiem cukru', 'Kolejno stopniowo dodaj: żółtka, mąkę i odżywkę białkową', 'Smaż na niedużej ilości tłuszczu kokosowego, na wolny ogniu', 'podawaj ze świeżymi owocami i masłem orzechowym dla podbicia kalorii']}
przepisy["TEST"] = {'Skladniki': {'SKLADNIK A': '3 sztuki', 'SKLADNIK B': '4 łyżki', 'SKLADNIK C': '20 g', 'SKLADNIK D': '2 łyżeczki', 'SKLADNIK E': '25 g'}, 'Kroki': ['11111111', '2222222', '33333']}
start()
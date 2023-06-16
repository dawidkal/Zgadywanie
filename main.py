import random


def zgadywanie_wyrazu():
 while True:
    with open("slowa.txt", "r") as plik:
        slowa = [line.strip() for line in plik.readlines()]
    plik.close()

    wylosowane_slowo = random.choice(slowa)
    dlugosc_slowa = len(wylosowane_slowo)
    zgadniete = False
    zgadniete_litery = []
    proba = 0
    print("***************************")
    print("*Zgadnij wylosowane słowo!*")
    print("***************************")
    print(f"Słowo składa się z {dlugosc_slowa} liter.")

    while not zgadniete:
        wpisana_litera = input("Podaj literę: ")

        if wpisana_litera == "koniec":
            #break
            exit()

        if len(wpisana_litera) != 1:
            print("Podaj jedną literę!")
            continue

        if wpisana_litera in zgadniete_litery:
            print("Już zgadłeś tę literę. Spróbuj inną!")
            continue

        zgadniete_litery.append(wpisana_litera)
        proba += 1

        if wpisana_litera in wylosowane_slowo:
            print("Zgadłeś! Ta litera znajduje się w słowie.")
        else:
            print("Nie zgadłeś. Ta litera nie występuje w słowie.")

        odgadniete_litery = [litera if litera in zgadniete_litery else "_" for litera in wylosowane_slowo]
        print(" ".join(odgadniete_litery))

        if "_" not in odgadniete_litery:
            print("Gratulacje! Odgadłeś słowo!")
            zgadniete = True
            proba=0

        print(f"Próba nr {proba}")
        print("** Graj dalej! Wpisanie wyrazu koniec kończy grę **")

zgadywanie_wyrazu()

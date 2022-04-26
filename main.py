from szyfry_logika import *
import os


print("Wybierz w jaki sposob chcesz zaszyfrowac lub odszyfrowac swoj tekst (wybierz cyfre od 1-3): ")
print("#"*92)
print("#" + " " * 30 + "1 - Enchanting Language Minecraft"+" "*(92-(len("1 - Enchanting Language Minecraft")+32))+"#")
print("#" + " " * 30 + "2 - Szyfr podstawieniowy" + " "*(92-(len("2 - Szyfr podstawieniowy")+32))+"#")
print("#" + " " * 30 + "3 - Szyfr Vigenère’a" + " "*(92-(len("2 - Szyfr Vigenère’a")+32))+"#")
print("#" + " " * 30 + "4 - Szyfr Bacona" + " "*(92-(len("4 - Szyfr Bacona")+32))+"#")
print("#"*92)
wybor = int(input("Wybierz co chcesz robic: "))

tab = [1, 2, 3, 4]

while wybor not in tab:
    wybor = int(input("Spróbuj ponownie: "))
    if wybor in tab:
        break

os.system("cls")
print()

if wybor == 1:
    print("Teraz wybierz co chcesz zrobic ze swoim tekstem."+"\n"+"1 - jesli chcesz szyfrowac" + "\n" + "2 - jesli chcesz deszyfrowac")
    print()
    wybor = int(input("Wybierz numer: "))
    if wybor == 1:
        tekst = input("Podaj tekst, ktory chcesz zamienic: ").lower()
        coding = Enchant(tekst=tekst)
        print(coding.coding(), end="")

    elif wybor == 2:
        kod = input("Podaj kod, ktory chcesz odszyfrowac: ")
        uncoding = Enchant(kod=kod)
        print(uncoding.decoding(), end="")

elif wybor == 2:
    print("Teraz wybierz co chcesz zrobic ze swoim tekstem."+"\n"+"1 - jesli chcesz szyfrowac" + "\n" + "2 - jesli chcesz deszyfrowac")
    print()
    wybor = int(input("Wybierz numer: "))

    if wybor == 1:
        tekst = input("Podaj tekst, który chcesz zaszyfrować: ")
        klucz = int(input("Podaj klucz, którym chcesz szyfrować: "))
        coding = Cezar(tekst=tekst, klucz=klucz)
        coding.coding()

    elif wybor == 2:
        szyfr = input("Podaj tekst, który chcesz odszyfrować: ")
        klucz = input("Podaj klucz, którym chcesz szyfrować lub wpisz 'bez' jesli nie znasz klucza:")
        if klucz == "bez":
            coding = Cezar(szyfr=szyfr)
            coding.decoding2()
        else:
            klucz = int(klucz)
            decoding = Cezar(szyfr=szyfr, klucz=klucz)
            decoding.decoding()

elif wybor == 3:
    print("Teraz wybierz co chcesz zrobic ze swoim tekstem."+"\n"+"1 - jesli chcesz szyfrowac" + "\n" + "2 - jesli chcesz deszyfrowac")
    print()
    wybor = int(input("Wybierz numer: "))

    if wybor == 1:
        tekst = input("Podaj tekst, który chcesz zaszyfrować: ")
        klucz = input("Podaj slowo klucz, którym chcesz szyfrować: ")
        coding = Vigenere(tekst=tekst, klucz=klucz)
        print("Zaszyfrowany tekst: " + coding.coding(), end="")

    elif wybor == 2:
        szyfr = input("Podaj tekst, który chcesz odszyfrować: ")
        klucz = input("Podaj slowo klucz, którym chcesz deszyfrować: ")
        decoding = Vigenere(szyfr=szyfr, klucz=klucz)
        print("Odszyfrowany tekst: " + decoding.decoding(), end="")

elif wybor == 4:
    print("Teraz wybierz co chcesz zrobic ze swoim tekstem."+"\n"+"1 - jesli chcesz szyfrowac" + "\n" + "2 - jesli chcesz deszyfrowac")
    print()
    wybor = int(input("Wybierz numer: "))

    if wybor == 1:
        tekst = input("Podaj tekst, który chcesz zaszyfrować: ")
        coding = Bacon(tekst=tekst)
        print("Zaszyfrowany tekst: " + coding.coding(), end="")

    elif wybor == 2:
        szyfr = input("Podaj tekst, ktory chcesz odszyfrowac: ")
        decoding = Bacon(szyfr=szyfr)
        print("Odszyfrowany tekst: " + str(decoding.decoding()), end="")

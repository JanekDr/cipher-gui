from tlumacz import *
import string


class Enchant:

    def __init__(self, tekst=None, kod=None):
        self.tekst = tekst
        self.kod = kod

    def coding(self):
        cryptogram = ""
        for literka in self.tekst.lower():
            if literka in letters or literka.isspace():
                cryptogram += std_galactic_alphabet[literka]
            elif literka in polish_char:
                cryptogram += std_galactic_alphabet[polish_char[literka]]
            else:
                cryptogram += literka
        return cryptogram

    def decoding(self):
        tj = ""
        for literka in self.kod:
            for key, value in std_galactic_alphabet.items():
                if literka == value:
                    tj += key
                    break
                elif literka in special_char:
                    tj += literka
                elif literka == "||":
                    tj += "y"
                    break
        return tj


class Cezar:

    def __init__(self, klucz=None, tekst=None, szyfr=None):
        self.tekst = tekst
        self.szyfr = szyfr
        self.klucz = klucz

    def coding(self):
        szyfrogram = ""
        for literka in self.tekst:
            if literka in letters:
                if literka.isupper():
                    szyfrogram += chr((ord(literka) - 65 + self.klucz) % 26 + 65)
                else:
                    szyfrogram += chr((ord(literka) - 97 + self.klucz) % 26 + 97)
            elif literka in polish_char:
                szyfrogram += polish_char[literka]
            elif literka.isdigit():
                szyfrogram += chr((ord(literka) - 48 + self.klucz) % 10 + 48)
            else:
                szyfrogram += literka
        return szyfrogram

    def decoding(self):
        tekstjawny = ""
        for literka in self.szyfr:
            if literka in letters:
                if literka.isupper():
                    tekstjawny += chr((ord(literka) - 65 - self.klucz) % 26 + 65)
                else:
                    tekstjawny += chr((ord(literka) - 97 - self.klucz) % 26 + 97)
            elif literka in polish_char:
                tekstjawny += polish_char[literka]
            elif literka.isdigit():
                tekstjawny += chr((ord(literka) - 48 - self.klucz) % 10 + 48)
            else:
                tekstjawny += literka
        return tekstjawny

        
    @staticmethod
    def decoding2(self):
        tekstyjawne = []

        for klucz in range(1, 26):
            tekstjawny = ""
            for literka in self.szyfr.upper():
                if literka.isalpha():
                    tekstjawny += chr((ord(literka)-65-klucz) % 26 + 65)
                elif literka.isdigit():
                    tekstjawny += chr((ord(literka) - 48 + klucz) % 10 + 48)
                else:
                    tekstjawny += literka
            tekstyjawne.append(tekstjawny)

        print("Prawdopodobne teksty jawne:")
        for tj in tekstyjawne:
            print(tj)


class Vigenere:

    def __init__(self, klucz=None, tekst=None, szyfr=None):
        self.klucz = klucz
        self.tekst = tekst
        self.szyfr = szyfr

    @property
    def gen_tab(self):
        alphabet = list(string.ascii_uppercase)
        alphabet2 = list(string.ascii_lowercase)
        tab = []
        tab2 = []

        for j in range(26):
            tab.append([])
            tab2.append([])
            for i in alphabet:
                tab[j].append(i)
            for n in alphabet2:
                tab2[j].append(n)
            znak = alphabet[0]
            znak2 = alphabet2[0]
            alphabet.append(znak)
            alphabet.pop(0)
            alphabet2.append(znak2)
            alphabet2.pop(0)
        return list(tab), list(tab2)

    def gen_key(self):
        klucz = list(self.klucz)
        klucz1 = ""
        if self.tekst is None:
            tekst = self.szyfr
        else:
            tekst = self.tekst

        for literka in klucz:
            if literka in letters:
                klucz1 += literka
        klucz1 = list(klucz1)

        if len(tekst) == len(klucz1):
            print(klucz)
        else:
            for i in range(len(tekst) - len(klucz1)):
                klucz1.append(klucz1[i % len(klucz1)])

        for i in range(len(tekst)):
            if tekst[i].isspace():
                klucz1.insert(i, " ")
            elif tekst[i].isdigit():
                klucz.insert(i, tekst[i])
        klucz1 = "".join(klucz1)

        if len(klucz1) != len(tekst):
            klucz1 = klucz1[:-(len(klucz1)-len(tekst))]
        return klucz1

    def coding(self):
        tab, tab2 = self.gen_tab
        klucz = self.gen_key()
        tekst = self.tekst
        szyfrogram = ""

        for i in range(len(tekst)):
            if tekst[i] in letters:
                if tekst[i].isupper():
                    szyfrogram += tab[ord(tekst[i])-65][ord(klucz[i].upper())-65]
                else:
                    szyfrogram += tab2[ord(tekst[i])-97][ord(klucz[i].lower())-97]
            elif tekst[i] in polish_char:
                znak = polish_char[tekst[i]]
                if znak.isupper():
                    szyfrogram += tab[ord(znak)-65][ord(klucz[i].upper())-65]
                else:
                    szyfrogram += tab2[ord(znak)-97][ord(klucz[i].lower())-97]
            else:
                szyfrogram += tekst[i]
        return szyfrogram

    def decoding(self):
        tab, tab2 = self.gen_tab
        klucz = self.gen_key()
        szyfr = self.szyfr
        tekst_jawny = ""
        print(klucz)
        print(szyfr)
        for j in range(len(klucz)):
            if szyfr[j] in letters:
                if szyfr[j].isupper():
                    for i in range(26):

                        if tab[ord(klucz[j].upper())-65][i] == szyfr[j]:
                            tekst_jawny += tab[0][i]
                else:
                    for i in range(26):
                        if tab2[ord(klucz[j].lower())-97][i] == szyfr[j]:
                            tekst_jawny += tab2[0][i]
            elif szyfr[j] in polish_char:
                tekst_jawny += polish_char[szyfr[j]]
            else:
                tekst_jawny += szyfr[j]
        return tekst_jawny


class Bacon:
    def __init__(self, tekst=None, szyfr=None):
        self.tekst = tekst
        self.szyfr = szyfr

    def coding(self):
        szyfrogram = ""
        for literka in self.tekst:
            if literka in letters:
                szyfrogram += bacon[literka.upper()]
            elif literka in polish_char:
                szyfrogram += bacon[polish_char[literka.upper()]]
            else:
                szyfrogram += literka
        return szyfrogram

    def decoding(self):
        szyfry = self.szyfr.split()
        tekst_jawny = ""
        for szyfr in szyfry:
            for i in range(0, len(szyfr), 5):
                wyraz = szyfr[i:i+5]
                for key, value in bacon.items():
                    if wyraz == value:
                        tekst_jawny += key
                        break
            tekst_jawny += " "
        return tekst_jawny

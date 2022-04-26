"""
Aplikacja szyfrowania i deszyfrowania
Author: Jan Druszcz
"""

from tkinter import *
from tkinter import ttk
from szyfry_logika import *
from tkinter import messagebox
from tkinter import scrolledtext
import pyperclip
from datetime import datetime


okno = Tk()
okno.title("Aplikacja szyfrowania i deszyfrowania")
okno.resizable(False, False)
okno.configure(bg="#2f3136")

font = "Calibri 12"

obramowka = LabelFrame(okno, highlightbackground="#829297", bg="#2f3136", height=120, width=260, text="Tryby:", font=font, fg="#829297")
obramowka.grid(row=1, rowspan=2, columnspan=2, column=2)

obramowka2 = LabelFrame(okno, highlightbackground="#829297", bg="#2f3136", height=120, width=260, text="Wybór szyfru:", font=font, fg="#829297")
obramowka2.grid(row=1, rowspan=2, columnspan=2, column=0, ipady=5, padx=25)

rodzaje_szyfrow = ttk.Combobox(obramowka2, value=rodzaje, font=font, justify='center')
rodzaje_szyfrow.current(1)
rodzaje_szyfrow.tk_setPalette(background="#2f3136", foreground="#829297")
rodzaje_szyfrow.grid(row=1, column=0, ipadx=25)
puste1 = Label(obramowka2).grid(row=0, column=0)
puste2 = Label(obramowka2).grid(row=3, column=0)


okienko = Label(okno, text="ENIGMATOR 3000", anchor="n", font="Calibri 28", bg="#2f3136", width=15, height=2, bd=1, fg="#829297")
okienko.grid(row=0, column=1)


pustepole = Label(okno, text="", bg="#2f3136").grid(row=3, column=1, pady=12)


def click_f(event):
    wejscie.config(state=NORMAL)
    wejscie.delete("1.0", END)


def click_f2(event):
    klucz.config(state=NORMAL)
    klucz.delete(0, END)


def clear_f():
    print("{} użyto przycisku CLEAR".format(datetime.now().strftime('%H:%M:%S')))
    wejscie.delete("1.0", END)
    klucz.delete(0, END)
    wyjscie.delete("1.0", END)
    wejscie.insert("1.0", "Podaj tekst")
    wejscie.config(state=DISABLED)
    klucz.insert(0, "Podaj klucz")


def copy_f():
    print("{} użyto przycisku COPY".format(datetime.now().strftime('%H:%M:%S')))
    pyperclip.copy(wyjscie.get('1.0', END)[:-1])


def check_cmbbox():
    if rodzaje_szyfrow.get() == "Szyfr podstawieniowy":
        return 1
    elif rodzaje_szyfrow.get() == "Enchanting Language Minecraft":
        return 0
    elif rodzaje_szyfrow.get() == "Szyfr Vigenère’a":
        return 2
    elif rodzaje_szyfrow.get() == "Szyfr Bacona":
        return 3


def check_key():
    try:
        int(klucz.get())
        return True
    except:
        messagebox.showerror("Nieprawidłowy format klucza.", "Podałeś nieprawidłowy format klucza dla danego szyfru. Wprowadź poprawny.")
        return False


def check_fields():
    if check_cmbbox() == 0 or check_cmbbox() == 3:
        if wejscie.get('1.0', END)[:-1] == "":
            return False
        else:
            return True

    if wejscie.get('1.0', END)[:-1] == "" and (klucz.get() == "" or klucz.get() == "Podaj klucz"):
        messagebox.showerror("BRAK DANYCH", "Wprowadź brakujące dane!\n Podaj tekst i klucz.")
        return False
    elif wejscie.get('1.0', END)[:-1] == "":
        messagebox.showerror("BRAK DANYCH", "Wprowadź brakujące dane!\n Podaj tekst.")
        return False
    elif klucz.get() == "" or klucz.get() == "Podaj klucz":
        messagebox.showerror("BRAK DANYCH", "Wprowadź brakujące dane!\n Podaj klucz.")
        return False
    else:
        return True


def enter_coding():
    if check_fields():
        if check_cmbbox() == 0:
            if var.get() == 0:
                tekst = wejscie.get('1.0', END)[:-1]
                coding = Enchant(tekst=tekst)
                wynik = coding.coding()
                print('{}: zaszyfrowano wiadomosc: "{}", na "{}" szyfrem: {}.'
                      .format(datetime.now().strftime('%H:%M:%S'), tekst, wynik, rodzaje_szyfrow.get()))
                wyjscie.delete("1.0", END)
                wyjscie.insert("1.0", str(wynik))
            else:
                kod = wejscie.get('1.0', END)[:-1]
                decoding = Enchant(kod=kod)
                wynik = decoding.decoding()
                print('{}: odszyfrowano wiadomosc: "{}", na "{}" szyfrem: {}.'
                      .format(datetime.now().strftime('%H:%M:%S'), kod, wynik, rodzaje_szyfrow.get()))
                wyjscie.delete("1.0", END)
                wyjscie.insert("1.0", str(wynik))

        elif check_cmbbox() == 1:
            if check_key():
                if var.get() == 0:
                    tekst = wejscie.get('1.0', END)[:-1]
                    klucz1 = klucz.get()
                    coding = Cezar(tekst=tekst, klucz=int(klucz1))
                    wynik = coding.coding()
                    print('{}: zaszyfrowano wiadomosc: "{}" kluczem "{}", na "{}" szyfrem: {}.'
                          .format(datetime.now().strftime('%H:%M:%S'), tekst, klucz1, wynik, rodzaje_szyfrow.get()))
                    wyjscie.delete("1.0", END)
                    wyjscie.insert("1.0", str(wynik))
                else:
                    szyfr1 = wejscie.get('1.0', END)[:-1]
                    klucz1 = klucz.get()
                    decoding = Cezar(szyfr=szyfr1, klucz=int(klucz1))
                    wynik = decoding.decoding()
                    print('{}: odszyfrowano wiadomosc: "{}" kluczem "{}", na "{}" szyfrem: {}.'
                          .format(datetime.now().strftime('%H:%M:%S'), szyfr1, klucz1, wynik, rodzaje_szyfrow.get()))
                    wyjscie.delete("1.0", END)
                    wyjscie.insert("1.0", str(wynik))

        elif check_cmbbox() == 2:
            if var.get() == 0:
                tekst = wejscie.get('1.0', END)[:-1]
                klucz1 = klucz.get()
                coding = Vigenere(tekst=tekst, klucz=klucz1)
                wynik = coding.coding()
                print('{}: zaszyfrowano wiadomosc: "{}" kluczem "{}", na "{}" szyfrem: {}.'
                      .format(datetime.now().strftime('%H:%M:%S'), tekst, klucz1, wynik, rodzaje_szyfrow.get()))
                wyjscie.delete("1.0", END)
                wyjscie.insert("1.0", str(wynik))
            else:
                szyfr1 = wejscie.get('1.0', END)[:-1]
                klucz1 = klucz.get()
                decoding = Vigenere(szyfr=szyfr1, klucz=klucz1)
                wynik = decoding.decoding()
                print('{}: odszyfrowano wiadomosc: "{}" kluczem "{}", na "{}" szyfrem: {}.'
                      .format(datetime.now().strftime('%H:%M:%S'), szyfr1, klucz1, wynik, rodzaje_szyfrow.get()))
                wyjscie.delete("1.0", END)
                wyjscie.insert("1.0", str(wynik))

        elif check_cmbbox() == 3:
            if var.get() == 0:
                tekst = wejscie.get('1.0', END)[:-1]
                coding = Bacon(tekst=tekst)
                wynik = coding.coding()
                print('{}: zaszyfrowano wiadomosc: "{}", na "{}" szyfrem: {}.'
                      .format(datetime.now().strftime('%H:%M:%S'), tekst, wynik, rodzaje_szyfrow.get()))
                wyjscie.delete("1.0", END)
                wyjscie.insert("1.0", str(wynik))
            else:
                szyfr1 = wejscie.get('1.0', END)[:-1]
                decoding = Bacon(szyfr=szyfr1)
                wynik = decoding.decoding()
                print('{}: odszyfrowano wiadomosc: "{}", na "{}" szyfrem: {}.'
                      .format(datetime.now().strftime('%H:%M:%S'), szyfr1, wynik, rodzaje_szyfrow.get()))
                wyjscie.delete("1.0", END)
                wyjscie.insert("1.0", str(wynik))


def decoding_f():
    print("{} zmieniono tryb na deszyfrowanie.".format(datetime.now().strftime('%H:%M:%S')))
    strvar.set("Wpisz szyfr poniżej:")
    strvar2.set("Odszyfrowany tekst:")


def coding_f():
    print("{} zmieniono tryb na szyfrowanie.".format(datetime.now().strftime('%H:%M:%S')))
    strvar.set("Wpisz tekst poniżej:")
    strvar2.set("Zaszyfrowany tekst:")


var = IntVar()
szyfr = Radiobutton(obramowka, text="Szyfrowanie    ", font=font, variable=var, value=0, command=coding_f, bg="#2f3136", fg="#829297")
deszyfr = Radiobutton(obramowka, text="Deszyfrowanie", font=font, variable=var, value=1, command=decoding_f, bg="#2f3136", fg="#829297")
szyfr.grid(row=0, columnspan=2, column=0, ipadx=10)
deszyfr.grid(row=1, columnspan=2, column=0)


klucz = Entry(okno, bd=7, bg="#34373c")
klucz.insert(0, "Podaj klucz")
# klucz.config(state=DISABLED)
klucz.bind("<Button-1>", click_f2)
klucz.grid(row=5, column=1, padx=10, pady=10, ipady=7)

strvar = StringVar()
strvar2 = StringVar()
napis = Label(okno, text="Wpisz klucz ponizej:", font=font, bg="#2f3136", fg="#829297").grid(row=4, column=1)
napis2 = Label(okno, textvariable=strvar, font=font, bg="#2f3136", fg="#829297").grid(row=4, column=0)
napis3 = Label(okno, textvariable=strvar2, font=font, bg="#2f3136", fg="#829297").grid(row=4, column=2)
strvar.set("Wpisz tekst poniżej:")
strvar2.set("Zaszyfrowany tekst:")

enter = Button(okno, text="ENTER", bg="#43b581", bd=7, command=enter_coding, font=font, fg="white").grid(row=6, column=0, pady=5)
clear = Button(okno, text="CLEAR", bg="#f04747", bd=7, command=clear_f, font=font, fg="white").grid(row=6, column=1, pady=5)
copy = Button(okno, text="COPY", bg="#7289da", bd=7, command=copy_f, font=font, fg="white").grid(row=6, column=2, pady=5)

wejscie = scrolledtext.ScrolledText(okno, bd=7, width=10, height=5, bg="#34373c")
wejscie.insert("1.0", "Podaj tekst")
wejscie.configure(state="disabled")
wejscie.bind("<Button-1>", click_f)
wejscie.grid(row=5, column=0, padx=10, pady=10, ipadx=70, ipady=10)

wyjscie = scrolledtext.ScrolledText(okno, bd=7, width=10, height=5, bg="#34373c")
wyjscie.config()
wyjscie.grid(row=5, column=2, padx=10, pady=10, ipadx=70, ipady=10)

# okno.iconbitmap(r'C:\Users\48531\Pictures\icon_app.ico')

okno.mainloop()

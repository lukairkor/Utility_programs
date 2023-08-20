#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Apr 16 15:37:12 2021
Koszt, zysk, marza, narzut
@author: lukas
"""
import enquiries
import os

# if __name__ == "__main__":

options = ['Oblicz', 'Wyjdz']
while True:
    choice = enquiries.choose('Choose one of these options: ', options)

    if choice == options[0]:
        try:
            koszt = int(input("Wpisz koszt:"))
            zysk = int(input("Wpisz zysk:\n"))

            os.system('clear')

            marza = (zysk - koszt) / zysk
            marza = marza * 100
            print("Marza wynosi:", round(marza), "%")

            narzut = ((zysk - koszt) / koszt) * 100
            print("Narzut wynosi:", round(narzut), "%")

            koszt = zysk * (1 - marza / 100)
            print("Koszt:", round(koszt, 0), "zl")

            zysk = koszt / (1 - marza / 100)
            print("Zysk:", round(zysk, 0), "zl")
        except:
            print("Bad input!")


    elif choice == options[1]:
        print("See you soon!")
        break

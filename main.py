import random as rd
import os

def cls():
    os.system("cls")

pilihanSuit = ["gunting", "batu", "kertas"]

lawan = rd.choice(pilihanSuit)

print("Selamat Datang Di Game Gunting, Batu, Kertas!\n\n\n")
print("Masukkan pilihan gunting / batu / kertas")
userInput = str(input("> "))

if userInput == lawan:
    print("\n\n\nAnda seri! lawan anda memilih pilihan yang sama!")

elif userInput == "gunting":
    if lawan == "batu":
        cls()
        print(f"Anda kalah! lawan anda memilih {lawan}\n\n\n")
    
    elif lawan == "kertas":
        cls()
        print(f"Anda menang! lawan anda memilih {lawan}\n\n\n")

elif userInput == "batu":
    if lawan == "gunting":
        cls()
        print(f"Anda menang! lawan anda memilih {lawan}\n\n\n")
    
    elif lawan == "kertas":
        cls()
        print(f"Anda kalah! lawan anda memilih {lawan}\n\n\n")

elif userInput == "kertas":
    if lawan == "gunting":
        cls()
        print(f"Anda kalah! lawan anda memilih {lawan}\n\n\n")
    
    elif lawan == "batu":
        cls()
        print(f"Anda menang! lawan anda memilih {lawan}\n\n\n")

else:
    print("\n\n\n\nMasukkan pilihan yang benar!!")
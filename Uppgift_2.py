# Tentamen 2024-08-19 - 2024-08-20 Uppgift 2 (5p)
print('Uppgift 2\n')
from random import randint

# Kom ihåg: Du får använda modulen ”random” i denna uppgift
# Skriv kod för ditt program med utskrift här:
length = int(input("Ange antal tecken som ska skapas: "))
random_letters = []
counter = 0
choice = input("Skriv in bokstaven som ska antalet förekomsten av den beräknas: ")
for i in range(0,length):
    random_letter = randint(ord('a'), ord('z'))
    random_letters.append(chr(random_letter))
    if choice == chr(random_letter):
        counter +=1
print("Förekomsten av", choice, "i listan ", random_letters, "är lika med", counter)

    
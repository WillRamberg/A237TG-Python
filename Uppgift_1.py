# Tentamen 2024-08-19 - 2024-08-20 Uppgift 1 (5p)
print('Uppgift 1\n')
import math

# Kom ihåg: Du får använda modulen ”Math” i denna uppgift.
# Skriv kod för ditt program med utskrift här:

def V_Klot(r):
    return 4* math.pi * r**3 / 3
#Functions to calculate Volume and Area using given formula
def A_Klot(r):
    return 4 * math.pi * r**2

def main():
    choice = 0
    while choice != 3:
        print("1. Beräkna klotets volym \n2. Beräkna klotets area \n3. Avsluta programmet.")
        choice = int(input("Ange det meny alternativet du vill köra: "))
        if choice == 1:
            r = int(input("Ange värdet på radien: "))
            print(f"Volymen av klotet är: {V_Klot(r):.2f} cm^3") #Calls function to return and print Volume using V_Klot(r)
        elif choice == 2:
            r = int(input("Ange värdet på radien: "))
            print(f"Arean av klotet är: {A_Klot(r):.2f} cm^2") #Calls function to return and print Area using A_Klot(r)
        elif choice == 3:
            print("Avslutar programmet")
            break

main()
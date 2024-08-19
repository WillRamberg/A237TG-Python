# Tentamen 2024-08-19 - 2024-08-20 Uppgift 3 (6p)
from random import randint
print('Uppgift 3\n')
# OBS! I denna uppgift är det inte tillåtet att använda funktionerna min(), max() och sum() 
# för att beräkna minimum, maximum och medelvärde.  

# Skriv kod för ditt program med utskrift här:
length = int(input("Ange längden av raden: "))
array = []
maxes, mins, sums = [], [], []
for i in range(0,length):
    insidearray = []
    sum = 0
    max = -1
    min = 10000000000000
    for j in range(0, length):
        tmp = randint(0,100*length)
        sum += tmp
        if max < tmp or max == None:
            max = tmp
        if min > tmp or min == None:
            min = tmp
        insidearray.append(tmp)
    sums.append(sum)
    maxes.append(max)
    mins.append(min)
    array.append(insidearray)
print(array)

print("Radnummer \tminimum \tmaximum \tMedelvärde")
for i in range(0, length):
    print(i, "\t", mins[i], "\t", maxes[i], "\t", sums[i]/length)
    print("-"*50)
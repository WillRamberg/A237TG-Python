# Tentamen 2024-08-19 - 2024-08-20 Uppgift 3 (6p)
from random import randint
import matplotlib.pyplot as plt
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

header= f"{'Radnummer':<10} {'minimum':>10} {'maximum':>10} {'Medelvärde':>15}"
seperator = "-" * len(header)
print(header)
for i in range(0, length):
    print(f"{i:<13} {mins[i]:<10.2f} {maxes[i]:<12.2f} {sums[i]/length:.2f}")
    print(seperator)

x = list(range(length))
plt.bar(x, maxes, width=0.4, label='Max', align='center')
plt.bar(x, mins, width=0.4, label='Min', align='center')

plt.xlabel('Index av listan')
plt.ylabel('Minsta och högsta')
plt.title('Minsta och högsta värdena av listan')
plt.xticks(x)
plt.legend()

plt.show()
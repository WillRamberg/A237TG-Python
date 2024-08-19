# Tentamen 2024-08-19 - 2024-08-20 Uppgift 5 (20p)
import csv
print('Uppgift 5\n')

# OBS! Inga andra importerade moduler än csv och matplotlib.pyplot får användas för att lösa nedanstående uppgifter.

# Skriv kod för ditt program med utskrift här:
def read_file(filename):
    data_list = []
    with open (filename, 'r') as file:
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader: 
            data_list.append(row)
    return data_list

inkomstData = read_file("inkomster.csv")
for i in range(0,3):
    print(inkomstData[i])

#C

def calc_min(list):
    min=list[0][2]
    for i in range(0, len(list)):
        if min > list[i][2]:
            min = list[i][2]
    return min

def calc_max(list):
    max=list[0][2]
    for i in range(0, len(list)):
        if max < list[i][2]:
            max = list[i][2]
    return max

def calc_avg(list):
    sum = 0
    for i in range(0, len(list)):
        sum += float(list[i][2])
    return round(sum / len(list), 2)

def calc_median(list):
    second_elements = []
    sorted_list = []
    second_elements = [sublist[2] for sublist in list]
    sorted_list = sorted(second_elements)
    length = len(sorted_list)
    if length % 2 == 1:
        return sorted_list[length // 2]
    else:
        mid1 = sorted_list[length // 2 - 1]
        mid2 = sorted_list[length // 2]
        return (float(mid1) + float(mid2)) / 2

men = []
women = []
for i in range(1,91):
    if(inkomstData[i][0] == "män"):
        men.append(inkomstData[i])
    else:
        women.append(inkomstData[i])

print("\n|Kön\t|Mininkomst\t|Maxinkomst\t|Medelinkomst\t|Medianinkomst")
print("+-------+---------------+---------------+---------------+----------------")
print(f"|Man    |{calc_min(men):<14} |{calc_max(men):<14} |{calc_avg(men):<14} |{calc_median(men):<13}")
print("+-------+---------------+---------------+---------------+----------------")
print(f"|Kvinna |{calc_min(women):<14} |{calc_max(women):<14} |{calc_avg(women):<14} |{calc_median(women):<13}")

#D
def calc_min_index(list):
    min=list[0][2]
    index = 0
    for i in range(0, len(list)):
        if min > list[i][2]:
            min = list[i][2]
            index = i
    return min, index

def calc_max_index(list):
    max=list[0][2]
    index = 0
    for i in range(0, len(list)):
        if max < list[i][2]:
            max = list[i][2]
            index = i
    return max, index

print("|Mininkomst|Min år   |Maxinkomst |Max år")
print("+----------+---------+-----------+---------")
min, min_age = calc_min_index(men)
max, max_age = calc_max_index(men)
print(f"|{min:<9} |{men[min_age][1]:<8} |{max:<10} |{men[max_age][1]:<5}")

min, min_age = calc_min_index(women)
max, max_age = calc_max_index(women)
print(f"|{min:<9} |{women[min_age][1]:<8} |{max:<10} |{women[max_age][1]:<9}")
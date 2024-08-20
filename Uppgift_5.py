# Tentamen 2024-08-19 - 2024-08-20 Uppgift 5 (20p)
import csv
print('Uppgift 5\n')

# OBS! Inga andra importerade moduler än csv och matplotlib.pyplot får användas för att lösa nedanstående uppgifter.

# Skriv kod för ditt program med utskrift här:
def read_file():
    filename="inkomster.csv"
    data_list = []
    with open (filename, 'r') as file: #opens the file with attribute read - r
        csv_reader = csv.reader(file, delimiter = ',')
        for row in csv_reader: 
            data_list.append(row) #for every row it adds the rows data into the created list
    return data_list

inkomstData = read_file()
for i in range(0,3):
    print(inkomstData[i]) #loops to print the first three elements

#C
#following definitions to calculate min, max, average and median
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
    if length % 2 == 1: #if odd number of elements, it takes the middle element as median
        return sorted_list[length // 2]
    else:
        mid1 = sorted_list[length // 2 - 1] #if even amount of elements, it takes the two middle elements, add these and then divide by 2
        mid2 = sorted_list[length // 2]
        return (float(mid1) + float(mid2)) / 2

men = []
women = []
for i in range(1,len(inkomstData)):
    if(inkomstData[i][0] == "män"): #sorts the whole list into their specific genders as list
        men.append(inkomstData[i])
    else:
        women.append(inkomstData[i])

print("\n|Kön\t|Mininkomst\t|Maxinkomst\t|Medelinkomst\t|Medianinkomst")
print("+-------+---------------+---------------+---------------+----------------")
print(f"|Man    |{calc_min(men):<14} |{calc_max(men):<14} |{calc_avg(men):<14} |{calc_median(men):<13}") #using the gender lists and the calculation funcitons i print the results
print("+-------+---------------+---------------+---------------+----------------")
print(f"|Kvinna |{calc_min(women):<14} |{calc_max(women):<14} |{calc_avg(women):<14} |{calc_median(women):<13}")

#D
def calc_min_index(list):
    min=list[0][2]
    index = 0
    for i in range(0, len(list)):
        if min > list[i][2]:
            min = list[i][2]
            index = i #i is the index value of the min that was found
    return min, index #caluclates min but also keeps the index value and returns this

def calc_max_index(list):
    max=list[0][2]
    index = 0
    for i in range(0, len(list)):
        if max < list[i][2]:
            max = list[i][2]
            index = i #i is the index value of the max that was found
    return max, index #calculates max but also keeps the index value and returns this

print("\n|Mininkomst|Min år   |Maxinkomst |Max år")
print("+----------+---------+-----------+---------")
min, min_age = calc_min_index(men)
max, max_age = calc_max_index(men)
#prints min and max that was calculated and using the index value also finds the age inside the list (men[MIN AGE INDEX][1] because 1 is index spot of age)
print(f"|{min:<9} |{men[min_age][1]:<8} |{max:<10} |{men[max_age][1]:<5}")
print("+----------+---------+-----------+---------")
min, min_age = calc_min_index(women)
max, max_age = calc_max_index(women)
print(f"|{min:<9} |{women[min_age][1]:<8} |{max:<10} |{women[max_age][1]:<9}")
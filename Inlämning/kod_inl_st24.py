# Skriv en inledande kommentar som talar om vad programmet gör. 


# Placera dina modulimpoter här:
import csv
import matplotlib.pyplot as plt

# Placera ev. funktioner som används i flera deluppgifter här:
# Skriv din ev. kod här:

# Deluppgift 1: Funktioner från deluppgift 1 i ordning.
# Skriv din kod här:

def read_file(filename):
    data_list = [] #creates list where the files data will be stored
    with open (filename, 'r') as file: #opens the file with attribute read - r
        csv_reader = csv.reader(file, delimiter = ';')
        for row in csv_reader: 
            data_list.append(row) #for every row it adds the rows data into the created list
    return data_list

# Deluppgift 2: Funktioner från deluppgift 2 i ordning.
# Skriv din kod här:
def plottaKPI(data):

    years = [int(row[0]) for row in data[1:]]
    months = [int(months) for months in input("Ange vilka månader som ska analyseras: ").split(", ")] #allows user to enter more than one value
    for month in months:
        if month in range(1, 13):
            monthly_value = [float(row[int(month)].replace(',', '.')) for row in data[1:]] #takes all values for each specific month enterd
            plt.plot(years, monthly_value, label = data[0][month])
        elif month == 13:
            monthly_value = [float(row[int(13)].replace(',', '.')) for row in data[1:]]
            plt.plot(years, monthly_value, label = data[0][13])
    plt.legend()
    plt.title("Konsumentprisindex År 1980-2023")
    plt.xlabel("År")
    plt.ylabel("Konsumentprisindex")
    plt.grid(True)
    plt.show()

# Deluppgift 3: Funktioner från deluppgift 3 i ordning.
# Skriv din kod här:
def varortjanster(data):
    start, end = [int(x) for x in input("Ange mellan vilka år analysen omfattar (ex: 1996-2023): ").split("-")] #allows user to choose the two years and splits it between -
    print(start, end)
    years = [int(value.replace(',', '.')) for value in data[0][start-1979:end-1978]] #takes all values between the start year and end year (-1979 since I use indexes)
    print("Varu-/tjänstegrupp \n1. livsmedel och alkoholfria drycker \n2. kläder och skor \n3. boende \n4. hälso- och sjukvård \n5. post och telekommunikationer \n6. rekreation och kultur \n7. restauranger och logi")
    groups = [int(groups) for groups in input("Ange Varu-/tjänstegrupper som ska analyseras: ").split(", ")]

    for group in groups:
        if group in range (1,8):
            group_data = [float(value.replace(',', '.')) for value in data[group][start-1979:]] #data for each group
            group_years = [year for year in years]
            values = group_data[years.index(start):years.index(end)+1]
            plt.plot(group_years, values, label=data[group][0])
    plt.legend()
    plt.title("Prisutvecklingen för olika kategorier av varor och tjänster År" + str(start) + "-" + str(end))
    plt.xlabel("År")
    plt.ylabel("Prisutveckling")
    plt.grid(True)
    plt.show()


# Deluppgift 4: Funktioner från deluppgift 4 i ordning.
# Skriv din kod här:

def ff(data):
    print("Varu-/tjänstegrupp \n1. livsmedel och alkoholfria drycker \n2. kläder och skor \n3. boende \n4. hälso- och sjukvård \n5. post och telekommunikationer \n6. rekreation och kultur \n7. restauranger och logi")
    group_choice = int(input("Ange kategori (1-7) som ska analyseras: "))
    group_data = [0]
    years = list(range(1980, 2024))
    for i in range(2, 45): #skips the first step since it would be / 0 anyways
        calculation = ((float(data[group_choice][i])-float(data[group_choice][i-1]))/float(data[group_choice][i-1])) * 100 #takes the exact expression
        group_data.append(calculation)

    fig = plt.figure(figsize = (10, 5))
    plt.bar(years, group_data)
    plt.grid(True)
    plt.xlabel("År")
    plt.ylabel("Förändingsfaktor")
    plt.title("Förändringsfaktor för " + data[group_choice][0])
    plt.show()

# Deluppgift 5: Funktioner från deluppgift 5 i ordning.
# Skriv din kod här:

def statistik(data):
    means = []
    medians = []
    maxes = []
    groups = []
    for i in range(1, 8):
        groups.append(data[i][0]) #loops through 1-8 for all the different groups, and saves their name (found on index 0) into a list with all groups
        sum = 0.00
        for j in range(1, 45): #loops thorugh all the years (1980 - 2023) using their indexes
            sum += float(data[i][j])
        means.append(sum / (len(data[i]) - 1)) #calculates mean and adds into the list
        sort = sorted(data[i][1:]) #makes a new list with the data that is sorted, but without the name (index 0) to be able to calculate median
        medians.append((float(sort[21]) + float(sort[22]))/2) #calculates median and adds into the list
        maxes.append(float(max(sort))) #calculates max and adds into the list

    fig, ax = plt.subplots()
    bars_max = ax.bar(groups, maxes, width=0.75, label='Max', color='blue')
    bars_median = ax.bar(groups, medians, width=0.5, label='Median', color='red') #plots all the different bars (max, median and mean)
    bars_mean = ax.bar(groups, means, width=0.25, label='Mean', color='green')

    ax.set_ylabel('Values')
    ax.set_title('Nested Bar Graph for Mean, Median, and Max')
    y_max = max(maxes)
    y_ticks = range(0, int(y_max) + 100, 100) #changes so the bar graph starts from 0 and ends att the highest point it will reach with all graphs. Then makes it jump with 100
    ax.set_yticks(y_ticks)
    ax.set_xticks(groups)
    plt.xticks(rotation=20)
    ax.set_xticklabels(groups)
    ax.legend()

    # Show plot
    plt.show()

# Huvudprogram med Meny från deluppgift 0. Använd menyrubriker enl. uppgiftsbeskrivningen.
# Skriv din kod här:
menu_choice = 0
kpiData = read_file("kpi2023.csv")
livsData = read_file("Varutjanstegrupp.csv")
while menu_choice != 6:
    titel = "Meny"
    print(f'{titel:^20}')
    font = "===="
    print(f'{font:^20}')
    print("1. Hämta data från fil \n2. Analysera data \n3. Analysera data \n4. Analysera data \n5. Analysera data \n6. Avsluta")
    menu_choice = int(input("Välj menyalternativ (1-6): "))
    if menu_choice == 1:
        kpiData = read_file("kpi2023.csv")
    elif menu_choice == 2:
        plottaKPI(kpiData)
    elif menu_choice == 3:
        varortjanster(livsData)
    elif menu_choice == 4:
        ff(livsData)
    elif menu_choice == 5:
        statistik(livsData)
    elif menu_choice == 6:
        print("Avslutar programmet!")
    else:
        print("Ange en annan siffra!")
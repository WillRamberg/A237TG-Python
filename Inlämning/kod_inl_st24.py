# Skriv en inledande kommentar som talar om vad programmet gör. 


# Placera dina modulimpoter här:
import csv
import matplotlib.pyplot as plt

# Placera ev. funktioner som används i flera deluppgifter här:
# Skriv din ev. kod här:

def read_file(filename):
    data_list = []
    with open (filename, 'r') as file:
        csv_reader = csv.reader(file, delimiter = ';')
        for row in csv_reader:
            data_list.append(row)
    return data_list

# Deluppgift 1: Funktioner från deluppgift 1 i ordning.
# Skriv din kod här:


# Deluppgift 2: Funktioner från deluppgift 2 i ordning.
# Skriv din kod här:
def plot_table(data):

    years = [int(row[0]) for row in data[1:]]
    months = [int(months) for months in input("Ange vilka månader som ska analyseras: ").split(", ")]
    for month in months:
        if month in range(1, 13):
            monthly_value = [float(row[int(month)].replace(',', '.')) for row in data[1:]]
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


# Deluppgift 4: Funktioner från deluppgift 4 i ordning.
# Skriv din kod här:


# Deluppgift 5: Funktioner från deluppgift 5 i ordning.
# Skriv din kod här:


# Huvudprogram med Meny från deluppgift 0. Använd menyrubriker enl. uppgiftsbeskrivningen.
# Skriv din kod här:
menu_choice = 0
while menu_choice != 6:
    kpiData = read_file("kpi2023.csv")
    titel = "Meny"
    print(f'{titel:^20}')
    font = "===="
    print(f'{font:^20}')
    print("1. Hämta data från fil \n2. Analysera data \n3. Analysera data \n4. Analysera data \n5. Analysera data \n6. Avsluta")
    menu_choice = int(input("Välj menyalternativ (1-6): "))
    if menu_choice == 1:
        kpiData = read_file("kpi2023.csv")
    elif menu_choice == 2:
        plot_table(kpiData)
    elif menu_choice == 3:
        print("Good")
    elif menu_choice == 4:
        print("Good")
    elif menu_choice == 5:
        print("Good")
    elif menu_choice == 6:
        print("Avslutar programet!")
    else:
        print("Ange en annan siffra!")
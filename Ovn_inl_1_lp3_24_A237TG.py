#För den tredje utskriften behöver programmet uppdateras så att denna lista får samma struktur som den andra listan (alla värden måste vara tal).
#kpi_10 = [['År', 'Jan', 'Feb', 'Mar', 'Apr', 'Maj', 'Jun', 'Jul', 'Aug', 'Sep', 'Okt', 'Nov', 'Dec'], ['2019', '328.56', '331.02', '331.79', '334.11', '334.95', '334.47', '335.8', '334.39', '335.95', '336.04', '336.36', '337.68'], ['2018', '322.51', '324.87', '325.76', '327.1', '327.86', '328.62', '330.33', '329.63', '331.14', '330.72', '330.4', '331.87'], ['2017', '317.5', '319.73', '319.68', '321.54', '321.74', '321.97', '323.69', '323.18', '323.62', '323.38', '324.04', '325.23'], ['2016', '313.13', '314.14', '315.7', '315.64', '316.21', '316.54', '316.73', '316.38', '316.91', '318', '318.1', '319.68'], ['2015', '310.75', '312.93', '313.19', '313.16', '314.24', '313.33', '313.43', '312.81', '314.06', '314.29', '313.75', '314.21'], ['2014', '311.39', '312.7', '312.68', '313.89', '314.05', '314.7', '313.67', '313.35', '313.85', '314.02', '313.56', '314.05'], ['2013', '312', '313.39', '314.65', '314.03', '314.54', '313.99', '313.55', '313.84', '315.05', '314.4', '314.2', '315.04'], ['2012', '311.85', '313.92', '314.8', '315.49', '315.23', '314.45', '313.23', '313.55', '314.81', '314.59', '313.82', '314.61'], ['2011', '306.15', '308.02', '310.11', '311.44', '312.02', '311.28', '311.13', '311.23', '313.41', '313.42', '314.16', '314.78'], ['2010', '299.79', '301.59', '302.32', '302.36', '302.92', '302.97', '302.04', '302.06', '304.6', '305.57', '306.58', '308.73']]
kpi_10 = [['R/K', 'K1', 'K2', 'K3'], ['R1', 1, 2, 3], ['R2', 10, 20, 30], ['R3', 300, 500, 400]]

def print_lista(kpi_10): # Skriver ut en 2D-lista (för tredje varianten med rubriker som text och värden som tal). 
    # Parameter: En 2D-lista med rubriker i första raden och första kolumnen att skriva ut. 
    # Returvärde: Inget

    print('\nHela listan\n') 
    print(kpi_10) # Skriver ut hela listan i en utskrift utan radvis radbrytning

    print('\nListan radvis\n')
    for row in kpi_10: # Skriver ut hela listan med radbrytning för varje rad
        print(row)
    
    print('\nListan radvis med f-string och snygga kolumner\n') #Bredden på kolumnerna i utskriften behöver anpassas efter listan.
    for rubrik in kpi_10[0]: # Skriver ut rubrikrad med texten centrerad över kolumnen
        print(f'{rubrik:^10}', end = '')
    print(' ')
    for row in kpi_10[1:]: # Skriver ut resten av listan text vänsterjusterad och tal högerjusrterade
        for i in row:
            print(f'{i:10}', end = '')
        print(' ')
    return None

# Skriv din kod här:

def mean_value(list):
    for row in list[1:]:
        sum = 0
        for col in row[1:]:
            sum = sum + int(col)
        row.append(sum / (len(row) -1))
    for row in kpi_10: # Skriver ut hela listan med radbrytning för varje rad
        print(row)

def sum_value(list):
    new_list = []
    for row in list[1:]:
        sum = 0
        for col in row[1:]:
            sum = sum + int(col)
        new_list.append(sum)
    print(new_list)

def find_max(list):
    biggest_list = []
    for row in list[1:]:
        biggest = [0,0]
        counter = 1
        for col in row[1:]:
            counter +=1
            if biggest[0] < int(col):
                biggest[0] = col
                biggest[1] = counter
        biggest_list.append(biggest)
    print(biggest_list)

def find_min(list):
    new_list = []
    for row in list[1:]:
        smallest = [100000000000,0]
        counter = 1
        for col in row[1:]:
            counter +=1
            if smallest[0] > int(col):
                smallest[0] = col
                smallest[1] = counter
        new_list.append(smallest)
    print(new_list)


menu_choice = 0

while menu_choice != 6:
    print("1. Skriv ut listan. \n2. Beräkna summa.\n3. Beräkna medelvärde.\n4. Hitta största värdet.\n5. Hitta minsta värdet. \n6. Avsluta programmet.")
    menu_choice = int(input("Välj ett menyalternativ (1-6): "))
    if menu_choice == 1:
        print_lista(kpi_10)
    elif menu_choice == 2:
        sum_value(kpi_10)
    elif menu_choice == 3:
        mean_value(kpi_10)
    elif menu_choice == 4:
        find_max(kpi_10)
    elif menu_choice == 5:
        find_min(kpi_10)
    elif menu_choice == 6:
        print("Avslutar programmet!")
    else:
        print("Ange en annan siffra")


# Tentamen 2024-08-19 - 2024-08-20 Uppgift 4 (4p)
print('Uppgift 4_NY\n')

# Nedanstående funktion tar en lista som argument och returnerar listan sorterad. 
# Tyvärr finns det några fel i funktionen som gör att den inte fungerar korrekt. 
# Din uppgift blir att rätta felen. Skriv en kommentar till varje ändring du gör, 
# okommenterade ändringar ger inga poäng.

# OBS Du får inte lägga till eller ta bort rader i koden för att få funktionen att 
# fungera utan enbart hitta felen och korrigera dessa. 

def sort_funk(lista):
    i=0
    while i < len(lista)-1: #Changed so the while loop works within the max index of the list, so while it is smaller than the length of list (changed > to <)
        if lista[i] > lista[i+1]: #Should compare with the next element, not the previous one (changed i-1 to i+1)
            x=lista[i]
            lista[i] = lista[i+1]
            lista[i+1] = x #Changed so the next step (i+1) becomes the temporary variable saved on line 17 instead it would just make it the same as it was before (changed lista[i] to x)
            i=0
            continue
        else:
            i+=1
    return lista
test_lista = [27, 13, 5, 8, 75, 103]
print(f"ursprunglig lista {test_lista}")
sort_funk(test_lista)
print(f"sorterad lista {test_lista}")


# Zapisywanie do pliku wygnerowane liczby podzielne przez 4

fileSave = open("plik.txt", "w")
for i in range(1,20+1):
    if i%4== 0:
        fileSave.write(str(i)+" ")
fileSave.close()

# Odczytywanie z pliku

fileRead = open("plik.txt", "r")
print(fileRead.read())
fileRead.close()

# Uzycie with i wyswietlenie na ekranie
with open("zdanie.txt", "r") as plik:
    for linia in plik:
        print(linia, end="")

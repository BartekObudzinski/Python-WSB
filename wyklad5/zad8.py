liczba = int(input("Podaj liczbe "))

suma = 0

while liczba > 0:
 suma+=liczba%10 #dodaj do wyniku wartość ostatniej cyfry
 liczba//=10 #usuń z przetwarzanej liczby ostatnią cyfrę 

print(suma)

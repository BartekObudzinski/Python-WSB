import math

a = int(input("Podaj liczbe "))
try:
    pierwiastek = math.sqrt(a)
    print(pierwiastek)
except:
    print("Liczba pod pierwiastkiem nie mzoe byc ujemna")

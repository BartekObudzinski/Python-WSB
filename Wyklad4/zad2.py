import os
a = int(input("Podaj pierwsza liczbe "))

b = int(input("Podaj druga liczbe: "))
print ("Podane liczby to ", a," i ", b)

dodawanie = a+b
odejmowanie = a-b
mnozenie = a*b

if b==0:
    print("Nie dzielimy przez 0")
    print("Dodawanie ", dodawanie, " odejmowanie ",odejmowanie, " mnozenie ", mnozenie)
else:
    dzielenie=a/b
print("Dodawanie ", dodawanie, " odejmowanie ",odejmowanie, " mnozenie ", mnozenie, " dzielnie ", dzielenie )

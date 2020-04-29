liczba = int(input("Podaj liczbe "))

for a in range(1):
    for x in range(1,liczba+1):
        print(x*"A")
        if (x>=10):
            break

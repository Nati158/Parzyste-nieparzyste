import random

def sprawdz_parzystosc_liczby(liczba):
    if liczba % 2 == 0:
        return "parzysta"
    else:
        return "nieparzysta"

# Generowanie losowej liczby
losowa_liczba = random.randint(1, 100)

print(f'Wylosowana liczba: {losowa_liczba}')
print(f'Ta liczba jest {sprawdz_parzystosc_liczby(losowa_liczba)}')

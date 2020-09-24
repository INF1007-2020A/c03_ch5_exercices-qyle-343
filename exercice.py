#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute() -> float:
    nombre = float(input("Veuillez entrer un nombre: "))
    if nombre < 0:
        nombre = nombre * -1
    return nombre


def use_prefixes() -> List[str]:
    prefixes, suffixes = 'JKLMNOP', 'ack'
    result = []
    for letter in prefixes:
        name = letter + suffixes
        result.append(name)
    return result


def prime_integer_summation() -> int:
    counter = 0
    prime_number = 3
    add = 2
    check_number = 2
    while counter < 100:
        if check_number == prime_number:
            check_number = 2
            add += prime_number
            counter += 1
            prime_number += 1
        else:
            if prime_number % check_number == 0:
                prime_number += 1
                check_number = 2
            else:
                check_number += 1
    return add


def factorial(number: int) -> int:
    return 0


def use_continue() -> None:
    pass


def main() -> None:
    print(f"La valeur absolue du nombre est {convert_to_absolute()}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des nombres de 0 à 100 est: {prime_integer_summation()}")

    number = 10
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()


if __name__ == '__main__':
    main()

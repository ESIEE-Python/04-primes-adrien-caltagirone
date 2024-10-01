""" Prime number module """
from math import sqrt

#### Fonction secondaire


def isprime(number):
    """ Is prime function """    
    if number == 1:
        return False

    prime = True

    for i in range(2, int(sqrt(number))+1):
        if number % i == 0:
            prime = False
            break

    return prime

#### Fonction principale


def main():
    """ Main prime function """

    # vos appels à la fonction secondaire ici

    for number in range(100):
        if isprime(number):
            print(number, end=", ")

    print()


if __name__ == "__main__":
    main()

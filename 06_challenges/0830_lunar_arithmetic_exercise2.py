"""Opgave "Lunar arithmetic"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

--------

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Se denne video fra 0:00 til 2:41:
    https://www.youtube.com/watch?v=cZkGeR9CWbk

Del 2:
    Skriv en klasse Lunar_int(), med metoder, der gør, at du kan anvende operatorerne + og * på
    objekter af denne klasse, og at resultaterne svarer til de regler, der forklares i videoen.

Del 3:
    Se resten af videoen.

Del 4:
    Skriv en funktion calc_lunar_primes(n), som retunerer en liste med de første n lunar primes.

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""
from code import interact
from hmac import digest
from itertools import count
from site import addsitedir
from statistics import linear_regression


#class Lunar_int:
#    def __init__(self, number1):
#        self.number1 = number1
#        pass
#    def _add_(self, number1, other):
#        digit=[int(d) for d in str(number1)]
#
#
#        return number1

# def split(num):
#     digits =[int(d) for d in str(num)]
#     print(digits)
#     if isinstance(digits, list):
#         print("actual list")
#     if isinstance(digits[0], int):
#         print(digits[0], "is a integer")
# 
# split(678)


class LunarInt:
    def __init__(self, number1):
        digit1 = [int(d) for d in str(number1)]
        self.digit = digit1
    def __add__(self, other):
        count(0)
        if digit1(0+count) == digit2(0+count):
            return (digit1(0+count))

lunar1 = LunarInt(25)

print(lunar1.digit)
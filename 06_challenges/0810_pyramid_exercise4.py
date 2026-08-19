"""Opgave "Number pyramid"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

--------

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Se de første 93 sekunder af denne video: https://www.youtube.com/watch?v=NsjsLwYRW8o

Del 2:
    Skriv en funktion "pyramid", der producerer de tal, der er vist i videoen.
    Funktionen har en parameter "lines", der definerer, hvor mange talrækker der skal produceres.
    Funktionen udskriver tallene i hver række og også deres sum.

Del 3:
    I hovedprogrammet kalder du funktionen med fx 7 som argument.

Del 4:
    Tilføj en mere generel funktion pyramid2.
    Denne funktion har som andet parameter "firstline" en liste med pyramidens øverste rækkens tallene.

Del 5:
    I hovedprogrammet kalder du pyramid2 med fx 10 som det første argument
    og en liste med tal efter eget valg som andet argument.
    Afprøv forskellige lister som andet argument.

Hvis du ikke aner, hvordan du skal begynde, kan du åbne 0812_pyramid_help.py og starte derfra

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""
import numbers
from encodings.punycode import insertion_sort


def pyramid(lines):
    numbers=[1,1]
    count=0
    startnumber = 2
    globalcount= 0
    print(len(numbers))
    print(numbers, sum(numbers), startnumber)
    newnumbers=numbers.copy()
    print(numbers[len(numbers)-1])

    for numbers in range(len(numbers)):
        print(numbers, "here")
        if  numbers+(numbers) == startnumber:
            newnumbers.insert(1, startnumber)
            count+=1
            print("number inserted")
            print(newnumbers)
        else:
            print(newnumbers)
            print("newline")
            count=0

pyramid(1)

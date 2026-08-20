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
from operator import length_hint


# def pyramid(lines):
#    numbers=[1,1]
#    count=1
#    startnumber = 1
#    globalcount= 0
#    print(len(numbers))
#    print(numbers, sum(numbers), startnumber)
#    newnumbers=numbers.copy()

#    for number in numbers:
#        if number + numbers == startnumber:
#            newnumbers.insert(1, startnumber)
#            count+=1
#            print(newnumbers)
#        else:
#            print(newnumbers)
#            print("newline")
#            count=0

# pyramid(1)


#numbers = [1,1, 8, 7, 0]

#for i, j in zip(numbers[:-1], numbers[1:]):
#    print(i, j)

def pyramid(lines):
    print(lines)
    numbers=[1,1]
    startnumber = 2
    globalcount=0
    count= 0
    newnumbers=numbers.copy()
    print(numbers, startnumber)
    while lines > globalcount:
     for f,s in zip(numbers[:-1+count], numbers[1+count:]):

         if f + s == startnumber:
             newnumbers.insert(1+count, startnumber)
             print("added")
             print(newnumbers, count)
             count += 1
             print(newnumbers, count)

         if count == len(numbers)-1:
             print("done ")
             count=0
             numbers=newnumbers.copy()
             globalcount += 1
             print(numbers, count, globalcount)

         #else:
             #print("here")
    print("end")



pyramid(2)
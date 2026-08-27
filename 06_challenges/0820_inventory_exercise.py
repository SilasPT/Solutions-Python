"""Opgave "The inventory sequence"

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

--------

Denne øvelse er en valgfri udfordring for de fremragende programmører blandt jer.
Du behøver absolut ikke at løse denne øvelse for at fortsætte med succes.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Del 1:
    Se de første 3 minutter af denne video:
    https://www.youtube.com/watch?v=rBU9E-ZOZAI

Del 2:
    Skriv en funktion inventory(), som producerer de tal, der er vist i videoen.
    Funktionen accepterer en parameter, der definerer, hvor mange talrækker der skal produceres.
    Funktionen udskriver tallene i hver række.

    Du vil sandsynligvis ønske at definere en funktion count_number(), som tæller, hvor ofte
    et bestemt antal optræder i den aktuelle talrække.

Del 3:
    I hovedprogrammet kalder du inventory() med fx 6 som argument.

--------

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
"""

def inventorytest(lines):
    inventory = []
    if inventory == []:
        inventory.insert(0, 0)
        inventory.insert(0, 0)
        print(inventory)
        print(lines)
    for int in inventory:
        inventory.count(0)
        print(inventory.count(0), "here")




def inventory(lines):
    inventory = []
    inventorypost = []
    globalcount = 0
    number = 0
    while lines > globalcount:
        if not inventory.count(number) == 0:
            inventorypost.append((inventory.count(number)))
            inventory.append((inventory.count(number)))
            #print("insert 1 ", inventory.count(number))
            #print(inventory)
            number+=1

        elif inventory.count(number) == 0:
            inventorypost.append((inventory.count(number)))
            inventory.append((inventory.count(number)))
            print(inventorypost)
            inventorypost.clear()
            #inventory.append("new line here)")
            number = 0
            #print(number, "number reset")
            globalcount += 1
            #print(inventory, "insert 2")
            #print("here")



inventory(6)

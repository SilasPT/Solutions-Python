"""
Opgave "Morris The Miner" (denne gang objekt orienteret)

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Genbrug din oprindelige Morris-kode og omskriv den til en objektorienteret version.

Definer en klasse Miner med attributter som sleepiness, thirst osv.
og metoder som sleep, drink osv.
Opret Morris og initialiser hans attributter ved at kalde konstruktoren for Miner:
morris = Miner()

Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil."""

class Miner:
    def __init__(self, ):


def dead_check():
    print(morris)
    if morris["sleepiness"] >= 100:
        print("morris died of sleepiness")
        quit()
    elif morris["thirst"] >= 100:
        print("morris died of thirst")
        quit()
    elif morris["hunger"] >= 100:
        print("morris died of thirst")
        quit()

def sleep():
    morris["turn"] += 1
    morris["sleepiness"] -= 10
    morris["thirst"] += 1
    morris["hunger"] += 1

def mine():
    morris["turn"] += 1
    morris["sleepiness"] += 5
    morris["thirst"] += 5
    morris["hunger"] += 5
    morris["gold"] += 5

def eat():
    morris["turn"] += 1
    morris["sleepiness"] += 5
    morris["thirst"] -= 5
    morris["hunger"] -= 20
    morris["gold"] -= 2

def buy_whisky():
    morris["turn"] += 1
    morris["sleepiness"] += 5
    morris["thirst"] += 1
    morris["hunger"] += 1
    morris["whisky"] += 1
    morris["gold"] -= 1

def drink():
    morris["turn"] += 1
    morris["sleepiness"] += 5
    morris["thirst"] -= 15
    morris["hunger"] -= 1
    morris["whisky"] -= 1

morris = Miner()

while morris["turn"] < 1000:
    dead_check()
    if morris["sleepiness"] >= 95:
        sleep()
    elif morris["hunger"] >= 94:
        eat()
    elif morris["thirst"] >= 94 and morris["whisky"] >=1:
        drink()
    elif morris["whisky"] <=1:
        buy_whisky()
    else:
        mine()

print(morris)
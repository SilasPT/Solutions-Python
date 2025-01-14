"""
Opgave "Morris the Miner":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Udgangssituation:
Morris har egenskaberne sleepiness, thirst, hunger, whisky, gold.
Alle attributter har startværdien 0.

Regler:
Hvis sleepiness, thirst eller hunger kommer over 100, dør Morris.
Morris kan ikke opbevare mere end 10 flasker whisky.
Ingen attribut kan gå under 0.

Ved hver omgang kan Morris udføre præcis én af disse aktiviteter:
sleep:      sleepiness-=10, thirst+=1,  hunger+=1,  whisky+=0, gold+=0
mine:       sleepiness+=5,  thirst+=5,  hunger+=5,  whisky+=0, gold+=5
eat:        sleepiness+=5,  thirst-=5,  hunger-=20, whisky+=0, gold-=2
buy_whisky: sleepiness+=5,  thirst+=1,  hunger+=1,  whisky+=1, gold-=1
drink:      sleepiness+=5,  thirst-=15, hunger-=1,  whisky-=1, gold+=0

Din opgave:
Skriv et program, der giver Morris så meget guld som muligt på 1000 omgange.

Hvis du ikke har nogen idé om hvordan du skal begynde, så åbn S0185_morris_help.py og start derfra.
Hvis du går i stå, så spørg google, de andre elever, en AI eller læreren.

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""

morris = {"turn": 0, "sleepiness": 0, "thirst": 0, "hunger": 0, "whisky": 0, "gold": 0}

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

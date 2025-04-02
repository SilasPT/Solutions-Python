"""opgave: Objektorienteret rollespil, afsnit 2 :

Som altid skal du læse hele øvelsesbeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Byg videre på din løsning af afsnit 1.

Del 1:
    Opfind to nye klasser, som arver fra klassen Character. For eksempel Hunter og Magician.
    Dine nye klasser skal have deres egne ekstra metoder og/eller attributter.
    Måske overskriver de også metoder eller attributter fra klassen Character.

Del 2:
    Lad i hovedprogrammet objekter af dine nye klasser (dvs. rollespilfigurer) kæmpe mod hinanden,
    indtil den ene figur er død. Udskriv, hvad der sker under kampen.

I hver omgang bruger en figur en af sine evner (metoder). Derefter er det den anden figurs tur.
Det er op til dig, hvordan dit program i hver tur beslutter, hvilken evne der skal bruges.
Beslutningen kan f.eks. være baseret på tilfældighed eller på en smart strategi

Del 3:
    Hver gang en figur bruger en af sine evner, skal du tilføje noget tilfældighed til den anvendte evne.

Del 4:
    Lad dine figurer kæmpe mod hinanden 100 gange.
    Hold styr på resultaterne.
    Prøv at afbalancere dine figurers evner på en sådan måde, at hver figur vinder ca. halvdelen af kampene.

Hvis du går i stå, kan du spørge google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-besked til din lærer: <filename> done
Fortsæt derefter med den næste fil."""

class Character:
    def __init__(self, name, max_health, _current_health, attackpower):
        self.name = name
        self.max_health = max_health
        self._current_health = _current_health
        self.attackpower = attackpower

    def gethit(self, attacker):
        self._current_health -= attacker.attackpower
        print(self.name + " gets hit by the attack of " + attacker.name)

    def hit(self, target):
        target.gethit(self)

    def getheal(self, attacker):
        self._current_health += attacker.healpower

    def __repr__(self):
        return f"Character: {self.name=} {self.max_health=} {self._current_health=} {self.attackpower=}"

    def showstats(self):
        print(self)

class Healer(Character):
     def __init__(self, name, max_health, _current_health, attackpower, special_power):
         self.healpower = special_power
         self.name = name
         self.max_health = max_health
         self._current_health = _current_health
         self.attackpower = attackpower

     def heal(self, target):
         target.getheal(self)

     def __repr__(self):
        return f"Character: {self.name=} {self.max_health=} {self._current_health=} {self.attackpower=} {self.healpower=}"


class Magican(Character):
    def __init__(self, name, max_health, _current_health, attackpower, special_power):
        self.manapower = special_power
        self.name = name
        self.max_health = max_health
        self._current_health = _current_health
        self.attackpower = attackpower

    def spellattack(self, target):
        if target.manapower > 0:
            target.gethit * self.manapower
            print(self.name + " hit " + target.name + " with a spell for " + self.attackpower * self.manapower + " damage")
            self.manapower -= 1
        else:
            print(self.name + " dont have any mana left to cast")

    def __repr__(self):
        return f"Character: {self.name=} {self.max_health=} {self._current_health=} {self.attackpower=} {self.manapower=}"

class Hunter(Character):
    def __init__(self, name, max_health, _current_health, attackpower, special_power):
        self.dodges = special_power
        self.name = name
        self.max_health = max_health
        self._current_health = _current_health
        self.attackpower = attackpower

    def gethit(self, attacker):
        if self.dodges > 0:
            print( self.name + " dodges the attack of " + attacker.name)
            self.dodges -= 1
        else:
            self._current_health -= attacker.attackpower
            print( self.name + " gets hit by the attack of " + attacker.name)

Joe_H = Hunter(Joe, 40, 40, 15, 5)
Jim_M = Magican(Jim, 30, 30, 10, 5)
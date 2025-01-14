"""
Opgave "Reading from a file":

Som altid skal du læse hele opgavebeskrivelsen omhyggeligt, før du begynder at løse opgaven.

Kopier denne fil til din egen løsningsmappe. Skriv din løsning ind i kopien.

Opret en tekstfil med en editor efter eget valg (pycharm, notepad, notepad++ osv.)
Hver række skal bestå af en persons navn efterfulgt af et mellemrum og et tal, der repræsenterer personens alder.
gem filen i din løsningsmappe

Skriv et program, der læser filen til en liste af strings.
Derefter brug indholdet af hver string til at udskrive en række som f.eks:
    <navn> er <alder> år gammel.

Hvis du går i stå, så spørg google, de andre elever eller læreren (i denne rækkefølge).

Når dit program er færdigt, skal du skubbe det til dit github-repository.
Send derefter denne Teams-meddelelse til din lærer: <filename> færdig
Fortsæt derefter med den næste fil.
"""
textfile = "S0165_file_test.txt" #Name of the file
Navn = ["Lars", "Ole", "Kristen", "Jakob", "Henrik"]
Alder = ["1", "2", "4", "16" , "18"]

def testinput(data1, data2):
    count = 0
    inputdata = "Navn og Alder liste\n"
    while count < len(data1) and len(data2):
        inputdata += "navn: " + data1[count] + "  alder: " + data2[count] + "\n"
        count+= 1
    return inputdata

with open(textfile,"w") as file:
    file.writelines(testinput(Navn, Alder))

with open(textfile) as file:
    for line in file:
        print (line.strip())
print()
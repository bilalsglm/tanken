# 1
# eingabe liter tank eures autos maximal fasst
#  eingabe/festlegen kosten euro/liter
# eingabe wieviel ihr tank in liter
# ausgabe der summe der getanken liter

maximalLiter = int(input('Bitte die maximalen Liter des Tanks angeben: '))
euroProlitre = 1.5
tanken = int (input("ich tanke so viele Liter:"))

summe = euroProlitre * tanken

print("Der Betrag, den ich bezahlen muss:" + str(summe))
print("Der Betrag, den ich bezahlen muss:" , summe)
print(f"Der Betrag, den ich bezahlen muss: {summe} " )

# 2
# ausgabe zu wie viel % der tank gefüllt ist
# wenn der tank unter 10% gefüllt ist : ausgabe "Reserve, bitte tanken"
# wenn der tank zwischen 11% und 100% gefüllt ist:ausgabe "Alles OK"
# wenn der tank zu mehr als 100% gefüllt ist : ausgabe "Ab in die Werkstatt"

gefuellt = maximalLiter/ 100 * tanken

if gefuellt<= 10:
    print('Reserve, bitte tanken')
elif 10 < gefuellt <= 100:
    print('Alles okay')
elif gefuellt > 100:
    print ('Ab in die Werkstatt')
else:
    print ('Irgendwas ist schief glaufen')

    
# Schreibe ein Program mit einer Funktion, die zwei übergabeparameter akzeptirt.
# 1. Euro pro Litre als float Bsp: 2.10 Euro
# 2. Anzahl der Liter, die Ihr tank Bsp: 50 Litre

# Die Funktion soll zurückgeben, wie voll der tank ist Bps. "Reserve" und zu wie viel Prozent der Tank gefüllt ist
# bps. 20%
# Beide Ausgaben dürfen in einem String stehen.

"""
def tanken(euroProliter, liter):

    maximalLiter = 80
    gefuelltinProzent = maximalLiter / 100 * liter
    summe = euroProliter * liter

    result = " "
    
    if gefuelltinProzent<= 10:
        result = 'Reserve, bitte tanken'
    elif 10 < gefuelltinProzent <= 100:
        result = 'Alles okay'
    elif gefuelltinProzent > 100:
        result = 'Ab in die Werkstatt'
    else:
        result = 'Irgendwas ist schief glaufen'

    return result + str(gefuelltinProzent) + "% " + str(summe) + "€"

liter = int(input('Bitte die maximalen Liter des Tanks angeben: '))
euroProliter = float(input("ich tanke so viele Liter:"))

print(tanken(euroProliter, liter))
"""
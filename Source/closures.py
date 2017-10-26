# Hier beginnt die outer-function
def make_dice(x):

    # Hier beginnt die inner-function
    def compute_probability(y):
        # 1.0 damit die Rechnung als "Float" betrachtet wird
        # Return der inner function (Resultat der Wahrscheinlichkeit)
        return 1.0/x**y
    # Achtung hier kein () setzen da wir kein Resultat zurueckgeben wollen!
    # Wir wollen eine Funktionssignatur erhalten <function compute_probability at 0x1030815f0>
    return compute_probability

die_with_6_nums = make_dice(6) # Die 6 ist dabei x

# Auskommentieren um die Funktionssignatur zu sehen
#print(die_with_6_nums)

# Die 2 wird implizit zu y und daher ein "First Class Citizen"
print(die_with_6_nums(2))


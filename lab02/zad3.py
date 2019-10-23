# Zadanie 3
# Basic formatting
text1 = "Dominika"
text2 = "Moluszys"

print("{1} {0}" .format(text1, text2))


# Value conversion
class Data(object):
    def __str__(self):
        return "Dominika"
    def __repr__(self):
        return "Moluszys"

print("{0!s} {0!r}" .format(Data()))


# Padding and aligning strings
print("{:>12}" .format("Dominika"))
print("{:12}" .format("Moluszys"))
print("{:_<10}" .format("Domix"))
print("{:^11}" .format("Domix"))


# Truncating long strings
print("{:.15}" .format("konstantynopolitanczykowianeczka"))


# Combining truncating and padding
print("{:15.20}" .format("konstantynopolitanczykiewiczowna"))
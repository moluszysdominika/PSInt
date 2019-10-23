# Zadanie 1
lorem = "Lorem Ipsum jest tekstem stosowanym jako przykładowy wypełniacz w przemyśle poligraficznym. Został po raz pierwszy użyty w XV w. przez nieznanego drukarza do wypełnienia tekstem próbnej książki. Pięć wieków później zaczął być używany przemyśle elektronicznym, pozostając praktycznie niezmienionym. Spopularyzował się w latach 60. XX w. wraz z publikacją arkuszy Letrasetu, zawierających fragmenty Lorem Ipsum, a ostatnio z zawierającym różne wersje Lorem Ipsum oprogramowaniem przeznaczonym do realizacji druków na komputerach osobistych, jak Aldus PageMaker."

# Zadanie 2
print('####################')
imie = 'Dominika'
nazwisko = 'Moluszys'

litera_1 = imie[2]
litera_2 = nazwisko[3]

liczba_liter1 = 0
liczba_liter2 = 0

for i in range(len(lorem)):
    if lorem[i] == litera_1:
        liczba_liter1 += 1
    elif lorem[i] == litera_2:
        liczba_liter2 += 1

print('W tekście jest {} liter {} oraz {} liter {}' .format(liczba_liter1, litera_1, liczba_liter2, litera_2))

# Zadanie 4
print('####################')
text = "Ala ma kota"

print(dir(tmp))
help(tmp.capitalize())

# Zadanie 5
print('####################')
#print([::-1] .format(imie))
print(imie[::-1].capitalize())

#Zadanie 6
print('####################')
list = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
list1 = list[5:10]
list2 = list[0:5]

print(list2)
print('*************')
print(list1)

#Zadanie 7
print('####################')
list.append(0)
list = list1 + list
listcopy = list
print(list)
print('*************')
listcopy.sort()
print(list1)

#Zadanie 8
print('####################')
studenci =[]
student1 = (111111, "Jan", "Kowalski")
student2 = (222222, "Aneta", "Walecka")
student3 = (333333, "Zuzanna", "Małecka")
studenci.append(student1)
studenci.append(student2)
studenci.append(student3)
print(studenci)

#Zadanie 9
print('####################')
slownik = {}
for val in studenci:
    slownik[val[0]] = val[1],val[2]
slownik[111111] += '22','jan.kowalski@gmail.com','1997','ul. Lubelska 3, 21-345 Darnewo'
slownik[222222] += '25','walecka@aneta.pl','1994','ul. Orzyska 45, 54-213 Orzysz'
slownik[333333] += '20','zuza@buziaczek.pl','1999','ul. Wadowicka 2137, 21-37 Wadowice'
print(slownik)

#Zadanie 10
print('####################')
phonelist =[]
phonelist.append('997')
phonelist.append('112')
phonelist.append('998')
phonelist.append('999')
phonelist.append('112')
print(phonelist)
phoneset = set(phonelist)
print(phoneset)

#Zadanie 11
print('####################')
for number in range(10):
    print(number)

#Zadanie 12
print('####################')
for number in range(100,20,-5):
    print(number)
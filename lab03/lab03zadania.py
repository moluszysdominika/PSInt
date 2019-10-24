# Zadanie 1

def index(a_list, b_list):
    output = []
    for i in range(len(a_list)):
        if i % 2 == 0:
            output.append(i)
    for i in range(len(b_list)):
        if i % 2 != 0:
            output.append(i)
    return output


list1 = [54, 65, 78, 95, 52, 65]
list2 = [16, 58, 23, 34, 35, 26, 59, 15, 45]
list3 = index(list1, list2)
print("Output:", list3)


# Zadanie 2

print('####################')

def fun(data_text):
    data_text = str(data_text)
    length = len(data_text)
    letters = list(data_text)
    big_letters = data_text.upper()
    small_letters = data_text.lower()
    dict = {'dlugosc tekstu:': length, 'lista znakow:': letters, 'kapitaliki:': big_letters,
            'male litery:': small_letters}
    return dict

lorem = "Lorem ipsum dolor sit amet"
print(fun(lorem))


# Zadanie 3

print('####################')

def fun(text, letter):
    text = str(text)
    for n in text:
        if n == letter:
            text = text.replace(n, '')
    return text

print(fun("Lorem ipsum dolor sit amet", 'm'))

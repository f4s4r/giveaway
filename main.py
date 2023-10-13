import random
data = {}

f = open('data.txt', encoding='utf-8')

n = int(f.readline())

for i in f:
    name1, name2, score = i.split()
    name = name1 + " " + name2
    data[name] = int(score)

names = [x for x in data]
qual = [data[x] for x in names]

itog = [int(x**1.5) for x in qual]#увеличивает разницу между занениями

abc = []
for i in range(n):
    letter = chr(i + 65)
    abc += [letter * itog[i]]
string = ''
for i in range(n):
    string += abc[i][0] * len(abc[i])
winner1 = string[random.randint(0, len(string))]
string1 = ''
for i in range(len(string)):
    if string[i] != winner1:
        string1 += string[i]


winner2 = string1[random.randint(0, len(string1))]
string2 = ''
for i in range(len(string1)):
    if string1[i] != winner2:
        string2 += string1[i]


winner3 = string2[random.randint(0, len(string2))]
string3 = ''
for i in range(len(string2)):
    if string2[i] != winner3:
        string3 += string2[i]

winner4 = string3[random.randint(0, len(string3))]
string4 = ''
for i in range(len(string3)):
    if string3[i] != winner4:
        string4 += string3[i]

winner5 = string4[random.randint(0, len(string4))]

win1 = names[ord(winner1)-65]
win2 = names[ord(winner2)-65]
win3 = names[ord(winner3)-65]
win4 = names[ord(winner4)-65]
win5 = names[ord(winner5)-65]
print(' ' + '1 место -', win1, '\n', '2 место -', win2, '\n', '3 место -', win3, '\n', '4 место -', win4, '\n', '5 место -', win5)
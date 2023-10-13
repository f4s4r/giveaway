import random #ипорт рандома
data = {}

f = open('data.txt', encoding='utf-8') #открытие файла .txt с именами и баллами

n = int(f.readline()) # считываение кол-ва участников, в данном случае 14

for i in f: #заполнение словаря data именами с баллами
    name1, name2, score = i.split()
    name = name1 + " " + name2
    data[name] = int(score)

names = [x for x in data] #создание списка только с именами
qual = [data[x] for x in names] # создание списка только с баллами

itog = [int(x**1.5) for x in qual]#дифферинцирует баллы в n раз(1.5 в данном случае)

abc = []
for i in range(n):
    letter = chr(i + 65) #возврат буквы в зависимости от положения человека в списке
    abc += [letter * itog[i]] #заполнение abc буквами, чтобы далее можно люди с большими баллами имели больше шансов выиграть
string = ''
for i in range(n):#создание единой строки со всеми буквами
    string += abc[i][0] * len(abc[i])
winner1 = string[random.randint(0, len(string))]
string1 = ''
for i in range(len(string)):
    if string[i] != winner1:
        string1 += string[i]


winner2 = string1[random.randint(0, len(string1))] #дальнейшие однообразные строчки кода просто выбирают победителей
string2 = '' #создание будущей строки, в которой не будет предыдущего символа, который уже победил
for i in range(len(string1)):
    if string1[i] != winner2: #проверка на то, есть ли уже победивший символ в строке
        string2 += string1[i] #если его нет, то он заносится в новую строку


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

win1 = names[ord(winner1)-65] # обратное нахождение имен с помощью выведенных букв
win2 = names[ord(winner2)-65]
win3 = names[ord(winner3)-65]
win4 = names[ord(winner4)-65]
win5 = names[ord(winner5)-65]
print(' ' + '1 место -', win1, '---',  data[win1], 'балла/ов')
print(' ' + '2 место -', win2, '---',  data[win2], 'балла/ов')
print(' ' + '3 место -', win3, '---',  data[win3], 'балла/ов')
print(' ' + '4 место -', win4, '---',  data[win4], 'балла/ов')
print(' ' + '5 место -', win5, '---',  data[win5], 'балла/ов')
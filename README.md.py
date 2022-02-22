# hw.hse
#Ex 1 - Средний балл (списки)
student = ('Иван Питонов', 2001, [8, 7, 7, 9, 6], True)

f_l_name = ''.join(student[0])
print(f_l_name.split())
print(f"Студент: {f_l_name[5:12]}, {f_l_name[0:4]}")

age = student[1]
year = 2020
birthyear = (year-age)
print(f"Возраст студента: {birthyear}")

assessment = [8, 7, 7, 9, 6] 
print(f"Оценки студента: {assessment}")

gpa = (sum(assessment) / len(assessment))
print(f"Средний балл студента: {gpa}")

if gpa >= 8:
    print(True)
else:
    print(False)

#Ex 2 - Сортируем числа и строки (списки, сортировки, map())
numbers = [1, 1000, 1002124, 25, 10, 20, 351]

numbers_int_sorted = sorted(numbers)
print(numbers_int_sorted)

numbers_str = list(map(str, numbers))
print(numbers_str)

numbers_str_sorted = sorted(numbers_str, key=int)
print(numbers_str_sorted)

numbers_str_key_sorted = sorted(numbers_str, key=int)
print(numbers_str_key_sorted)

print(numbers_int_sorted, numbers_str_sorted, numbers_str_key_sorted)

#Ex 3 - Количество различных чисел (списки и множества)
lst = [1, 2, 3, 7, 1, 2, 10, 9]
print(lst)
lst1 = set(lst)
print(len(lst1))

#Ex 4 - Факультативы (множества) - предметы: английский, немецкий, право, математика, сольфеджио
a = set(input().split())
b = set(input().split())
c = set(input().split())
print(len(list(a.intersection(b).intersection(c)))) 
print(', '.join((a.union(b)).difference(c)))


#Ex 5 - Вложенные словари
dict_of_lists = {
    'Список1': [{'Python': 'язык программирования'}, {'R':'язык программирования', 'LaTEX' : 'язык верстки' }],
    'Список2' : [{'Windows' :  ['операционная система', 'разработчик'], 'UNIX' : 'операционная система'}, {'IBM': ['компания-производитель', 'разработчик'], 'IPv6' : 'интернет-протокол' }]}
el = dict_of_lists.pop('Список2')
new_key = {'Список2' : [{'Windows' : 'разработчик', 'UNIX' : 'операционная система'}, {'IBM': ['компания-производитель', 'разработчик'], 'IPv6' : 'интернет-протокол' }]}
dict_of_lists.update(new_key)
print(dict_of_lists['Список2'][0]['Windows'])

#Ex 6 - Срезы строк
word = 'Abrakadabra'
print(word[2])
print(word[-2])
print(word[:5])
print(word[:9])
print(word[::2])
print(word[1::2])
print(word[::-1])
print(word[::-2])
print(len(word))

#Ex 7 - Срезы списков
dwarves = ["Балин", "Двалин", "Бифур", "Бофур", 
         "Бомбур", "Оин", "Глоин", "Дори", "Нори",
         "Ори", "Фили", "Кили", "Торин"]
print(dwarves[1:4])
print(dwarves[0::2])
print(dwarves[5::2])
print(dwarves[::-2][-7:-3]) 

#Ex 8 - Сколько чисел совпадает? (условия)
n_1 = int(input())
n_2 = int(input())
n_3 = int(input())
if n_1 == n_2 == n_3:
    print(3)
elif n_1 == n_2 or n_2 == n_3 or n_1 == n_3:
    print(2)
else:
    print(0)

#Ex 9 - Переклеить строку
print("-".join(input()))

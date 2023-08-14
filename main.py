# статический метод посмотреть теорию
# raise для описания своих ошибок
# while True:
#     try:
#         login = input('Введите логин: ')
#         if len(login) <= 3:
#             raise Exception('Введен короткий логин повторите ввод')
#         if len(login) >= 30:
#             raise Exception('Введен длинный логин повторите ввод')
#
#         break
#     except Exception as error:
#         print(f'Ошибка {error}')
# try:
#     password = input('Введите пароль: ')
#     if len(password) >= 8:
#         raise Exception('Введен не верный пароль повторите ввод')
# except Exception as error:
#     print(error)
# print(f'Вы ввели логин такой: {login} и пароль: {password}')
#
# import os
#
# programers = []
# with open('text.txt', 'r', encoding="utf-8") as textFile:
#     someProgramers = textFile.readlines()
#     programers = [programer.rstrip('\n') for programer in someProgramers]
#
# while True:
#     try:
#         print('0 - Выход')
#         print('1 - Количество программистов на проекте')
#         print('2 - Добавить программиста на проект')
#         print('3 - Убрать программиста с проекта')
#         programers.sort()
#         option = input('Выберите действие из списка: ')
#
#         if option == '0':
#             with open('text.txt', 'w', encoding="utf-8") as textFile:
#                 textFile.writelines([car + '\n' for car in programers])
#
#             break
#
#         elif option == '1':
#             print('Количество программистов на проекте')
#             for programer in programers:
#                 print(' - ' + programer)
#
#         elif option == '2':
#             programer = input('Введите ФИО программиста для добавления на проект: ')
#             # raise Exception('Введены символы необходим цифровой выбор действия')
#             if not programer.isalpha():
#                 raise Exception('Введена не корректная фамилия')
#                 programers.append(programer)
#                 print(f'Программист {programer} добавлен на проект ')
#
#             # else:
#             #     print('Ошибка введена не корректная фамилия повторите ввод')
#
#         elif option == '3':
#             print(programers)
#             programer = int(input('Выберите программиста для перевода на др. проект по индексу: '))
#             programers.pop(programer)
#             print(f'Программисты {programers} остались на проекте, а программист {programer} переведен на другой проект')
#
#     except Exception as error:
#         print(f'Ошибка {error}')
#     #
#     os.system('Ожидание')
#     os.system('cls')
#
# print('Пока')

# PostgreSQL
#
# def summa(*args):
#     return len(args)
# result = summa(1,2,3,4)
# print(result)

# text = 'gfdhghdg gfhgfdfdhj jhfgdhhgfdjfg dfdhfgdjhg'
# textList = text.split(' ')
# textList1 = len(textList)
# print(textList1)
# print(len(textList[-1]))

text = '2 + 5'

# while True:
#     print('+ - сложение')
#     print('- - вычитание')
#     print('* - умножение')
#     print('/ - деление')
#     print('Q - выход')
#
#     option = input('Выберите действие из списка: ')
#
#     if option == '+':
#         print (f'{text[0]} + {text[4]} = {int(text[0]) + int(text[4])}')
#
#     elif option == '-':
#         print(f'{text[0]} - {text[4]} = {int(text[0]) - int(text[4])}')
#
#     elif option == '*':
#         print(f'{text[0]} * {text[4]} = {int(text[0]) * int(text[4])}')
#
#     elif option == '/':
#         print(f'{text[0]} / {text[4]} = {int(text[0]) / int(text[4])}')
#
#     elif option == 'Q':
#         break
# print('Пока')

# цифра 5
# someList = [1,1,2,2,3,3,4,4,5]
# for index in someList:
#     if someList.count(index) == 1:
#         print(index)
#         print(someList[index])
#         break

# someList = [1,3,5,9,6]
# someList1 = [4,5,7,8,1,3,4]
# someList3 = []
#
# for index in someList:
#     if someList.count(index) == 1:
#         someList3.append(index)
# for index in someList1:
#     if someList1.count(index) == 1:
#         someList3.append(index)
# print(someList3)
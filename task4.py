##Преобразовать слова «разработка», «администрирование», «protocol»,
##«standard» из строкового представления в байтовое и выполнить
##обратное преобразование (используя методы encode и decode).
##Подсказки:
##--- используйте списки и циклы, не дублируйте функции


list_text = ['разработка', 'администрирование', 'protocol', 'standard']

for i in list_text:
    print(f'{i}')
    print(f'В байтовом формате: {i.encode("utf8")}')
    print(f'Обратное преобразование: {i.encode("utf8").decode()}\n')
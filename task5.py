##Выполнить пинг веб-ресурсов yandex.ru, youtube.com и
##преобразовать результаты из байтовового в строковый тип на кириллице.
##Подсказки:
##--- используйте модуль chardet, иначе задание не засчитается!!!

import subprocess

ping = [['ping', 'yandex.ru'],['ping', 'youtube.com']]
 
for i in ping:
    ping_process = subprocess.Popen(i, stdout=subprocess.PIPE)
    count = 0
    for j in ping_process.stdout:
        if count < 5:
            j = j.decode('cp866').encode('utf-8')
            print(j.decode('utf-8'))
            count += 1
        else:
            break
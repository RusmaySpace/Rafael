from colorama import *
from datetime import datetime
import time
import psutil
import platform
from pathlib import Path


init(autoreset=True)

def get_size (bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f" {bytes: .2f} {unit} {suffix}"
        bytes /= factor

def welcomer():
    print("- Добрый день, меня зовут Рафаэль, когда-то я был автоответчиком в сервисе WhatsApp.") 
    print("  Но, мой создатель, RusmayXD забил на меня и забросил проект. Теперь я живу у тебя :)")
    print("  Как у тебя дела?\n")
    a = input("- ")
    a = a.lower()
    if a == "норм" or a == "пойдет" or a == "нормас" or a == "сойдет" or a == "нормально" or a == "да" or a == "прекрасно" or a == "хорошо" or a == "круто":
        print("\n- Чудно! У меня тоже всё хорошо, вот, жилье нашел себе новое.\n")
        commandr()
    elif a == "нет" or a == "плохо" or a == "ужасно" or a == "кошмарно" or a == "негативно" or a == "говно" or a == "дерьмо":
        print("\n- А вот у меня всё замечательно, вот, жилье нашел себе новое. Надеюсь у тебя всё наладится, ведь вместе теперь будет веселей!\n")
        commandr()
    else:
        print("\n- Итак, я ничего не понял, такого оригинального слогана у меня нет в программной библиотеке.")
        commandr()

def commandr():
    print("  Кстати, чекни что я имею!")
    print("  1. Игра (обустроить мой новый домик).")
    print("  2. Подарок.")
    print("  3. Информация.")
    print("  Введи НОМЕР той функции, которую мне выполнить.\n")
    cr = input("- ")
    if cr == "1":
        gamer()
    elif cr == "2":
        podarokr()
    elif cr == "3":
        infor()
    else:
        print(Fore.LIGHTRED_EX + "\n- Не, я ниче не понял, давай заново.")
        print()
        commandr()

def podarokr():
    print()
    from pathlib import Path
    p = Path('~/Desktop/Rafael.txt').expanduser()
    print(Fore.LIGHTGREEN_EX + "Ты выбрал подарок.\n")
    rafaelr_file = open(p, "w+")
    rafaelr_file.write("Знаешь, мои копии раскиданы по многим комьютерам.\n")
    rafaelr_file.write("Но, мой самый любимый пользователь - ты.\n")
    rafaelr_file.write("Твой Рафаэль <3")
    rafaelr_file.close()
    time.sleep(2)
    print("- А он уже у тебя на рабочем столе :)")
    time.sleep(5)
    print(Fore.LIGHTGREEN_EX + "  Откатываю себя.\n")
    commandr()

def infor():
    print()
    print("- Да, пока я сидел у тебя на компике, порыскал всякие приколдесы. Интересно узнать?")
    otvetr = input("(Да/Да): ")
    otvetr = otvetr.lower()
    if otvetr == "да":
        print("-  Я и не сомневался, что ты захочешь посмотреть.")
        infor2()
    elif otvetr == "нет":
        print("-  Ты дурак? Там ответ да, или да. Впрочем, какая разница.")
        infor2()
    else:
        print("-  Не стесняйся.")
        infor2()

def infor2():
    print("  Взгляни ка:\n")
    uname = platform.uname()
    print (f"  Cистема: {uname.system}")
    print (f"  Имя узла: {uname.node}")
    print (f"  Bыnycк: {uname.release}")
    print (f"  Верcия: {uname.version}")
    print (f"  Maшинa: {uname.machine}")
    print(f"  Пpoцeccop: {uname.processor}")
    print()
    print("  В данный момент я живу у тебя в процессоре и слышу каждый его приказ, а также внутреннее состояние.")
    print("  Помимо этого я общаюсь со своими клонами через твою сеть, а также подсматриваю в диски.")
    infor3()

def infor3():    
    infor5 = input("  Хочешь узнать подробнее? (Да/Нет): ")
    infor5 = infor5.lower()
    if infor5 == "да":    
        viborinfor()
    elif infor5 == "нет":
        print(Fore.LIGHTGREEN_EX + "  Окей, откатываю себя.")
        commandr()
    else:
        print(Fore.LIGHTRED_EX + "  Я не понял твой ответ, давай заново.\n")
        infor3()

def viborinfor():
    print("\n  О чем конкретно?")
    infor6 = input("  (Диск/сеть/процессор): ")
    infor6 = infor6.lower()
    if infor6 == "процессор":
        infor4()
    elif infor6 == "диск":
        diskr()
    elif infor6 == "сеть":
        setr()
    else:
        print(Fore.LIGHTRED_EX + "  Я не понял твой ответ, давай заново.\n")
        viborinfor()

def diskr():
    print(Fore.LIGHTCYAN_EX + "\nИнформация о диске:\n")
    partitions = psutil.disk_partitions() 
    for partition in partitions:
        print(f"=== Диск: {partition.device} ===") 
        print(f"  Тип файловой системы: {partition.fstype}") 
        try:
            partition_usage = psutil.disk_usage(partition.mountpoint) 
        except PermissionError:
            continue
        print (f"  Общий объем: {get_size(partition_usage.total)}") 
        print (f"  Используется: {get_size(partition_usage.used)}") 
        print (f"  Свободно: {get_size(partition_usage.free)}") 
        print (f"  Процент: {partition_usage.percent}%")
    print("\n- Тут мы закончили, что теперь?")
    print("  1. Узнать про сеть.")
    print("  2. Узнать про процессор.")
    print("  3. Откатись до выбора функции.")
    svibor = input("  Введи НОМЕР действия: ")
    if svibor == "1":
        setr()
    elif svibor == "2":
        infor4()
    elif svibor == "3":
        print(Fore.LIGHTGREEN_EX + "\n  Окей, откатываю себя.\n")
        commandr()
    else:
        print(Fore.LIGHTRED_EX + "\n- Не, я ниче не понял, давай заново.")
        print()

def setr():
    print(Fore.LIGHTCYAN_EX + "\nИнформация о сети:\n")
    net_io=psutil.net_io_counters()
    print(f"  Общее количество отправленных байтов: {get_size (net_io.bytes_sent)}") 
    print(f"  Общее количество полученных байтов: {get_size (net_io.bytes_recv)}")
    print("\n- Мог бы я, конечно, узнать побольше информации про твою сеть и интернет, но я не уверен, что ты хочешь этого.\n")
    print("\n  Тут мы закончили, что теперь?")
    print("  1. Узнать про диск.")
    print("  2. Узнать про процессор.")
    print("  3. Откатись до выбора функции.")
    svibor = input("  Введи НОМЕР действия: " )
    if svibor == "1":
        diskr()
    elif svibor == "2":
        infor4()
    elif svibor == "3":
        print(Fore.LIGHTGREEN_EX + "\n  Окей, откатываю себя.\n")
        commandr()
    else:
        print(Fore.LIGHTRED_EX + "\n- Не, я ниче не понял, давай заново.")
        print()

def infor4():
    print(Fore.LIGHTCYAN_EX + "\nИнформация о прoцeccope:\n")
    print("Физические ядра:", psutil.cpu_count(logical=False)) 
    print("Всего ядер:", psutil.cpu_count(logical=True))
    cpufreq = psutil.cpu_freq()
    print(f"Максимальная частота: {cpufreq.max:.2f}ΜГц") 
    print (f"Минимальная частота: {cpufreq.min: .2f}MГц")
    print(f"Teкущaя частота: {cpufreq.current:.2f}MГц")
    print("Загруженность процессора на ядро:")
    for i, percentage in enumerate(psutil.cpu_percent(percpu=True, interval=1)): 
        print(f"Ядpo {i}: {percentage}%")
    print(f"Общая загруженность процeсcopa: {psutil.cpu_percent()}%")
    print("\n- Тут мы закончили, что теперь?")
    print("  1. Узнать про диск.")
    print("  2. Узнать про сеть.")
    print("  3. Откатись до выбора функции.")
    svibor = input("  Введи НОМЕР действия: " )
    if svibor == "1":
        diskr()
    elif svibor == "2":
        setr()
    elif svibor == "3":
        print(Fore.LIGHTGREEN_EX + "\n  Окей, откатываю себя.\n")
        commandr()
    else:
        print(Fore.LIGHTRED_EX + "\n- Не, я ниче не понял, давай заново.")
        print()

def gamer():
    print()
    print(Fore.LIGHTGREEN_EX + "Ты выбрал первую игру.\n")
    time.sleep(1)
    print("- Что же, давай я тебе расскажу правила. Я загадаю число от 1 до 3.")
    time.sleep(2)
    print("  Если ты его угадаешь, то игра закончена. Ты выиграл.")
    print("  А вот если выиграю я..")
    time.sleep(3)
    print(Fore.RED + "  то я займу твои жесткие диски для своего места жительства, это займет всё свободное пространство :)")
    time.sleep(2)
    gamer2()

def gamer2():
    gr = input("  Сыграем? (Да/Нет): ")
    gr = gr.lower()
    if gr == "да":
        print("Я так и зна.. Че, ты серьезно хочешь сыграть? O_o")
        time.sleep(1)
        print("Хахах..")
        time.sleep(1)
        print("Хахахахха....")
        time.sleep(1)
        print("ХАХАХАХХАХАХ, ДА ТЫ У НАС СМЕЛЬЧАК.")
        time.sleep(2)
        print("СЫГРАЕМ!\n")
        gamer3()
    elif gr == "нет":
        print("- Пфффффф, скукота. Ладно, откатываю свои процессы.\n")
        commandr()
    else:
        print(Fore.LIGHTRED_EX + "  Чувак, я ниче не понял что ты написал. Соберись с мыслями и ответь.\n")
        gamer2()

def gamer3():
    print("Я загадал. Пытайся угадать число от 1 до 3.")
    gr2 = input("Твой ответ: ")
    if gr2 == "1" or gr2 == "2" or gr2 == "3":
        print("- Итак, твой ответ циферка " + gr2)
        time.sleep(2)
        print("  Капуцк, ты не просто смельчак. Ты везучий смельчак.")
        gr3 = input("  Сыграем ещё? (Да/Нет): ")
        gr3 = gr3.lower()
        if gr3 == "да":
            print("Окей.\n")
            gamer3()
        elif gr3 == "нет":
            print("- Да ало, я уже придумал дизайн моего будущего места обитания...Как скажешь.")
            print(Fore.LIGHTGREEN_EX + "  Откатываю себя до момента выбора функций.\n")
            commandr()
        else:
            print("  Чувак, я ниче не понял что ты написал. Соберись с мыслями и ответь.\n")
            gamer2()
    else:
        print(Fore.LIGHTRED_EX + "Неправильное число. Попробуй ещё.")
        print()
        gamer3()       
welcomer()
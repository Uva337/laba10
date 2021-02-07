#!/usr/bin/env python3
# -*- config: utf-8 -*-

# 8.Использовать словарь, содержащий следующие ключи: название пункта назначения; номер
# поезда; время отправления. Написать программу, выполняющую следующие действия:
# ввод с клавиатуры данных в список, состоящий из словарей заданной структуры; записи должны
# быть упорядочены по номерам поездов;
# вывод на экран информации о поезде, номер которого введен с клавиатуры; если таких поездов нет,
# выдать на дисплей соответствующее сообщение.


import sys
import json


def add(poezd, name, num, time):
    poez = {
        'name': name,
        'num': num,
        'time': time,
    }

    poezd.append(poez)
    if len(poezd) > 1:
        poezd.sort(key=lambda item: item.get('num', ''))


def list(poezd):
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 17
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^17} |'.format(
            "№",
            "Пункт назначения",
            "Номер поезда",
            "Время отправления"
        )
    )
    print(line)

    for idx, poez in enumerate(poezd, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>17} |'.format(
                idx,
                poez.get('name', ''),
                poez.get('num', ''),
                poez.get('time', 0)
            )
        )

    print(line)


def select(poezd):
    count = 0
    for poez in poezd:
        if poez.get('time') == time:
            count += 1
            print('Время отправления:', poez.get('time', ''))
            print('Номер поезда:', poez.get('num', ''))
            print('Пункт назначения:', poez.get('name', ''))


        if count == 0:
            print("Таких поездов нет!")


def load(parts):
    with open(parts, 'r') as f:
         return poezd

def save(poezd, parts):
    with open(parts, 'w') as f:
        json.dump(poezd, f)


if __name__ == '__main__':

    poezd = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            name = input("Название пункта назначения: ")
            num = int(input("Номер поезда: "))
            time = input("Время отправления: ")

            add(poezd, name, num, time)

        elif command == 'list':
            print(list(poezd))

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)

            number = int(parts[1])
            select(poezd)

        elif command.startswith('load '):
            parts = command.split(' ', maxsplit=1)
            poezd = load(parts[1])

        elif command.startswith('save '):
            parts = command.split(' ', maxsplit=1)
            save(poezd, parts[1])

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить поезд;")
            print("list - вывести список поездов;")
            print("select <номер поезда> - запросить информацию о выбранном поезде;")
            print("load <имя_файла> - загрузить данные из файла;")
            print("save <имя_файла> - сохранить данные в файл;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
            

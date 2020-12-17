#!/usr/bin/env python3
# -*- config: utf-8 -*-

# Использовать словарь, содержащий следующие ключи: фамилия, имя; номер телефона;
# дата рождения. Написать программу, выполняющую следующие
# действия: ввод с клавиатуры данных в список, состоящий из словарей заданной структуры;
# записи должны быть упорядочены по трем первым цифрам номера телефона; вывод на
# экран информации о человеке, чья фамилия введена с клавиатуры; если такого нет, выдать
# на дисплей соответствующее сообщение.
import sys


def add(people, surname, name, number, year):
    peop = {
        'surname': surname,
        'name': name,
        'number': number,
        'year': year
    }

    people.append(peop)
    if len(people) > 1:
        people.sort(key=lambda item: item.get('number', '3'))

def list(people):
    line = '+-{}-+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 20,
        '-' * 20,
        '-' * 20,
        '-' * 15
    )
    print(line)
    print(
        '| {:^4} | {:^20} | {:^20} | {:^20} | {:^15} |'.format(
            "№",
            "Фамилия ",
            "Имя",
            "Номер телефона",
            "Дата рождения"
        )
    )
    print(line)

    for idx, peop in enumerate(people, 1):
        print(
            '| {:>4} | {:<20} | {:<20} | {:<20} | {:>15} |'.format(
                idx,
                peop.get('surname', ''),
                peop.get('name', ''),
                peop.get('number', ''),
                peop.get('year', 0)
            )
        )
    print(line)


def select(people):
    count = 0
    for peop in people:
        if peop.get('surname') == sur:
            count += 1
            print('Фамилия:', peop.get('surname', ''))
            print('Имя:', peop.get('name', ''))
            print('Номер телефона:', peop.get('number', ''))
            print('Дата рождения:', peop.get('year', ''))

    if count == 0:
        print("Таких фамилий нет !")


if __name__ == '__main__':

    people = []

    while True:
        command = input(">>> ").lower()

        if command == 'exit':
            break

        elif command == 'add':
            surname = input("Фамилия ")
            name = input("Имя ")
            number = int(input("Номер телефона "))
            year = input("Дата рождения в формате: дд.мм.гггг ")

            add(people, surname, name, number, year)

        elif command == 'list':
            print(list(people))

        elif command.startswith('select '):
            parts = command.split(' ', maxsplit=2)

            sur = (parts[1])
            select(people)

        elif command == 'help':
            print("Список команд:\n")
            print("add - добавить человека;")
            print("list - вывести список людей;")
            print("select <фамилия> - запросить информацию по фамилии;")
            print("help - отобразить справку;")
            print("exit - завершить работу с программой.")

        else:
            print(f"Неизвестная команда {command}", file=sys.stderr)
# на Отлично
# в одного человека надо сделать
# консольное приложение Телефонный справочник
# с внешним хранилищем информации,
# и чтоб был реализован основной функционал - просмотр,
# сохранение, импорт, поиск, удаление, изменение данных.
# Задача 38: 
# Дополнить телефонный справочник 
# возможностью изменения и удаления данных. 
# Пользователь также может ввести имя или фамилию, 
# и Вы должны реализовать функционал для изменения и удаления данных

# для отлично в группах 
# надо выполнить или ТГ бот или ГУИ 
# (это когда кнопочки и поля ввода как в Виндовс приложениях) или БД
# ГУИ можно сделать просто на EasyGUI или Tkinter

from easygui import *

def show_data(filename: str):
    with open(filename, "r", encoding="utf-8") as f:
        msgbox(f.read())


def add_data(filename: str):
    with open(filename, "a", encoding="utf-8") as f:
        fio = enterbox("Введите ФИО: ")
        phone_number = enterbox("Введите номер телефона: ")
        f.write(f"{fio} | {phone_number}\n")
        msgbox(f"Добавлена запись : {fio} | {phone_number}")


def find_data(filename: str):
    search_line = enterbox("Введите ФИО или номер для поиска: ")
    search_line = search_line.upper()
    with open(filename, "r", encoding='utf-8') as f:
        tel_book = f.read()
        find_list = search(tel_book, search_line)
        return find_list


def find_one_line(filename: str):
    find_list = find_data(filename)
    if len(find_list) > 1:
        msgbox("Найдены записи:")
        for index in range(len(find_list)):
            msgbox(f"{index + 1} - {find_list[index]}")
        index_element = int(enterbox("Введите номер записи для редактирования: ")) - 1
        msgbox(f"Для редактирования выбрана запись - {find_list[index_element]}")
        return find_list[index_element]
    elif len(find_list) == 1:
        msgbox(f"Для редактирования выбрана запись - {find_list[0]}")
        return find_list[0]
    else:
        msgbox("Поиск не дал результатов.")
        return ""


def search(book: str, search_str: str):
    book = book.split("\n")
    result = []
    for line in book:
        if search_str in line.upper():
            result.append(line)      
    return result


def edit_data(filename: str):
    with open(filename, "r", encoding='utf-8') as f:
        tel_book = f.read()
    tel_book_lines = tel_book.split("\n")
    target_line = find_one_line(filename)
    while len(target_line) == 0:
        target_line = find_one_line(filename)
    edited_line = edit_line(target_line)
    tel_book_lines[tel_book_lines.index(target_line)] = edited_line
    msgbox(f"Запись - {target_line}, изменена на - {edited_line}")
    with open(filename, "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))


def edit_line(line: str):
    elements = line.split(" | ")
    fio = enterbox("Введите ФИО: ")
    phone = enterbox("Введите номер телефона: ")
    if len(fio) == 0:
        fio = elements[0]
    if len(phone) == 0:
        phone = elements[1]
    return f"{fio} | {phone}"


def remove_data(filename: str):
    with open(filename, "r", encoding='utf-8') as f:
        tel_book = f.read()
    tel_book_lines = tel_book.split("\n")
    find_list = find_data(filename)
    while len(find_list) == 0:
        find_list = find_data(filename)
    if len(find_list) > 0:
        result = ''
        # msgbox("Найдены записи:")
        for index in range(len(find_list)):
            result += f'{find_list[index]}\n'
            # (f"{index + 1} - {find_list[index]}")
        msgbox(result,'Найдены записи:', 'ОСТОРОЖНО! УДАЛЕНИЕ!!!!')
        index_for_remove = int(
            enterbox("Введите номер строки для удаления, или 0 для удаления всех найденных строк: ")) - 1
        if 0 <= index_for_remove < len(find_list):
            msgbox(f"Удалена запись: {find_list[index_for_remove]}")
            tel_book_lines.pop(tel_book_lines.index(find_list[index_for_remove]))
        elif index_for_remove == -1:
            for index in find_list:
                tel_book_lines.pop(tel_book_lines.index(index))
            msgbox(f"Удалено записей: {len(find_list)}")
        else:
            msgbox("Удалено записей: 0")
    with open(filename, "w", encoding='utf-8') as f:
        f.write("\n".join(tel_book_lines))


close = False

file_phone_book = "phone_book.txt"
with open(file_phone_book, "a", encoding="utf-8") as file:
    file.write("")

while not close:
    action = buttonbox('Выберите нужный пункт МЕНЮ:', "Программа для редактирование и отображения данных справочника.",  ('Просмотр', 'Добавление', 'Поиск', 'Изменение', 'Удаление', 'Выход'))
    #  = int(enterbox("Действие: "))
    if action == 'Просмотр':
        show_data(file_phone_book)
    elif action == 'Добавление':
        add_data(file_phone_book)
    elif action == 'Поиск':
        for i in find_data(file_phone_book):
            msgbox(i)
    elif action == 'Изменение':
        edit_data(file_phone_book)
    elif action == 'Удаление':
        remove_data(file_phone_book)
    else:
        close = True



















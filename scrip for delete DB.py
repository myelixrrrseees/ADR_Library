import sqlite3


def delete_record(one_id_del):
    try:
        sqlite_connection = sqlite3.connect('flsite.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sql_delete_query = f"""DELETE from users WHERE id = {one_id_del}"""
        cursor.execute(sql_delete_query)
        sqlite_connection.commit()
        print("Запись успешно удалена")
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


def delete_multiple_records(ids_list):
    try:
        sqlite_connection = sqlite3.connect('flsite.db')
        cursor = sqlite_connection.cursor()
        print("Подключен к SQLite")

        sqlite_update_query = """DELETE from users where id = ?"""
        cursor.executemany(sqlite_update_query, ids_list)
        sqlite_connection.commit()
        print("Удалено записей:", cursor.rowcount)
        sqlite_connection.commit()
        cursor.close()

    except sqlite3.Error as error:
        print("Ошибка при работе с SQLite", error)
    finally:
        if sqlite_connection:
            sqlite_connection.close()
            print("Соединение с SQLite закрыто")


print('1. Удаление одной записи')
print('2. Удаление некого колличества записей')

nomer_delete = int(input('Введите способ удаления: '))

if nomer_delete == 1:

    print('\n')
    one_id_del = int(input('Введите номер id: '))
    print('\n')

    delete_record(one_id_del)

if nomer_delete == 2:

    print('\n')
    since_list_id_del = int(input('Введите id, с которого начнется список: '))
    to_list_id_del = int(input('Введите id, на котором закончится список: '))
    list = [(since_list_id_del,), (to_list_id_del,)]
    print('\n')

    delete_multiple_records(list)
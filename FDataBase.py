import sqlite3
import time
import math
from PIL import Image


def convert_data(data, file_name):

    with open(file_name, 'wb') as file:
        file.write(data)
    img = Image.open(file_name)
    return img


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def getMenuUser(self):
        sql = '''SELECT * FROM users'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except:
            print("Ошибка чтения из БД")
        return []

    def getMenuBook(self):
        sql = '''SELECT * FROM books'''
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res

        except:
            print("Ошибка чтения из БД")

        return []

    def addUser(self, email, name, password):
        try:
            self.__cur.execute(f"SELECT COUNT() as `count` FROM users WHERE email LIKE '{email}'")
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Пользователь с таким email уже существует")
                return False

            self.__cur.execute(f"SELECT COUNT() as `count` FROM users WHERE name LIKE '{name}'")
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Пользователь с таким name уже существует")
                return False

            tm = math.floor(time.time())
            self.__cur.execute("INSERT INTO users VALUES(NULL, ?, ?, ?, NULL, ?)", (email, name, password, tm))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления в БД " + str(e))
            return False

        return True

    def getUser(self, id):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE id = {id} LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False

            return res
        except sqlite3.Error as e:
            print("Ошибка получения данных из БД" + str(e))

        return False

    def getUserByEmail(self, email):
        try:
            self.__cur.execute(f"SELECT * FROM users WHERE email = '{email}' LIMIT 1")
            res = self.__cur.fetchone()
            if not res:
                print("Пользователь не найден")
                return False

            return res
        except sqlite3.Error as e:
            print("Ошибка получения данных из БД" + str(e))

        return False

    def updateUserAvatar(self, avatar, user_id):
        if not avatar:
            return False

        try:
            binary = sqlite3.Binary(avatar)
            self.__cur.execute(f"UPDATE users SET avatar = ? WHERE id = ?", (binary, user_id))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка обновления аватара в БД " + str(e))
            return False

        return True




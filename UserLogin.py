from FDataBase import FDataBase
from flask_login import UserMixin
from flask import url_for


class UserLogin(UserMixin):

    def fromDB(self, user_id, db):
        try:
            self.__user = db.getUser(user_id)
        except:
            print('Не успешно')
        return self

    def create(self, user):
        try:
            self.__user = user
        except:
            print('Не успешно')
        return self

    def get_id(self):
        return str(self.__user['id'])

    def getName(self):
        return self.__user['name'] if self.__user else "Без имени"

    def getEmail(self):
        return self.__user['email'] if self.__user else "Без email"

    def getAvatar(self, app):
        img = None
        try:
            img = self.__user['avatar']
        except FileNotFoundError as e:
            print(e)

        return img

    def verifyExt(self, filename):
        ext = filename.rsplit('.', 1)[1]
        if ext == "png" or ext == "PNG":
            return True
        return False

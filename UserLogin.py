from FDataBase import FDataBase


class UserLogin():

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

    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.__user['id'])

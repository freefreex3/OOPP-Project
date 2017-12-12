class Users:
    def __init__(self, username, password, phone_no, email):
        self.__username = username
        self.__password = password
        self.__phone_no = phone_no
        self.__email = email

    def get_username(self):
        return self.__username
    def set_username(self, username):
        self.__username = username

    def get_password(self):
        return self.__password
    def set_password(self, password):
        self.__password = password

    def get_phone_no(self):
        return self.__phone_no
    def set_phone_no(self, phone_no):
        self.__phone_no = phone_no

    def get_email(self):
        return self.__email
    def set_email(self, email):
        self.__email = email

class Technician(Users):
    def __init__(self, ):


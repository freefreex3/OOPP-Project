from Users import Users

class technician(users):
    def __init__(self, username, password, phone_no, email, occupation):
        Users.__init__(self, username, password, phone_no, email)
        self.__occupation = occupation

    def get_occupation(self):
        return self.__occupation

    def set_occupation(self, occupation):
        self.__occupation = occupation


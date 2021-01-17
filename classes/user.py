from models.model import UserModel
from migrations import users


class User:
    def __init__(self, data: UserModel):
        self.id = data.id
        self.name = data.name
        self.email = data.email
        self.password = data.password
        self.zip_code = data.zip_code

    def save(self):
        print("Inserindo {}".format(self.__dict__))
        users.insert(self.__dict__)

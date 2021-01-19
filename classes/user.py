from models.model import UserModel, Geolocation


class User:
    def __init__(self, data: UserModel):
        self.id = data.id
        self.name = data.name
        self.email = data.email
        self.password = data.password
        self.zip_code = data.zip_code
        self.born_date = data.born_date
        self.city = data.city
        self.geolocation = data.geolocation.dict()
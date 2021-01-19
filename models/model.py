from pydantic import BaseModel
from datetime import date as dt


class Geolocation(BaseModel):
    lat: float
    lng: float


class UserModel(BaseModel):
    id: str
    name: str
    email: str
    password: str
    zip_code: str
    born_date: dt
    city: str
    geolocation: Geolocation

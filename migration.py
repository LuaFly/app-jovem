from migrations import users
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

users.create(True)
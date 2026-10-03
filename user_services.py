import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.database import database
from models.user import user

class user_services:
    def __init__(self,database):
        self.database=database

    def add_user(self,user):
        self.database.insert("users_info","user_name,Email,national_id,phone_number,password",
                    f"'{user.user_name}','{user.email}',{user.national_id},'{user.phone_number}','{user.password}'")

    def get_user(self,user_id):
        result=self.database.fetch_where("*", "users_info", "user_id",user_id)
        if result:
            return user(*result)
        return None
    def login(self,Email,password):
        result_e=self.database.fetch_where("*","users_info","Email",Email)
        if not result_e:
            return "invalid Email"
        result_p=self.database.fetch_where("password", "users_info", "Email",Email)
        if password!=result_p:
            return "Wrong password"
        return user(*result_e)

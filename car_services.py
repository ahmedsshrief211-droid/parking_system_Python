import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.database import database
from models.car import car

class car_services:
    def __init__(self,database):
        self.database=database

    def add_car(self,user_id,brand,model,year,plate_number):
        self.database.insert("car","user_id,brand,model,year,plate_number",
                f"'{self.user_id}','{self.brand}','{self.model}','{self.year}','{self.plate_number}'")

    def get_car(self,car_id):
        result=self.database.fetch_where("*", "car", "car_id",car_id)
        if result:
            return car(*result)
        return None

    def get_users_car(self,user_id):
        result=self.database.fetch_all_where("*","car","user_id",user_id)
        return result

    def update_car(self,column,updated_value,car_id):
        self.database.update("car",column,updated_value,"car_id",car_id)

    def delete_car(self,car_id):
        self.database.delete("car","car_id",car_id)
        


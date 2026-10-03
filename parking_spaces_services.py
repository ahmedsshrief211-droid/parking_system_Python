import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.database import database
from models.parking_spaces import parking_spaces

class parking_spaces_services:
    def __init__(self,database):
        self.database=database

    def get_space(self,space_id):
        result=self.database.fetch_where("*", "parking_spaces", "space_id",space_id)
        if result:
            return parking_spaces(*result)
        return None

    def get_all_spaces(self):
        result=self.database.fetch_all("*","parking_spaces")
        if result:
            return parking_spaces(*result)
        return None

    def get_available_spaces(self):
        result=self.database.fetch_all_where("*","parking_spaces","status","available")
        if result:
            return result
        return None

    def recommend_space(self):
        spaces=self.get_available_spaces()
        if spaces:
            return spaces[0]
        return None

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from database.database import database
from models.reservation import reservation

class reservation_services:
    def __init__(self,database):
        self.database=database

    def create_reservation(self, user_id, car_id, space_id):
        space=self.database.fetch_where("*","parking_spaces","space_id",space_id)
        if not space:
            return "Space not found"

        if space[3]!="available":
            return "Space is not available"
        
        car=self.database.fetch_where("*","car","car_id",car_id)
        if not car or car[1]!=user_id:
            return "Car not found"

        self.database.insert("reservations","user_id,car_id,space_id",f"{user_id},{car_id},{space_id}")
        self.database.update("status","parking_spaces","reserved","space_id",space_id)
        return "Reservation created successfully"

    def get_user_reservations(self,user_id):
        result=self.database.fetch_all_where("*","reservations","user_id",user_id)
        if result:
            return result
        return None

    def cancel_reservation(self,reservation_id,user_id):
        reservation = self.database.fetch_where("*","reservations","reservation_id",reservation_id)
        if not reservation or reservation[1]!=user_id:
            return "Reservation not found"

        self.database.update("status","reservations","cancelled","reservation_id",reservation_id)
        self.database.update("status","parking_spaces","available","space_id",reservation[3])
        return "Reservation cancelled successfully"
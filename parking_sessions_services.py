import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from database.database import database
from models.parking_sessions import parking_sessions
from datetime import datetime
import math

class parking_sessions_services:
    def __init__(self,database):
        self.database=database

    def start_session(self,user_id,reservation_id):
        reservation=self.database.fetch_where("*","reservations","reservation_id",reservation_id)
        if not reservation or reservation[1]!=user_id:
            return "Reservation not found"

        start_time=datetime.now().strftime("%Y/%m/%d %H:%M:%S")
        self.database.insert("parking_sessions","reservation_id,start_time",f"{reservation_id},'{start_time}'")
        return "Parking session started successfully"

    def end_session(self,session_id):
        session=self.database.fetch_where("*","parking_sessions","session_id",session_id)
        if not session:
            return "Session not found"

        end_time=datetime.now().strftime("%Y/%m%d %H:%M:%S")
        start_time=datetime.strptime(session[2],"%Y/%m/%d %H:%M:%S")
        end_datetime=datetime.strptime(end_time,"%Y/%m/%d %H:%M:%S")
        total_time=end_datetime-start_time
        hours=math.cell(int(total_time.total_seconds()/3600))
        cost=hours*50
        self.database.update("end_time","parking_sessions",end_time,"session_id",session_id)
        self.database.update("cost","parking_sessions",cost,"session_id",session_id)
        return cost

    def get_user_sessions(self,user_id):
        result=self.database.fetch_all_where("*","parking_sessions","user_id",user_id)
        if result:
            return result
        return None
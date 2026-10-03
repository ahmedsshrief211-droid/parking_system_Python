import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))
from database.database import database

class payment_services:
    def __init__(self,database):
        self.database=database

    def create_payment(self,session_id,payment_method):
        session=self.database.fetch_where("*","parking_sessions","session_id",session_id)
        if not session:
            return "Session not found"

        if session[5] is None:
            return "Session not finished"
        
        payment=self.database.fetch_where("*","payments","session_id",session_id)
        if payment:
            return "Payment already exists"

        amount=session[6]
        self.database.insert("payments","session_id,amount,payment_method,payment_status",f"{session_id},{amount},'{payment_method}','paid'")
        return "Payment is successful"

    def get_payment(self,payment_id):
        result=self.database.fetch_where("*","payments","payment_id",payment_id)
        if result:
            return result
        return None
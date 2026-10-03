import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class parking_sessions:
    def __init__(self,car_id,space_id,reservation_id,entry_time,exist_time,cost):
        self.car_id=car_id
        self.space_id=space_id
        self.resrvation_id=reservation_id
        self.entry_time=entry_time
        self.exit_time=exist_time
        self.cost=cost

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class reservation:
    def __init__(self,car_id,space_id,reservation_time,entry_time,exist_time,reservation_status):
        self.car_id=car_id
        self.space_id=space_id
        self.resrvation_time=reservation_time
        self.entry_time=entry_time
        self.exit_time=exist_time
        self.reservation_status=reservation_status

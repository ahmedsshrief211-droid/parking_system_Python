import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class car:
    def __init__(self,user_id,brand,model,year,plate_number):
        self.user_id=user_id
        self.brand=brand
        self.model=model
        self.year=year
        self.plate_number=plate_number

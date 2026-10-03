import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

class parking_spaces:
    def __init__(self,space_number,section,status):
        self.space_number=space_number
        self.section=section
        self.status=status

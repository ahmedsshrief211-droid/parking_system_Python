import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


class user:
    def __init__(self,user_name,Email,national_id,phone_number,password):
        self.user_name=user_name
        self.email=Email
        self.national_id=national_id
        self.phone_number=phone_number
        self.password=password


# u1=user("ahmed","ahmed@gmail.com",78903457082354,"573280975","hsjadfe9qw8")
# u1.add_user()
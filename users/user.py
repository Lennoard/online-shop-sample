class User:

    def __init__(self, uid: str, name: str, email: str, password: str, phone_number: int, is_admin: bool = False):
        self.uid = uid
        self.name = name
        self.email = email
        # For the purpose of this sample only
        self.password = password
        self.phone_number = phone_number
        self.is_admin = is_admin

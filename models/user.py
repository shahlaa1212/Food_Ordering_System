from utilities.general_utils import generate_id
class User:
    def __init__(self, first_name, last_name, username, password, is_loggedin, role) -> None:
        self.id = generate_id()
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.password = password
        self.is_loggedin = is_loggedin
        self.role = role
    
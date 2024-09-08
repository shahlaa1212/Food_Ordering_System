from models.user import User
from services import user_service
from utilities.general_utils import verify_password, hash_password

class AuthenticationService:
    def __init__(self, user_service):
        self.user_service = user_service
        self.current_user = None
    
    def signup(self, first_name, last_name, username, password, age):
        hashed_password = hash_password(password)
        new_user = User(username=username, password=hashed_password, age=age, first_name=first_name, last_name=last_name)
        self.user_service.add(new_user.to_dict())
        return "Signup successful!"
   
    def signin(self, username, password):
        users = self.user_service.list_all()
        for user in users:
            if user['username'] == username and verify_password(user['password'], password):
                user['is_loggedin'] = True
                self.user_service.update(user['id'], {'is_loggedin': True}, {'role': 'admin'})
                self.current_user = user
                return True
        print("Invalid credentials!")
        return False
 
    def signout(self, user_id):
        if self.current_user and self.current_user['user_id'] == user_id:
            self.current_user = None
            return "Signout successful!"
        return "User is not signed in"

from utilities.base_service import BaseService
from models.user import User
from utilities.data_utils import load_data, save_data
from utilities.general_utils import generate_id

class UserService(BaseService):
    def __init__(self, file_path='database/users.txt'):
        self.file_path = file_path
        self.users = load_data(self.filename)
          
    def list_all(self):
        self.users = load_data(self.file_path)
        return self.users

    def add(self, user):
        # todo: implement this method
        user_id = generate_id()
        hashed_password = hash_password(password)
        new_user = {'user_id': user_id, 'username': username, 'password': hashed_password, 'role': role}
        self.users.append(new_user)
        save_data(self.file_path, self.users)

    def remove(self, user_id):
        # todo: implement this method
        self.users = [user for user in self.users if user['user_id'] != user_id]
        save_data(self.file_path, self.users)

    def update(self, user_id, updated_info):
        for user in self.users:
            if user['user_id'] == user_id:
                user.update(updated_user)
        save_data(self.file_path, self.users)

   
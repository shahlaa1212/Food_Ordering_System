from utilities.base_service import BaseService
from utilities.data_utils import load_data, save_data, append_data
from models.meal import Meal

class MealService(BaseService):
    def __init__(self, file_path='database/meals.txt'):
        self.file_path = file_path
        self.meals = load_data(self.filename)
    
    def list_all(self):
        self.meals = load_data(self.file_path)
        return self.meals

    def add(self, meal, current_user):
        if not isinstance(current_user, dict) or current_user.get('role') != 'admin':
            raise PermissionError("Only admins can add meals.")
        meal_dict = meal.to_dict()
        meal_dict['id'] = str(uuid.uuid4())

        save_data(self.file_path, meal_dict)
        return meal_dict
    
    def remove(self, meal_id):
        # todo: implement this method
        self.meals = [meal for meal in self.meals if meal['meal_id'] != meal_id]
        save_data(self.file_path, self.meals)

    def update(self, meal_id, updated_info):
        for meal in self.meals:
            if meal['meal_id'] == meal_id:
                meal.update(updated_meal)
        save_data(self.file_path, self.meals)


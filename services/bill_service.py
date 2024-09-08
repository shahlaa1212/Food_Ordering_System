from utilities.base_service import BaseService
from models.bill import Bill
from utilities.data_utils import load_data, save_data
from utilities.general_utils import generate_id
import uuid

class BillService(BaseService):  
    def __init__(self, file_path='database/bills.txt'):
        self.file_path = file_path
        self.bills = load_data(self.file_path)
    
    def list_all(self):
        self.bills = load_data(self.file_path)
        return self.bills

    def add(self):
        bill_id = generate_id()
        new_bill = {'bill_id': bill_id, 'user_id': user_id, 'meal_id': meal_id, 'total_amount': total_amount}
        self.bills.append(new_bill)
        save_data(self.file_path, self.bills)

    def remove(self, bill_id):
        self.bills = [bill for bill in self.bills if bill['bill_id'] != bill_id]
        save_data(self.file_path, self.bills)
 
    def update(self, bill_id, updated_info):
        for bill in self.bills:
            if bill['bill_id'] == bill_id:
                bill.update(updated_bill)
        save_data(self.file_path, self.bills)



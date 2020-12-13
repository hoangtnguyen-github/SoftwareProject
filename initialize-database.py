import pymongo
import datetime
import os
from dotenv import load_dotenv

## necessary for python-dotenv ##
##APP_ROOT = os.path.join(os.path.dirname(__file__), '..')   # refers to application_top
##dotenv_path = os.path.join(APP_ROOT, '.env')
##load_dotenv(dotenv_path)

##mongo = os.getenv('MONGO')

MONGO = "mongodb+srv://software-app:aVKT90MHrk9edtfy@cluster0.jifle.mongodb.net/warehouseInventory?retryWrites=true&w=majority"

SECRET_KEY = "al;dskl;fjads"

client = pymongo.MongoClient(MONGO)

db = client['warehouseInventory']

users = db['users']
roles = db['roles']
items = db['items']



def add_role(role_name):
    role_data = {
        'role_name': role_name
    }
    return roles.insert_one(role_data)



def add_user(empID, first_name, last_name, shift, email, password, role, username1, birthday):
    user_data = {
        'empID': empID,
        'first_name': first_name,
        'last_name': last_name,
        'shift': shift,
        'email': email,
        'password': password,
        'role': role,
        'username1': username1,
        'birthday': birthday,
        'date_hired': datetime.datetime.now(),
        'date_modified': datetime.datetime.now()
    }
    return users.insert_one(user_data)


def add_item(itemid, name, shift_added, material, location, price, weight, addedby):
    item_data = {
        'itemid': itemid,
        'name': name,
        'shift_added': shift_added,
        'material': material,
        'location': location,
        'price': price,
        'weight': weight,
        'addedby': addedby,
        'date_added': datetime.datetime.now(),
        'date_modified': datetime.datetime.now()
    }
    return items.insert_one(item_data)


def initial_database():
    # add roles
    admin = add_role('admin')
    contributor = add_role('contributor')
    user = add_role('user')

    # add users
    hoang = add_user('1', 'Hoang', 'Nguyen', '1', 'hoang@hoang.com', 'abc123', 'admin', 'hoangnguyen', '1/20/2020')


   
    # add item
    table = add_item('1', 'table', '1', 'metal', 'A16', '$120', '200', 'hoangnguyen1')


def main():
    initial_database()
   

main()

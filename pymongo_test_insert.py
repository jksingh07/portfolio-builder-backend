# Get the database using the method we defined in pymongo_test_insert file
from pymongo_get_database import get_database
from dateutil import parser
from datetime import datetime

dbname = get_database()
collection_name = dbname["Login"]

# item_1 = {
#   "_id" : "U1IT00001",
#   "email" : "jaskaran@gmail.com",
#   "password" : "asdf@123",
#   "uname" : "Jaskaran99",
# }

# item_2 = {
#   "_id" : "U1IT00002",
#   "email" : "sahil@gmail.com",
#   "password" : "asdf@123",
#   "uname" : "Sahil99",
# }
# collection_name.insert_many([item_1,item_2])



# datetime object containing current date and time
now = datetime.now()
# dd/mm/YY H:M:S
dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
curr_date = parser.parse(dt_string)
item_3 = {
  "email" : "dummy@gmail.com",
  "password" : "pass",
  "uname" : "dummy",
  "date": curr_date
}
collection_name.insert_one(item_3)

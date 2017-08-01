from database.mysql import MySQLDatabase
from settings import db_config

"""
Retrieve the settings from the
'db_config' dictionary to connect to
our database so we can instantiate our
MySQLDatabase object
"""

db = MySQLDatabase(db_config.get('db_name'),
                   db_config.get('user'),
                   db_config.get('pass'),
                   db_config.get('host'))



### Selecting Rows ###

# Get all the records from the people table
results = db.select('people')

for row in results:
    print row


# selecting columns with named tuples
results = db.select('people', columns=['id', 'first_name'], named_tuples = True)

for row in results:
    print row.id, row.first_name


# we can also do more complex queries using 'CONCAT' and 'SUM'
people = db.select('people', columns=["CONCAT(first_name, ' ', last_name)" \
                                      " AS full_name", "SUM(amount)" \
                                      " AS total_spend"],
                   named_tuples=True, where="people.id=1",
                   join="orders ON people.id=orders.person_id")
 
for person in people:
    print person.full_name, "spent ", person.total_spend



### Inserting Info ###
    
# Inserting an order
db.insert('orders', person_id="2", amount="120.00")



### Updating Info ###

# Updating a person
person = db.select('people', named_tuples=True)[0] 
db.update('profiles', where="person_id=%s" % person.id, address="1a another street")



### Deleting Info ###

# Deleting a record
person = db.select('people',named_tuples=True)[0]
db.delete('orders', person_id="=%s" % person.id, id="=1")

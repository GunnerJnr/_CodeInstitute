from flask import Flask
from flask import render_template
from pymongo import MongoClient
import json

app = Flask(__name__)

# connection settings
MONGODB_HOST = 'localhost'
MONGODB_PORT = 27017
DB_NAME = 'avengers'
COLLECTION_NAME = 'avengers_project'


#
@app.route('/')
def dashboard():
    """

    :return:
    """
    return render_template("index.html")


# routing to the database info
@app.route("/avengers/avengers_project")
def avengers_projects():
    """
    A flask view to serve the project data from
    MongoDB in JSON format.
    :return: the database data in JSON format file
    """

    # define a constant with the record fields we wish to retrieve
    FIELDS = {
        '_id': False, 'Name': True, 'Current': True,
        'Gender': True, 'Year': True,
        'Honorary': True, 'Appearances': True, 'URL': True
        }

    # open a connection to MongoDB, we will use a 'WITH' statement
    # this allows the connection to close as soon as we leave the 'WITH' statement
    with MongoClient(MONGODB_HOST, MONGODB_PORT) as connection:
        # define the collection of data we wish to access
        collection = connection[DB_NAME][COLLECTION_NAME]
        # retrieve a result set with the fields defined in FIELDS
        # and then we will limit the results to 55000
        projects = collection.find(projection=FIELDS, limit=55000)
        # convert projects to a list in a JSON object and return the JSON data
        return json.dumps(list(projects))


# FOR DEBUGGING USE ONLY [COMMENT THIS OUT]
if __name__ == '__main__':
    app.run(debug=True)

""" [UNCOMMENT THIS]
if __name__ == '__main__':
    app.run()
"""
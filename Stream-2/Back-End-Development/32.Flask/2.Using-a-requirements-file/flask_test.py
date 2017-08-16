from flask import Flask

# create an instance of our class and pass the name of our module
# the app instance needs to know the name so it can find our templates and static folder files
app = Flask(__name__)

# A route has been defined using a decorator. Unlike the timeit decorator,
# this one takes a url as an argument. The decorator is saying ‘if the user navigates to the
# address /, then run the function below’, i.e. the decorated function.
@app.route('/')
def hello_world():
    # Our function returns the text ‘Hello World’
    return 'Hello World!'

# use if __name__ == ‘__main__’: to ensure the app is only run when instantiated directly
# from the Python interpreter, not when imported from another file
if __name__ == '__main__':
    # run our app using app.run()
    app.run()

from flask import Flask

# create an instance of our class and pass the name of our module
# the app instance needs to know the name so it can find our templates and static folder files
app = Flask(__name__)

ages = {
    'bob': '43',
    'alice': '29'
}

@app.route('/users/<user>')
def users(user):
    age = ages.get(user)
    if age:
        return '%s is %s years old' % (user, age)
    else:
        abort(404)

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

'''
It’s also possible to automatically convert numbers to ints and floats by using this conversion syntax.

If our users were stored in a list, we could have used this syntax:

@app.route('/users/<int:user_id>')
def users(user_id):
'''

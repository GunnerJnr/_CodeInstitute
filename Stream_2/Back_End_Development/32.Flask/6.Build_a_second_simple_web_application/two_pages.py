from flask import Flask
from flask import render_template # Add this as the last import at the beginning of the file

# create an instance of our class and pass the name of our module
# the app instance needs to know the name so it can find our templates and static folder files
app = Flask(__name__)

# A route has been defined using a decorator. Unlike the timeit decorator,
# this one takes a url as an argument. The decorator is saying ‘if the user navigates to the
# address /, then run the function below’, i.e. the decorated function.
@app.route('/')
def home():
    return render_template('home.html')
@app.route('/about')
def about():
    return render_template('about.html')

# use if __name__ == ‘__main__’: to ensure the app is only run when instantiated directly
# from the Python interpreter, not when imported from another file
if __name__ == '__main__':
    # run our app using app.run()
    app.run()

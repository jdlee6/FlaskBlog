# import the create_app function that we created
from flaskblog import create_app

# create our application
# we could've passed in configurations as arguments but it is using the Config class as default
app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
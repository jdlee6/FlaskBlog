from flask import Blueprint, render_template

# create a new Blueprint for errors
errors = Blueprint('errors', __name__)

# error handlers in our application is similar to how we create our routes except we use the decorator below
# error handler for a 404 
# create error_404 function with the error parameter
@errors.app_errorhandler(404)
def error_404(error):
    # import the render template function
    # we will create this template in a subdirectory called errors within our templates directory 
    # return the status code so we can specify the response(default is 200 which means success)
    return render_template('errors/404.html'), 404

''' copy and paste this for our other error responses '''

@errors.app_errorhandler(403)
def error_403(error):
    return render_template('errors/403.html'), 403

@errors.app_errorhandler(500)
def error_500(error):
    return render_template('errors/500.html'), 500

''' note there is also another method called just 
.errorhandler() but that will only work for that specific blueprint. 
app.errorhandler() will allow us to work across the entire application '''
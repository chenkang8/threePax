import logging
from flask import Flask, redirect, url_for, render_template, request, current_app, json

app = Flask(__name__)

# For use with gunicorn
if __name__ != '__main__':
    gunicorn_logger = logging.getLogger('gunicorn.error')
    app.logger.handlers = gunicorn_logger.handlers
    app.logger.setLevel(gunicorn_logger.level)
    app.logger.debug("THIS IS A TEST")
        
# Main Route
@app.route("/")
def load():
    return render_template("login.html")  

@app.route("/home")
def home():
    return render_template('home.html')

# Route for handling the login page logic
@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'messages' in request.args:
        error = request.args['messages']
    else:
        error = None
    if request.method == 'POST':
        if request.form['username'] != 'testuser1' or request.form['password'] != 'p@ssword1':
            error = 'Invalid Credentials. Please try again.'
        else:
            return redirect(url_for('home'))
    return render_template('login.html', error=error)

@app.route("/logout")
def logout():
        return redirect(url_for("login", messages="You have been logged out"))

if __name__ == "__main__":
    app.logger.debug("APP IS RUNNING")
    app.config["TEMPLATES_AUTO_RELOAD"] = True
    app.run(debug = True)

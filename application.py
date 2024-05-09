from flask import Flask


from home.views import home_app

app = Flask(__name__)
app.register_blueprint(home_app)

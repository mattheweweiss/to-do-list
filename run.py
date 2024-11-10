from routes.auth_routes import auth
from routes.to_do_list_routes import to_do_list

from flask import Flask
from dotenv import load_dotenv
import os


load_dotenv()

port = os.environ.get("PORT")
# Converts to integer
port = int(port)


app = Flask(__name__)
app.secret_key = os.environ.get("SECRET_KEY")
app.register_blueprint(auth)
app.register_blueprint(to_do_list)


app.run(host='0.0.0.0', port=port, debug=True)
from flask import Flask, Blueprint

from main.views import main_blueprint

app = Flask(__name__)

app.register_blueprint(main_blueprint)

if __name__ == '__main__':

    app.run(debug=True)




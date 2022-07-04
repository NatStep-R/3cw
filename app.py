from flask import Flask

from main.views import main_blueprint
from search.views import search_blueprint
from api.views import api_blueprint


app = Flask(__name__)
app.config["JSON_AS_ASCII"] = False


app.register_blueprint(main_blueprint)
app.register_blueprint(search_blueprint)
app.register_blueprint(api_blueprint)


@app.errorhandler(404)
def page_not_found(e):
    return "Такой страницы не существует"


@app.errorhandler(500)
def page_not_found(e):
    return "Ошибка сервера"


if __name__ == '__main__':

    app.run(debug=True)

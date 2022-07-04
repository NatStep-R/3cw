from flask import Blueprint, jsonify
from functions import get_posts_all, get_post_by_pk

api_blueprint = Blueprint('appi_blueprint', __name__, template_folder='templates')


@api_blueprint.route('/api/posts/')
def api_posts():
    posts = get_posts_all()
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:id>')
def api_post():
    post = get_post_by_pk(id)
    return jsonify(post)

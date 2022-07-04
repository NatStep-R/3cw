from flask import Blueprint, jsonify

from logger import create_logger
from utils import get_posts_all, get_post_by_pk


logger = create_logger()


api_blueprint = Blueprint('api_blueprint', __name__, template_folder='templates')


@api_blueprint.route('/api/posts/')
def api_posts():
    posts = get_posts_all()
    logger.info("Страница постов запрошена")
    return jsonify(posts)


@api_blueprint.route('/api/posts/<int:post_id>')
def api_post(post_id):
    post = get_post_by_pk(post_id)
    logger.info(f"Страница поста {post_id} запрошена")
    return jsonify(post)

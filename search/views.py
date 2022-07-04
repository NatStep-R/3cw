from flask import Blueprint, jsonify, render_template
import functions

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')


@search_blueprint.route('/posts/<poster_name>/'):
def get_posts_by_name(poster_name):
    user_posts = functions.get_posts_by_user(poster_name)
    return render_template('user_feed.html', posts=user_posts)
from flask import Blueprint, render_template, request
import utils

search_blueprint = Blueprint('search_blueprint', __name__, template_folder='templates')


@search_blueprint.route('/users/<username>/')
def get_posts_by_name(username):
    user_posts = utils.get_posts_by_user(username)
    return render_template('user-feed.html', posts=user_posts)


@search_blueprint.route('/search/')
def search_post():
    s = request.args['s']
    posts = utils.search_for_posts(s)
    return render_template('search.html', posts=posts)

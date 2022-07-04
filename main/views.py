from flask import Blueprint, render_template
import functions

main_blueprint = Blueprint('main_blueprint', __name__, template_folder='templates')


@main_blueprint.route('/')
def main_page():
    posts = functions.get_posts_all()
    return render_template('index.html', posts=posts)


@main_blueprint.route('/post/<int:id>')
def get_post(id):
    post = functions.get_post_by_pk(id)
    comments_to_post = functions.get_comments_by_post_id(id)
    return render_template('post.html', post=post, comments=comments_to_post)



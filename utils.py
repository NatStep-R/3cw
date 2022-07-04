import json


def load_data(path):
    with open(path, 'r', encoding='utf=8') as f:
        data = json.load(f)
    return data


def get_posts_all():
    """Возвращает все посты"""
    posts = load_data("data/data.json")
    return posts


def get_posts_by_user(user_name):
    """Возвращает посты определенного пользователя"""
    posts = load_data("data/data.json")
    is_in_base = False
    user_posts = []
    for post in posts:
        if user_name.lower() in post["poster_name"].lower():
            is_in_base = True
            user_posts.append(post)
    if is_in_base:
        return user_posts
    else:
        raise ValueError('Такого пользователя не существует')


def search_for_posts(query):
    """Возвращает список постов по ключевому слову"""
    query = query.lower()
    founded_posts = []
    posts = load_data("data/data.json")
    for post in posts:
        if query in post["content"].lower():
            founded_posts.append(post)
    return founded_posts


def get_post_by_pk(pk):
    """Возвращает один пост по его идентификатору"""
    posts = load_data("data/data.json")
    for post in posts:
        if pk == post['pk']:
            return post
    else:
        raise ValueError('Такого поста нет в базе')


def get_comments_by_post_id(post_id):
    comments = load_data("data/comments.json")
    comments_to_post = []
    for comment in comments:
        if comment["post_id"] == post_id:
            comments_to_post.append(comment)
    return comments_to_post

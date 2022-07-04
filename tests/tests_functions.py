from functions import *
import random
import pytest


def test_get_posts():
    data = get_posts_all()
    assert type(data) == list
    assert len(data) != 0


def test_posts_by_user():
    posts = get_posts_all()
    users = []
    for post in posts:
        users.append(post["poster_name"])
    random_name = random.choices(users)
    post = get_posts_by_user(random_name)
    assert type(post) == list
    assert len(post) != 0


def test_posts_by_user_error():
    with pytest.raises(ValueError):
        get_posts_by_user("aaa")


def test_post_by_id():
    posts = get_posts_all()
    random_id = random.choices(range(len(posts) + 1))
    post = get_post_by_pk(random_id)
    assert type(post) == dict
    assert len(post) != 0


def test_post_by_id_error():
    with pytest.raises(ValueError):
        posts = get_posts_all()
        get_post_by_pk(len(posts) + 2)


def test_get_comments():
    posts = get_posts_all()
    random_id = random.choices(range(len(posts) + 1))
    comments = get_comments_by_post_id(random_id)
    assert type(comments) == list


def test_search_posts_by_substring():
    posts = search_for_posts(" ")
    assert type(posts) == list
    assert len(posts) != 0

from app import app
import random
from functions import get_posts_all


class TestAPI:
    def test_api_posts(self):
        resp = app.test_client().get("/api/posts", folow_redirects=True)
        assert resp.status_code == 200
        assert type(resp.data) == list
        assert len(resp.json) != 0
        assert resp.json.keys() == {
            "poster_name",
            "poster_avatar",
            "pic",
            "content",
            "views_count",
            "likes_count",
            "pk"
        }

    def test_api_post(self):
        posts_data = get_posts_all()
        rand_post = random.choice(posts_data)
        resp = app.test_client().get(f"api/post/{rand_post['pk']}")
        assert resp.status_code == 200
        assert type(resp.data) == dict
        assert len(resp.json) != 0
        assert resp.json.keys() == {
            "poster_name",
            "poster_avatar",
            "pic",
            "content",
            "views_count",
            "likes_count",
            "pk"
        }




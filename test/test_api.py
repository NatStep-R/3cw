from app import app


class TestAPI:
    def test_api_posts(self):
        resp = app.test_client().get("/api/posts", follow_redirects=True)
        assert resp.status_code == 200
        assert type(resp.json) == list
        assert len(resp.json) != 0
        assert resp.json[0].keys() == {
            "poster_name",
            "poster_avatar",
            "pic",
            "content",
            "views_count",
            "likes_count",
            "pk"
        }

    def test_api_post(self):
        resp = app.test_client().get(f"/api/posts/1")
        assert resp.status_code == 200
        assert type(resp.json) == dict
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

import pytest
from app import schemas


def test_get_all_posts(authorized_client, test_posts):
    response = authorized_client.get("/posts/")
    def validate(post):
        return schemas.PostOut(**post)
    posts_map = map(validate, response.json())
    # print(list(posts_map))
    assert len(response.json()) == len(test_posts)
    assert response.status_code == 200

def test_unauthorized_user_get_all_posts(client, test_posts):
    response = client.get("/posts/")
    assert response.status_code == 401

def test_unauthorized_user_get_post(client, test_posts):
    response = client.get(f"/posts/{test_posts[0].id}")
    assert response.status_code == 401

def test_user_get_nonexisting_post(authorized_client, test_posts):
    response = authorized_client.get(f"/posts/10")
    assert response.status_code == 404

def test_user_get_post(authorized_client, test_posts):
    response = authorized_client.get(f"/posts/{test_posts[0].id}")
    post = schemas.PostOut(**response.json())
    assert post.Post.id == test_posts[0].id
    assert post.Post.content == test_posts[0].content

@pytest.mark.parametrize("title, content, published", [
    ("this is test title 1", "this is test content 1", True),
    ("this is test title 2", "this is test content 2", True),
    ("this is test title 3", "this is test content 3", False)
])
def test_create_post(authorized_client, test_user, test_posts, title, content, published):
    response = authorized_client.post("/posts/", json={"title": title, "content": content, "published": published})
    new_post = schemas.Post(**response.json())
    assert response.status_code == 201
    assert new_post.user_id == test_user["id"]

def test_create_post_default_published(authorized_client, test_user):
    response = authorized_client.post("/posts/", json={"title": "test_title", "content": "test_content"})
    new_post = schemas.PostCreate(**response.json())
    assert new_post.published == True

def test_unauthorized_create_post(client, test_user):
    response = client.post("/posts/", json={"title":"this is main title", "content": "whatever"})
    assert response.status_code == 401

def test_unauthorized_delete_post(client, test_posts):
    response = client.delete(f"/posts/{test_posts[0].id}")
    assert response.status_code == 401

def test_nonexisting_delete_post(authorized_client, test_posts):
    response = authorized_client.delete(f"/posts/99")
    assert response.status_code == 404

def test_delete_post(authorized_client, test_posts):
    response = authorized_client.delete(f"/posts/1")
    assert response.status_code == 204

def test_forbidden_delete_post(authorized_client, test_posts):
    response = authorized_client.delete(f"/posts/{test_posts[3].id}")
    assert response.status_code == 403

def test_update_post(authorized_client, test_posts):
    response = authorized_client.put(f"/posts/{test_posts[0].id}", json={"title": "updated_title", "content": "updated_content"})
    # print(response.json())
    updated_post = schemas.Post(**response.json())
    assert response.status_code == 205
    assert updated_post.title == test_posts[0].title

def test_forbidden_update_post(authorized_client, test_posts):
    response = authorized_client.put(f"/posts/{test_posts[3].id}", json={"title": "updated_title", "content": "updated_content"})
    assert response.status_code == 403

def test_unauthorized_update_post(client, test_posts):
    response = client.put(f"/posts/{test_posts[3].id}", json={"title": "updated_title", "content": "updated_content"})
    assert response.status_code == 401

def test_nonexisting_update_post(authorized_client, test_posts):
    response = authorized_client.put(f"/posts/99", json={"title": "updated_title", "content": "updated_content"})
    assert response.status_code == 404

from urllib import response
from app import schemas

def test_vote_on_post(authorized_client, test_posts):
    response = authorized_client.post("/vote/", json={"post_id": test_posts[3].id, "dir": 1})
    assert response.status_code == 201

def test_vote_on_post_twice(authorized_client, test_vote, test_posts):
    response = authorized_client.post("/vote/", json={"post_id": test_posts[3].id, "dir": 1})
    assert response.status_code == 409


def test_delete_vote(authorized_client, test_posts, test_vote):
    response = authorized_client.post("/vote/", json={"post_id": test_posts[3].id, "dir": 0})
    assert response.status_code == 201

def test_delete_nonexisting_vote(authorized_client, test_posts):
    response = authorized_client.post("/vote/", json={"post_id": test_posts[3].id, "dir": 0})
    assert response.status_code == 404


def test_unauthorized_vote_on_post(client, test_posts):
    response = client.post("/vote/", json={"post_id": test_posts[3].id, "dir": 1})
    assert response.status_code == 401

def test_vote_on_nonexisting_post(authorized_client, test_posts):
    response = authorized_client.post("/vote/", json={"post_id": 99, "dir": 1})
    assert response.status_code == 404  
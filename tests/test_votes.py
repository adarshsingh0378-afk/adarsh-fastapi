def test_vote_unauthprizes_user(client, test_posts):
    res = client.post(
        "/vote/", json={"post_id": test_posts[3].id, "dir": 1}
    )
    assert res.status_code == 401
    
    
def test_create_user_item(db_session):
    # Create User
    user = UserDB(email="owner@example.com")
    db_session.add(user)
    db_session.commit()

    # Create Item via API
    response = client.post(
        f"/users/{user.id}/items/",
        json={"title": "Test Item"}
    )

    assert response.status_code == 200
    assert response.json()["owner_id"] == user.id

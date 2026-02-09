import pytest

@pytest.mark.parametrize(
    "search_term,expected_count",
    [
        ("apple", 1),
        ("banana", 0),
        (None, 5)  # Returns all seeded items
    ]
)
def test_search_items(search_term, expected_count, db_session):
    # Seed DB with known data...

    # Execute search
    params = {"q": search_term} if search_term else {}
    response = client.get("/items/", params=params)

    assert len(response.json()) == expected_count

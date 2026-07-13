import src.app as app_module


def test_get_activities_returns_all_activities(client):
    # Arrange
    expected_activity_names = set(app_module.activities.keys())

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert set(payload.keys()) == expected_activity_names


def test_get_activities_includes_participants(client):
    # Arrange
    target_activity = "Chess Club"

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert "participants" in payload[target_activity]
    assert isinstance(payload[target_activity]["participants"], list)

import copy

import pytest
from fastapi.testclient import TestClient

import src.app as app_module


@pytest.fixture(autouse=True)
def reset_activities_state():
    """Restore the in-memory activities dictionary after each test."""
    # Arrange
    original_activities = copy.deepcopy(app_module.activities)

    # Act
    yield

    # Assert
    app_module.activities.clear()
    app_module.activities.update(original_activities)


@pytest.fixture
def client():
    return TestClient(app_module.app)

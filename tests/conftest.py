import pytest

import partners


@pytest.fixture
def app():
    """Create and configure a app instance for each test."""
    yield partners.app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()

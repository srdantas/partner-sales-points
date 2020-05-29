import os

import pytest
import testcontainers.compose

import partners
import tests.generators

COMPOSE_PATH = os.path.dirname(os.path.abspath(__name__))


@pytest.yield_fixture(autouse=True, scope='session')
def compose_start():
    """Setup a compose with dependencies for tests."""
    compose = testcontainers.compose.DockerCompose(COMPOSE_PATH)
    compose.start()
    yield compose


@pytest.yield_fixture(autouse=True, scope='session')
def test_suite_cleanup_thing():
    yield


@pytest.yield_fixture
def app():
    """Create and configure a app instance for each test."""
    yield partners.app


@pytest.fixture
def client(app):
    """A test client for the app."""
    return app.test_client()


@pytest.fixture
def valid_partner():
    return {
        "id": tests.generators.id(),
        "tradingName": "PopCorn Station",
        "ownerName": "Dodo Dantas",
        "document": tests.generators.document(),
        "coverageArea": {
            "type": "MultiPolygon",
            "coordinates": [
                [
                    [
                        [
                            0.0,
                            0.0
                        ],
                        [
                            tests.generators.point(),
                            tests.generators.point()
                        ],
                        [
                            tests.generators.point(),
                            tests.generators.point()
                        ],
                        [
                            0.0,
                            0.0
                        ],
                    ]
                ]
            ]
        },
        "address": {
            "type": "Point",
            "coordinates": [
                tests.generators.point(),
                tests.generators.point()
            ]
        }
    }


@pytest.fixture
def invalid_partners():
    return [{
        "tradingName": "PopCorn Station",
        "ownerName": "Dodo Dantas",
        "document": tests.generators.document(),
        "coverageArea": {
            "type": "MultiPolygon",
            "coordinates": [
                [
                    [
                        [
                            0.0,
                            0.0
                        ],
                        [
                            tests.generators.point(),
                            tests.generators.point()
                        ],
                        [
                            tests.generators.point(),
                            tests.generators.point()
                        ],
                        [
                            0.0,
                            0.0
                        ],
                    ]
                ]
            ]
        },
        "address": {
            "type": "Point",
            "coordinates": [
                tests.generators.point(),
                tests.generators.point()
            ]
        }
    },
        {
            "id": tests.generators.id(),
            "tradingName": "PopCorn Station",
            "ownerName": "Dodo Dantas",
            "coverageArea": {
                "type": "MultiPolygon",
                "coordinates": [
                    [
                        [
                            [
                                0.0,
                                0.0
                            ],
                            [
                                tests.generators.point(),
                                tests.generators.point()
                            ],
                            [
                                tests.generators.point(),
                                tests.generators.point()
                            ],
                            [
                                0.0,
                                0.0
                            ],
                        ]
                    ]
                ]
            },
            "address": {
                "type": "Point",
                "coordinates": [
                    tests.generators.point(),
                    tests.generators.point()
                ]
            }
        },
        {
            "id": tests.generators.id(),
            "ownerName": "Dodo Dantas",
            "document": tests.generators.document(),
            "coverageArea": {
                "type": "MultiPolygon",
                "coordinates": [
                    [
                        [
                            [
                                0.0,
                                0.0
                            ],
                            [
                                tests.generators.point(),
                                tests.generators.point()
                            ],
                            [
                                tests.generators.point(),
                                tests.generators.point()
                            ],
                            [
                                0.0,
                                0.0
                            ],
                        ]
                    ]
                ]
            },
            "address": {
                "type": "Point",
                "coordinates": [
                    tests.generators.point(),
                    tests.generators.point()
                ]
            }
        },
        {
            "id": tests.generators.id(),
            "tradingName": "PopCorn Station",
            "document": tests.generators.document(),
            "coverageArea": {
                "type": "MultiPolygon",
                "coordinates": [
                    [
                        [
                            [
                                0.0,
                                0.0
                            ],
                            [
                                tests.generators.point(),
                                tests.generators.point()
                            ],
                            [
                                tests.generators.point(),
                                tests.generators.point()
                            ],
                            [
                                0.0,
                                0.0
                            ],
                        ]
                    ]
                ]
            },
            "address": {
                "type": "Point",
                "coordinates": [
                    0.0, 0.0
                ]
            }
        },
        {
            "id": tests.generators.id(),
            "tradingName": "PopCorn Station",
            "ownerName": "Dodo Dantas",
            "document": tests.generators.document(),
            "address": {
                "type": "Point",
                "coordinates": [
                    0.0, 0.0
                ]
            }
        },
        {
            "id": tests.generators.id(),
            "tradingName": "PopCorn Station",
            "ownerName": "Dodo Dantas",
            "document": tests.generators.document(),
            "coverageArea": {
                "type": "MultiPolygon",
                "coordinates": [
                    [
                        [
                            [
                                0.0,
                                0.0
                            ],
                            [
                                tests.generators.point(),
                                tests.generators.point()
                            ],
                            [
                                tests.generators.point(),
                                tests.generators.point()
                            ],
                            [
                                0.0,
                                0.0
                            ],
                        ]
                    ]
                ]
            }
        },
        {
            "id": tests.generators.id(),
            "tradingName": "PopCorn Station",
            "ownerName": "Dodo Dantas",
            "document": tests.generators.document(),
            "coverageArea": {
                "coordinates": [
                    [
                        [
                            [
                                0.0,
                                0.0
                            ],
                            [
                                tests.generators.point(),
                                tests.generators.point()
                            ],
                            [
                                tests.generators.point(),
                                tests.generators.point()
                            ],
                            [
                                0.0,
                                0.0
                            ],
                        ]
                    ]
                ]
            },
            "address": {
                "type": "Point",
                "coordinates": [
                    tests.generators.point(),
                    tests.generators.point()
                ]
            }
        },
        {
            "id": tests.generators.id(),
            "tradingName": "PopCorn Station",
            "ownerName": "Dodo Dantas",
            "document": tests.generators.document(),
            "coverageArea": {
                "type": "MultiPolygon"
            },
            "address": {
                "type": "Point",
                "coordinates": [
                    tests.generators.point(),
                    tests.generators.point()
                ]
            }
        },
        {
            "id": tests.generators.id(),
            "tradingName": "PopCorn Station",
            "ownerName": "Dodo Dantas",
            "document": tests.generators.document(),
            "coverageArea": {
                "type": "MultiPolygon",
                "coordinates": [
                    [
                        [
                            [
                                0.0,
                                0.0
                            ],
                            [
                                tests.generators.point(),
                                tests.generators.point()
                            ],
                            [
                                tests.generators.point(),
                                tests.generators.point()
                            ],
                            [
                                0.0,
                                0.0
                            ],
                        ]
                    ]
                ]
            },
            "address": {
                "coordinates": [
                    tests.generators.point(),
                    tests.generators.point()
                ]
            }
        },
        {
            "id": tests.generators.id(),
            "tradingName": "PopCorn Station",
            "ownerName": "Dodo Dantas",
            "document": tests.generators.document(),
            "coverageArea": {
                "type": "MultiPolygon",
                "coordinates": [
                    [
                        [
                            [
                                0.0,
                                0.0
                            ],
                            [
                                tests.generators.point(),
                                tests.generators.point()
                            ],
                            [
                                tests.generators.point(),
                                tests.generators.point()
                            ],
                            [
                                0.0,
                                0.0
                            ],
                        ]
                    ]
                ]
            },
            "address": {
                "type": "Point"
            }
        }]

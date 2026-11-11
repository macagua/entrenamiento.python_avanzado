"""Configuration file for pytest."""

import pytest


def pytest_addoption(parser):
    """Add a command line option --cmdopt with default value 'type1' to pytest.

    Args:
        parser (object): The parser object used to add command line options to pytest.
    """    
    parser.addoption(
        "--cmdopt", action="store", default="type1", help="my option: type1 or type2"
    )


@pytest.fixture
def cmdopt(request):
    """Fixture to retrieve the value of the command line option --cmdopt.

    Args:
        request (object): The request object used to retrieve the value of the command line option.

    Returns:
        str: The value of the command line option --cmdopt.
    """
    return request.config.getoption("--cmdopt")

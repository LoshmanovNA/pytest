import pytest
from fixture.application import Application
import json
import os.path

fixture = None
config = None


@pytest.fixture()
def app(request):
    global fixture
    global config
    browser = request.config.getoption("--browser")
    if config is None:
        config_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), request.config.getoption("--config"))
        with open(config_file) as file:
            config = json.load(file)
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser)
    fixture.session.ensure_login(username=config["username"], password=config["password"])
    return fixture


@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()

    request.addfinalizer(fin)
    return fixture


def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome")
    parser.addoption("--config", action="store", default="config.json")

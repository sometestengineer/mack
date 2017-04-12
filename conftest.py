import pytest
from fixture.application import Application


fixture = None


@pytest.fixture
def app(request):
    global fixture
    browser = request.config.getoption('--browser')
    if fixture is None or not fixture.is_valid():
        fixture = Application(browser=browser)
    return fixture


# (scope='session') - one fixture for all tests in session,
@pytest.fixture(scope='session', autouse=True)  # without autouse browser won't close
def stop(request):
    def fin():
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture


# py.test --browser=chrome test_... to run test in different browser from CLI
# or Edit Configurations > Options > --browser=chrome in PyCharm
def pytest_addoption(parser):  # pytest method to hook options
    parser.addoption('--browser', action='store', default='firefox')




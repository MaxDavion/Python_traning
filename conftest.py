from fixture.application import Application
import pytest

fixture = None

@pytest.fixture
def app(request):
    if fixture is None:
        global fixture
        fixture = Application()
        fixture.session.login(user="admin", password="secret")
    else:
        if not fixture.is_valid():
            fixture = Application()
            fixture.session.login(user="admin", password="secret")
    return fixture

@pytest.fixture(scope = 'session', autouse = True)
def stop(request):
    def fin():
        fixture.session.logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture

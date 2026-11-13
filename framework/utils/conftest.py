import pytest

@pytest.fixture
def user_credentials(request):
    return request.param
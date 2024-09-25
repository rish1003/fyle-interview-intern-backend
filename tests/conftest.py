import pytest
import json
from core.models.principals import Principal
from core.models.users import User
from tests import app
from core import db

@pytest.fixture
def client():
    return app.test_client()


@pytest.fixture
def h_student_1():
    headers = {
        'X-Principal': json.dumps({
            'student_id': 1,
            'user_id': 1
        })
    }

    return headers


@pytest.fixture
def h_student_2():
    headers = {
        'X-Principal': json.dumps({
            'student_id': 2,
            'user_id': 2
        })
    }

    return headers


@pytest.fixture
def h_teacher_1():
    headers = {
        'X-Principal': json.dumps({
            'teacher_id': 1,
            'user_id': 3
        })
    }

    return headers


@pytest.fixture
def h_teacher_2():
    headers = {
        'X-Principal': json.dumps({
            'teacher_id': 2,
            'user_id': 4
        })
    }

    return headers


@pytest.fixture
def h_principal():
    headers = {
        'X-Principal': json.dumps({
            'principal_id': 1,
            'user_id': 5
        })
    }

    return headers

@pytest.fixture
def new_user():
    """Create a sample user once for testing and return its ID."""
    user = User(username='testuser', email='test@example.com')
    db.session.add(user)
    db.session.commit()
    yield user.id 
    db.session.delete(user)
    db.session.commit()

@pytest.fixture()
def new_principal():
    principal = Principal(user_id=1)
    db.session.add(principal)
    db.session.commit()
    yield principal
    db.session.delete(principal)
    db.session.commit()
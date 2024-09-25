import pytest

from core.libs.exceptions import FyleError
from core.models.users import User


def test_fyle_error_to_dict():
    """Test the to_dict method of FyleError."""
    message = "This is a custom error message."
    status_code = 500
    error = FyleError(status_code, message)
    error_dict = error.to_dict()
    
    # Assertions
    assert isinstance(error_dict, dict)  # Should return a dictionary
    assert 'message' in error_dict  # Should have 'message' key
    assert error_dict['message'] == message  # Should have the correct message
    
def test_user_model_methods(new_user):
    """Test User model methods: __repr__, filter, get_by_id, get_by_email."""
    
    # Use the existing user's ID to test methods
    user = User.get_by_id(new_user)
    assert user is not None
    assert repr(user) == '<User \'testuser\'>'


    # Test get_by_id method
    found_user_by_id = User.get_by_id(new_user)
    assert found_user_by_id is not None
    assert found_user_by_id.username == 'testuser'

    # Test get_by_email method
    found_user_by_email = User.get_by_email('test@example.com')
    assert found_user_by_email is not None
    assert found_user_by_email.username == 'testuser'

    # Test get_by_id with a non-existent ID
    found_user_nonexistent_id = User.get_by_id(999)  # Assuming 999 does not exist
    assert found_user_nonexistent_id is None

    # Test get_by_email with a non-existent email
    found_user_nonexistent_email = User.get_by_email('nonexistent@example.com')
    assert found_user_nonexistent_email is None
    
def test_principal_creation(new_principal):
    """Test that a Principal instance is created correctly."""
    assert new_principal.id is not None
    assert new_principal.user_id is not None


def test_principal_repr(new_principal):
    """Test the __repr__ method of the Principal model."""
    assert repr(new_principal) == f'<Principal {new_principal.id!r}>'
import pytest
from bson import ObjectId
from greens.schemas.vegs import DocumentResponse


# Since ObjectIdField is not a standard Pydantic field, we'll assume it's a custom field
# that should accept BSON ObjectId instances. We'll need to mock or construct valid and
# invalid ObjectId instances for testing.

# Helper function to create a valid ObjectId instance
def create_valid_objectid():
    return ObjectId()


# Helper function to create an invalid ObjectId instance
def create_invalid_objectid():
    return "invalid_objectid"


# Happy path tests with various realistic test values
@pytest.mark.parametrize(
    "test_id, object_id",
    [
        ("HP-1", create_valid_objectid()),
        # Add more test cases with different valid ObjectIds if necessary
    ],
)
def test_document_response_with_valid_id(test_id, object_id):
    # Act
    document_response = DocumentResponse(id=object_id)

    # Assert
    assert document_response.id == str(object_id), f"Test case {test_id} failed: The id field did not match the input ObjectId."


# Edge cases
# Assuming edge cases would be related to the boundaries of ObjectId creation and representation
# Since ObjectId is a specific BSON type, edge cases might not be as relevant here,
# but we can still test for unusual but valid ObjectIds

# Error cases
@pytest.mark.parametrize(
    "test_id, object_id, expected_exception",
    [
        ("EC-1", create_invalid_objectid(), ValueError),  # Invalid ObjectId format
        ("EC-2", None, ValueError),  # None as an ObjectId
        ("EC-3", 12345, ValueError),  # Integer as an ObjectId
        # Add more test cases with different invalid ObjectIds if necessary
    ],
)
def test_document_response_with_invalid_id(test_id, object_id, expected_exception):
    # Act and Assert
    with pytest.raises(expected_exception) as exc_info:
        DocumentResponse(id=object_id)

    assert str(exc_info.value), f"Test case {test_id} failed: Expected exception {expected_exception} was not raised."

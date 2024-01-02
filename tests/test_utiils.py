import pytest
from plotish.interfaces.utils import check_in_dict

def test_check_in_dict_existing_key():
    # Test when the key exists in the dictionary
    input_dict = {"name": "John", "age": 25, "city": "New York"}
    key = "age"
    default_value = 0
    result = check_in_dict(input_dict, key, default_value)
    assert result == input_dict[key]

def test_check_in_dict_nonexistent_key():
    # Test when the key does not exist in the dictionary
    input_dict = {"name": "John", "city": "New York"}
    key = "age"
    default_value = 0
    result = check_in_dict(input_dict, key, default_value)
    assert result == default_value

def test_check_in_dict_with_default():
    # Test when the key exists in the dictionary and a default value is provided
    input_dict = {"name": "John", "age": 25, "city": "New York"}
    key = "age"
    default_value = 0
    result = check_in_dict(input_dict, key, default_value)
    assert result == input_dict[key]

def test_check_in_dict_with_default_nonexistent_key():
    # Test when the key does not exist in the dictionary and a default value is provided
    input_dict = {"name": "John", "city": "New York"}
    key = "age"
    default_value = 0
    result = check_in_dict(input_dict, key, default_value)
    assert result == default_value

# Add more tests as needed

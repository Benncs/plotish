"""utils: helper function for package"""


def check_in_dict(dic: dict, name: str, default: any) -> any:
    """
    Retrieve the value associated with the given name in the dictionary.
    If the name is not present, return the default value.

    Parameters:
    - dic (dict): The dictionary to check for the name.
    - name (str): The name to look for in the dictionary.
    - default (any): The default value to return if the name is not present.

    Returns:
    any: The value associated with the name in the dictionary or the default value.

    Example:
    ```python
    sample_dict = {'key1': 'value1', 'key2': 'value2'}
    result = check_in_dict(sample_dict, 'key1', 'default_value')
    print(result)  # Output: 'value1'
    ```
    """
    if name in dic:
        val = dic[name]
    else:
        val = default
    return val

def get_value_from_dict(dict, key):
  """
  Get the value associated with a given key in a dictionary.

  Args:
    dict: The dictionary to search.
    key: The key to search for.

  Returns:
    The value associated with the key, or None if the key does not exist.
  """

  try:
    return dict[key]
  except KeyError:
    return None
dict = {'name': 'John Doe', 'age': 30}

# Get the value associated with the 'name' key.
name = get_value_from_dict(dict, 'name')

# Get the value associated with the 'age' key.
age = get_value_from_dict(dict, 'age')

print(name)  # Prints 'John Doe'
print(age)  # Prints 30

# Get the value associated with the 'address' key.
address = get_value_from_dict(dict, 'address')

# Since the 'address' key does not exist in the dictionary, None is returned.
print(address)  # Prints None

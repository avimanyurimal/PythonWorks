def insert_string(list, string):
  """
  This function inserts a given string at the beginning of all items in a list.

  Args:
    list: A list of items.
    string: The string to insert at the beginning of each item.

  Returns:
    A new list with the string inserted at the beginning of each item.
  """

  new_list = []
  for item in list:
    new_list.append(string + str(item))

  return new_list


# Sample list: [1,2,3,4], string: emp
# Expected output: ['emp1', 'emp2', 'emp3', 'emp4']

list = [1, 2, 3, 4]
string = "emp"

new_list = insert_string(list, string)

print(new_list)

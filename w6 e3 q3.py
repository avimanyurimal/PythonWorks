def filter_adults(people_list):
    return [person for person in people_list if person['age'] > 18]
people = [
    {'name': 'Alice', 'age': 25},
    {'name': 'Bob', 'age': 17},
    {'name': 'Charlie', 'age': 30},
    {'name': 'Dave', 'age': 16}
]
adults = filter_adults(people)
print(adults)

def sort_by_age(people):
    return sorted(people, key=lambda x: x['age'], reverse=True)

def filter_by_age(people, threshold):
    return [person for person in people if person['age'] <= threshold]

# Example usage:
people = [
    {'name': 'Alice', 'age': 30},
    {'name': 'Bob', 'age': 25},
    {'name': 'Charlie', 'age': 35}
]

sorted_people = sort_by_age(people)
print("Sorted by Age:", sorted_people)

filtered_people = filter_by_age(people, 30)
print("Filtered by Age:", filtered_people)

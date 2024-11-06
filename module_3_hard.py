def calculate_structure_sum(elements):
    if isinstance(elements, int):
        return elements
    elif isinstance(elements, str):
        return len(elements)
    elif isinstance(elements, dict):
        return sum(calculate_structure_sum(key) + calculate_structure_sum(value) for key, value in elements.items())
    elif isinstance(elements, (list, tuple, set)):
        return sum(calculate_structure_sum(number) for number in elements)
    else:
        return 0

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
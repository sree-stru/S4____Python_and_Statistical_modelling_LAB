user_input = input("Enter the numbers separated by commas: ").split(',')
tuple_elements = list(map(int, user_input))

odd_tuple = []
even_tuple = []

for x in tuple_elements:
    if x % 2 == 0:
        even_tuple.append(x)
    else:
        odd_tuple.append(x)

print(f"Tuple of odd elements: {tuple(odd_tuple)}")
print(f"Tuple of even elements: {tuple(even_tuple)}")

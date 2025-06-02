# 1.List Manipulation:

# Create a list of Kannada foods. Use list comprehension to create a new list where each food name is in uppercase.

from numpy import matrix


kannada_foods = ['bisi bele bath', 'masala dosa', 'idli', 'vada', 'poori']
uppercase_foods = [foods.upper() for foods in kannada_foods]
print(uppercase_foods)

#2. Sum of Prices:

# Create a dictionary of 5 items with their prices. Write a program that calculates the total price of all items using a for loop.

item_prices = {
    'apple': 30,
    'banana': 20,
    'orange': 25,
    'grapes': 50,
    'mango': 60
}

total = 0
for price in item_prices.values():
    total += price
print("Total price of all items:", total)


#3. List of Squares:

# Create a list of numbers from 1 to 10. Use list comprehension to generate a list of their squares.
numbers = list(range(1, 11))
squares = [num ** 2 for num in numbers]
print("List of squares:", squares)

#4. Student Data Task:

# Create a list of 3 dictionaries, where each dictionary contains the name, age, and marks of a student. Loop through the list and print each student's information.

cars = [
    {'name': 'porcsh 911', 'price': 'Rs 96.05 L', 'manufacture': 'German'},
    {'name': 'Defender', 'price': 'Rs 1.52 Cr', 'manufacture': 'Slovakia'},
    {'name': 'BMW', 'price': 'Rs 44.40 L', 'manufacture': 'India'}
]
for car in cars:
    print(f"Name: {car['name']}, price: {car['price']}, manufacture: {car['manufacture']}")



#5. Dictionary Comprehension:

# Create a dictionary where the keys are Kannada cities, and the values are their populations. Use dictionary comprehension to filter out cities with populations below 10 lakhs.

kannada_cities_population = {
    'Bengaluru': 12000000,
    'Mysuru': 1000000,
    'Mangaluru': 600000,
    'Hubballi': 800000,
    'Kalaburagi': 500000
}

filtered_cities = {city: population for city, population in kannada_cities_population.items() if population < 1000000}
print("Filtered cities with population below 10 lakhs:", filtered_cities)

# 6.Nested List Challenge: Write a Python program that takes a list of lists (a 2D list) as input and:

# Prints the entire matrix row by row.
# Prints the sum of each row in the matrix.

def process_matrix(matrix):
    print("Matrix contents (row by row):")
    print("-" * 30)
    for i, row in enumerate(matrix):
        print(f"Row {i + 1}: {row}")
    print("\nRow Sums:")
    print("-" * 15)
    for i, row in enumerate(matrix):
        print(f"Sum of Row {i + 1}: {sum(row)}")

# Example usage:
sample_matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
process_matrix(sample_matrix)
  
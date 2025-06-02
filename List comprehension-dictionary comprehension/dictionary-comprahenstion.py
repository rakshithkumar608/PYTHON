numbers = [1,2,3,4,5,6]
squared_numbers = {num: num ** 2 for num in numbers}
print(squared_numbers)

names = ["Anand", "Geetha", "Kumar"]
name_length = {name: len(name) for name in names}
print(name_length)


city_population = {
    "Bengaluru": 84,
    "Mysuru": 11,
    "Hubballi": 9,
    "Mangaluru": 5
}

large_cities = {city: population for city, population in city_population.items() if population > 10}
print(large_cities)
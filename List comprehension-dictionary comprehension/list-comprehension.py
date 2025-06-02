n = [1,2,3,4,5,6]
s = [num ** 2 for num in n]
print(s)

n = [1,2,3,4,5,6]
even_num = [num for num in n if num % 2 == 0]
print(even_num)

cities = ["Bengaluru", "Mysuru", "Hubballi", "Mangaluru"]
city_length = [city.upper() for city in cities]
print(city_length)


l = [X for X in range(1,11)]
print(l)
edl = [x**2 for x in l if x%2 == 0]
print(edl)
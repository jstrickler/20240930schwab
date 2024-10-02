cities = []  # empty list
# or
cities = list()  # empty lislt

cities = ['Portland', 'Pittsburgh', 'Peoria']
print(f"cities: {cities}\n")

cities.append('Miami')
cities.append('Montgomery')
print(f"cities: {cities}\n")

cities.insert(0, 'Boston')
cities.insert(5, "Buffalo")
print(f"cities: {cities}\n")

more_cities = ["Detroit", "Des Moines"]
cities.extend(more_cities)
print(f"cities: {cities}\n")

# LIST.append(obj)  LIST.insert(pos, obj)  LIST.extend(iterable)

# LIST.extend(X)
# for obj in X:
#    LIST.append(obj)

del cities[3]
print(f"cities: {cities}\n")

cities.remove('Buffalo')
print(f"cities: {cities}\n")

city = cities.pop()  # pops last element
print(f"city: {city}")
print(f"cities: {cities}\n")

city = cities.pop(3)  # pops specified element
print(f"city: {city}")
print(f"cities: {cities}\n")

for city in reversed(cities):
    print(city)

# declare lists

numbers = []
a = [2,7,10,8]
cities = ['mumbai', 'pune', 'bangalore','delhi', 'agra', 'indore']
b= [10,3, 'apple',6,'strawberry']
c= range(1,10,2)

#print the results
print(a)
for city in cities:
    print(city)
print(b)
print(c)

# get length of lists
print(len(a))
print(len(cities))

# add item into list
numbers.append(19)
numbers.append(1)

for i in numbers:
    print(i)

# get specific item
print(cities[0])

# sorting
print(a.sort())

# edit item
print('----edit item')
cities[2] = 'new city'
for city in cities:
    print(city)

# remove item
print('----remove item')
a.remove(8)    # by value
del cities[2]  # by index
for city in cities:
    print(city)
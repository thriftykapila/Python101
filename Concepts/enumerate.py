# Python provide the built-in function enumerate() for keeping the count while doing iterations.
# Let's see its syntax:
#
# enumerate(iterable, start = 0)
# Parameters:
# - iterable: any object that supports iteration.
# - start: the index value from which the counter is to be started, by default it's 0 .

items = ['bread', 'milk', 'butter']

grocery = []
for count, item in enumerate(items):
    grocery.append(item[::-1])
    print(item)

print(items)
print(grocery)

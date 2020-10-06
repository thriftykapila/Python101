grocery = ['bread', 'milk', 'butter']
grocery1 = []
for count, item in enumerate(grocery):
  grocery1.append(item[::-1])
  print(item)
print(grocery)
print(grocery1)
fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

# for VAR in ITERABLE:
#     ...use VAR ...

for fruit in fruits:
    if fruit.startswith('p'):
        continue
    if len(fruit) > 8:
        continue
    print(fruit)
print()



fruits = ['pomegranate', 'cherry', 'apricot', 'apple',
'lemon', 'kiwi', 'orange', 'lime', 'watermelon', 'guava',
'papaya', 'fig', 'pear', 'banana', 'tamarind', 'persimmon',
'elderberry', 'peach', 'blueberry', 'lychee', 'grape', 'date' ]

print(f"{'peach' in fruits = }")
print(f"{'blackberry' in 'fruits' = }")


fruits[5] = "strawberry"

print(f"{fruits = }\n")

print(f"{fruits[0] = }")
print(f"{fruits[4] = }")
print(f"{fruits[len(fruits)-1] = }")
print(f"{fruits[-1] = }")
# print(f"{fruits[33] = }")   out of range

# start-at:stop-before:increment-by
#   0:len(X):1
print(f"{fruits[0:3:1] = }")
print(f"{fruits[:3] = }")
print(f"{fruits[3:7] = }")
start = 5
print(f"{fruits[start:start + 8] = }")
print(f"{fruits[::2] = }")
print(f"{fruits[10:] = }")
print(f"{fruits[-5:] = }")

print(f"{fruits[-1:-11:-1] = }")
print('-' * 60)

b = "banana split"
print(f"{b[:3] = }")
print(f"{b[::2] = }")
print(f"{b[-5:] = }")
print()

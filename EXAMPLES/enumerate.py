
colors = "red blue green yellow brown black".split()

months = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()

colors_enum = enumerate(colors)
print(f"{colors_enum = }")

for i, color in colors_enum:  # enumerate() returns iterable of (index, value) tuples
    print(i, color)

print()

for num, month in enumerate(months, 100):  # Second parameter to enumerate is added to index
    print(f"{num} {month}")

from pprint import pprint

COLOR = "blue"

def spam(count):
    print(COLOR * count)

spam(5)

g = globals()
pprint(g)
print()

x = g['spam']
print(f"{x = }")
print(f"{type(x) = }")
x(3)
print()

print(f"{COLOR = }")
print(f"{g['COLOR'] = }")

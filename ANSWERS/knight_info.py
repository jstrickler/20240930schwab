import sys
from knight import Knight

for name in sys.argv[1:]:
    k = Knight(name)
    print(f"Name: {k.title} {k.name}")
    # print("Name:", k.title, k.name)
    # print("Name: {} {}".format(k.title, k.name))
    # print("Name: %s %s" % (k.title, k.name))
    # print("Name: " + k.title + " " + k.name)
    print("Favorite Color:", k.favorite_color)
    print()

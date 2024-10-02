import typing as T

# Numeric = T.Union[int, float]

Numeric = int | float



def square_root(n: Numeric) -> float:
    return n ** .5

for i in 100, 10, 1, 625:
    print(i, square_root(i))

x: int

x = square_root(1000)
print(f"{x = }")


x = 5
x = "abc"

print(f"{square_root(5.9) = }")

print(__annotations__)

print(f"{square_root.__annotations__ = }")

def spam(data: T.Iterable):
    for element in data:
        print(element)

spam(["a", "b", "c"])
spam(("a", "b", "c"))
spam("abc")
spam(range(5))

def toast(thing: T.Any) -> str:
    return "Well, aren't you strict?"

toast(5)
toast("abc")
toast(['a', 1, (1, 2), [3, 4]])

def foo() -> list[str]:
    return ["a", "b"]

# list[int|float]
# tuple[str,str,int,float,str]
# T.Tuple[str,str,int,float,str]

# dict[str,list[int]]

def eggs(m: str | None):
    pass


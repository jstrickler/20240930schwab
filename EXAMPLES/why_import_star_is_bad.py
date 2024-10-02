from navigation import *  # import current _implicitly_ from navigation
from electrical import current, voltage, amps  # import current _explicitly_ from electrical

print(current())  # calls navigation.current(), not electrical.current()
print(voltage())
print(amps())

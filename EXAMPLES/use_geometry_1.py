import sys
import alpha.mathlib.geometry as geometry # find and load geometry.py

a1 = geometry.circle_area(8)
a2 = geometry.rectangle_area(10, 12)
a3 = geometry.square_area(7.9)
print(a1, a2, a3)

# 1. current folder
# 2. folders in PYTHONPATH     folder1;folder2;folder3 (win) or dir1:dir2:dir3 (non-win)
# 3. installation folder + "/lib"   (sys.prefix + "/lib")

print(f"{sys.prefix = }")
print(f"{sys.executable = }")
print()
for path in sys.path:
    print(path)



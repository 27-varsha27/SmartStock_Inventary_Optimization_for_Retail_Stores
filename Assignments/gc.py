import gc
import sys

print("========== REFERENCE COUNTING ==========")

a = [1, 2, 3]
print("Ref count of a:", sys.getrefcount(a))

b = a
print("Ref count after b = a:", sys.getrefcount(a))

del b
print("Ref count after deleting b:", sys.getrefcount(a))

del a
print("a deleted\n")

print("========== CYCLIC GARBAGE COLLECTION ==========")

class Demo:
    def __init__(self, name):
        self.name = name
        self.ref = None

    def __del__(self):
        print(f"{self.name} collected")

x = Demo("X")
y = Demo("Y")

x.ref = y
y.ref = x

del x
del y

print("Before gc.collect()")
unreachable = gc.collect()
print("Unreachable objects collected:", unreachable)

print("\n========== GENERATIONAL GC ==========")

print("GC thresholds:", gc.get_threshold())
print("GC count before object creation:", gc.get_count())

lst = []
for i in range(5000):
    lst.append(i)

print("GC count after object creation:", gc.get_count())

del lst
print("After deleting objects")
print("Unreachable objects collected:", gc.collect())

print("\n========== GC MODULE CONTROLS ==========")

print("GC enabled?", gc.isenabled())

gc.disable()
print("GC enabled after disable?", gc.isenabled())

gc.enable()
print("GC enabled after enable?", gc.isenabled())

print("Manual GC run:", gc.collect())

print("\n========== END ==========")

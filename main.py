# 1-m
i = lambda x: x if x > 0 else 0
print(i(-5))


# 2-m
i = lambda x: x % 2 == 0
print(i(4))


# 3-m
f = lambda a, b: a if a > b else b
print(f(7, 3))


# 4-m
a = lambda x: "Musbat" if x > 0 else "Manfiy"
print(a(-2))


# 5-m
f = lambda x: x * 2 if x > 10 else x
print(f(8))


# 6
a = lambda x: x / 2 if x % 2 == 0 else x * 3
print(a(6))


# 7
f = lambda a, b: a if a < b else b
print(f(7, 3))


# 8
f = lambda x: "OK" if x % 5 == 0 else "NO"
print(f(10))


# 9
f = lambda x: 100 if x > 100 else x
print(f(150))


# 10
f = lambda x: -x if x < 0 else x
print(f(-9))


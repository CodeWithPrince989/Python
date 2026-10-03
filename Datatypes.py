# Numeric
a = 100 #Integer
print(type(a))
print(id(a))

a = 3.4 #Float
print(id(a))
print(type(a))

a = 3 + 4j  #Complex
print(type(a))
print(id(a))
print(a.real, a.imag)

# String => Ordered, Immutable, slcing
s1 = "World"
print(id(s1))
print(type(s1))
print(s1[:5])

# list
l1 = [1, 5, "Hello", 3.14]
print(l1[2])
print(l1[0])
l1[2] = "Hello World"
print(l1[2])
a = range(0, 10)
print(a)

#Tuple
t1 = (1, 3, "Prince", 3)
print(type(t1))
print(t1[1:3])

# Set 
s1 = {1, 1, 2, 3, 4, 2}
print(s1)

# Frozen Set 
f1 = frozenset({1, 3, 4, 1, 3, 4})
print(f1)

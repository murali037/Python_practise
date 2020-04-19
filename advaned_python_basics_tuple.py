#%%

tup = ("Max",27,"Boston")

print(tup)

print(type(tup))

tup = "max",23,45,1,"ff"

print(tup)

print(type(tup))

tup = "max",

print(tup)

print(type(tup))

#%% list vs tuple

a = [1,2,3,4,5]

b = 1,2,3,4,5

print(type(a))

print(type(b))

print(b.count(1))

print(a.count(1))

#%%

tup = "max","vicks","We"

a,b,c = tup

print(a)
print(b)
print(c)

#%%

tup = 0,1,2,3,4,5

a, *b, c = tup

print(a)
print(b)
print(c)

#%%

int_a = 1

char = "s"

my_list = [1,2,3]
tup = 1,2,3

print(sys.getsizeof(int_a),"bytes")
print(sys.getsizeof(char),"bytes")
print(sys.getsizeof(my_list),"bytes")
print(sys.getsizeof(tup),"bytes")

#%%

import timeit
print(timeit.timeit(stmt="[1,1,2,3,4,5]", number = 100000000))
print(timeit.timeit(stmt="(1,1,2,3,4,5)", number = 100000000))



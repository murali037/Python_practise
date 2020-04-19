#%% unordered, mutable, no duplicates

set = {1,2,3,3,3,3,2,3,3,"m"}

print(set)

print(type(set))

#%% how many unique characters are in a word

my_set = set("HellovhcfgxdfydtdtyudsHHHyrt")
print(my_set)

#%%

myset = set()

myset.add(1)
myset.add(2)
myset.add(3)
myset.add(1)

print(myset)

myset.remove(3)

print(myset)

myset.pop()

print(myset)


myset.discard(4)
print(myset)

myset.clear()
print(myset)


#%%

for i in myset:
    print(i)

x = set()

y = ()

print(type(x))

print(type(y))

#%% union

evens ={2,4,6,8}

odds = {1,3,5,7,9}

primes = {2,3,5,7}

u = evens.union(primes)

print(u)

i = odds.intersection(primes)

print(i)


#%%

A = {1,2,3,4,5,6,7,8}
B= {1,2,3,11,22,33}
diff = A.difference(B)

print(diff)

sym_diff = A.symmetric_difference(B)

print(sym_diff)


A.update(B)     ## update

print(A)

#%% frozen set

a = frozenset([1,2,3,4])

print(a)

for i in a:
    print(i)








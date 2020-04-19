

#%% Lists

a = [11,212,33,4,5,6,66,7]

print(a)

a.sort()
a.pop()
a.remove(33)


print(a)

#%%

a = [1,2,3,4,5,6,7,8,9]

print(a[::1])

print(a[::-1])

print(a[::2])

print(a[::][::-1][2])

#%% copying lists

a = ["cat","dog","mouse"]

print(a)

b=a
c = a.copy()
a.append('rat')

print("a",a)

print("b",b)

print("c",c)


#%%

my_list = [1,2,3,4,5]

b = [i*i for i in my_list]

print(my_list)

print(b)
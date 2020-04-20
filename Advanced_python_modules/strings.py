#%%

str1 = 'hello'

str2 = "world"

print(str1, str2)

#%% multi line strings

str1 = """ ads
sd
ds
dfffff
"""
print(str1)

for i in str1:
    print(i)

#%%

str1 = "hello"


print(str1[::-1])

str2 = "world"

str3 = str1 + " " +str2

print(str3)

if "ell" in str1:   # substring
    print("yes")



#%% remove whitespaces

str1 = "       heallp    world    "

print(str1)

str2 = str1.strip()

print(str2)


#%%

str1 = "".join(str2)
print(str1)


#%%


var = "Cruises"

my_str = "the variable is %s" %var

print(my_str)


#%%

var = 6.9

my_str = "the variable is %.1f" %var

print(my_str)

my_str = "the variable is {:.2f} and {}" .format(var,var)

print(my_str)

my_str = f"the variable is {var} and {var}"

print(my_str)


















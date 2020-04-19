#%%

h = {"name": "Max", "age":28, "city": "New York"}

print(h)

print(h["name"])

del h["age"]

print(h)

h["new"] = "osbject"
print(h)

h.pop("new")

print(h)

h[1]=334
h[2]=9293

print(h)

h.popitem()

print(h)

#%%

h = {"name": "Max", "age":28, "city": "New York"}

if "name" in h.values():
    print(h["name"])
else:
    print(h.keys())

#%%
h = {"name": "Max", "age":28, "city": "New York"}
print(h)

try:
    print(h["last_name"])
except:
    print("error")


#%%

for key in h.values():
    print(key)

for i,j in h.items():
    print(i,j)

#%% for copying

h = {"name": "Max", "age":28, "city": "New York"}

d = h.copy()
d[1] = 3

print(h)

print(d)


#%%

h.update(d)

print(h)

print(d)


#%%

tup = 1,

h[tup] = "baby"

print(h)





















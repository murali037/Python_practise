#%%

from collections import Counter

a ="aaabbbbbbbccccc"

cnt = Counter(a)

print(cnt)
print(cnt.most_common(2)[0][0])

print(list(cnt.elements()))


#%%
from collections import namedtuple

point = namedtuple('point','x,y')

pt = point(1,-4)

print(pt)

#%%

from collections import defaultdict

d = defaultdict()

print(d)

#%%

from collections import deque

q = deque()
q.append(13)
q.append(2)
q.append(1)
q.append(1)
q.append(1)

print(q)

q.pop()

print(q)

q.popleft()

print(q)

q.appendleft(45)

print(q)

q.extend([1,2,34242,12])

print(q)

q.rotate(1)

print(q)



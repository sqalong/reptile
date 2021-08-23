from collections import Counter

# a = ['apple', 'banana', 'apple', 'tomato', 'orange', 'apple', 'banana', 'watermeton']
# d = Counter(a)
# print(d)
alist = [{"name": "a", "age": 20}, {"name": "b", "age": 30}, {"name": "c", "age": 25}]
alist.sort(key=lambda x: x['age'])
print(alist)

l = []
for i8 in range(3):
    x = int(input('integer:\n'))
    l.append(x)
l.sort()
print(l)
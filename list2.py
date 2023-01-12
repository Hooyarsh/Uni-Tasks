l  = []

g = int(input())

list_length = g

for i in range(list_length):
    z = int(input())
    l.append(z)
print ("before sort", (l))
for i in range(len(l)):
    for j in range(i + 1, len(l)):

        if l[i] > l[j]:
           l[i], l[j] = l[j], l[i]
print ("after sort", (l))

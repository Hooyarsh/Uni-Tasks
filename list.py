y = int(input())
a = [1, 2, 3, 4, "Hooyar"]
print (a[y])
print (*a, sep = "\n")
for x in range(len(a)):
    print (a[x])
a.append ("Shahidi")
print (a)
x = int(input())
a.remove(x)
print (a)
f = int(input())
a.pop(f)
print (a)
#------------------------------------
list = []

g = int(input())

list_length = g

for i in range(list_length):
    z = input()
    list.append(z)

print (list)


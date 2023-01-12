a = [1,2,3,4,5,6,7,8,9]
#g = input()
#x = int(input())
#a.insert(x, g)
print (a)
d = int(input("start of interval: "))
u = int(input("end of interval: "))
for i in range(d,u):
    j = input()
    a.insert(i, j)
for y in range(d,u):
    a.pop()
print (a)

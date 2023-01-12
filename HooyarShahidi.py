mylist = ["a","b","c","d","e"]
print (mylist)
newlist = []
d = int(input("start of interval: "))
u = int(input("end of interval: "))
for i in range(d,u):
    newlist.append(mylist[i])
del(mylist[d:u])
print (mylist)
print (newlist)

list = []
a = int(input("start: "))
b = int(input("end: "))
for j in range (a,b+1):
    list.append(j)
even = []
odd = []
for i in list:
    if(i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)

print("Even List: ",even)
print("Odd List: ",odd)

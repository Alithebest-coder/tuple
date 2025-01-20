tup1=(4,3,2,2,-1,18)
tup2=(2,4,8,8,3,2,9)
list1=[]
for i in range(len(tup1)):
    x=tup1[i]*tup2[i]
    list1.append(x)
print(list1)
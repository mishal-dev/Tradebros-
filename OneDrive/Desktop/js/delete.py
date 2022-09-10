l=[i for i in range(1,101)]
val=len(l)
c=[]
start=0
for i in range(start,val,2):
    c.append(l[i])
l=c
c=[]
for i in range(start,len(l),2):
    c.append(l[i])
l=c
c=[]
for i in range(start,len(l),2):
    c.append(l[i])
print(c)
l=c
c=[]
for i in range(1,len(l),2):
    c.append(l[i])
print(c)
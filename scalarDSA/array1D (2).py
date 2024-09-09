def query(pos,val):
    a[pos]=val
    return a

a=[0,0,0,0,0,0,0]
a=query(1,3)
a=query(4,2)
a=query(3,1)
for i in range(1,len(a)):
    a[i]+=a[i-1]
print(a)


# def query(a,start,end,val):
#     while(start<=end):
#         a[start]=val
#         return a

# a=[0,0,0,0,0,0,0]
# n=len(a)
# a=query(a,5,3,1)
# a=query(a,4,2,1)
# a=query(a,3,1,1)
# for i in range(1,n):
#     a[i]+=a[i-1]
# print(a)

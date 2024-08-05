# menu='''1.linear search
#         2.binary search
#         3.sentinel search'''
# print
# linear search
c=0
def linearsearch(key,a):
    global c
    for i in range(len(a)):
        c+=1
        if a[i]==key:
            return i
    return -1
a=[]
key=int(input("element to be found"))
# # n=int(input("no of elements of array"))
# # for i in range(n):
# #     a.append(int(input("Enter the elements of array")))
# # print("the given list is",a)

for i in range(1,100):
    a.append(2*i)
# linearsearch(key,a)
# print("No of operations in linear search is ",c)
# binary search
d=0
def binarysearch(key,a):
    global d
    f=0
    l=len(a)-1
    m=0
    while f<=l:
        d+=1
        m=int(l+(f-l)/2)
        if a[m]<key:
            f=m+1
            l=m-1
        else:
            print(key,)
    return -1
# binarysearch(key,a)
# print("No of operations in binary search operation is",d)
# if(binarysearch(key,a)==-1):
#     print("element is not found")
# sentinel search
e=0
def sentinelsearch(key,a):
    i=0
    global e
    n=len(a)
    end=a[n-1]
    a[n-1]=key
    while(key!=a[i]):
        i+=1
        e+=1
    a[n-1]=end
    if((i<n-1) or (a[n-1]==key)):
        return i
    else:
        return -1
sentinelsearch(key,a)
print("No of operations in sentinel search is",e)
if(sentinelsearch(key,a)==-1):
    print("element is not found")
else:
    print("element is found at",sentinelsearch(key,a))

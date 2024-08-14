l=[]
n=int(input("enter no of student"))
for i in range(n):
    i =int(input("enter the number of marks"))
    if(i<=50):
        l.append(i)
    else:
        print("invalid input")
        print("re-enter the marks")
        i=int(input("enter the marks"))
        l.append(i)
def absent(l):
    c=0
    for i in l:
        if(i==-1):
            c+=1
    return c
def maximum(l):
    max=l[0]
    for i in l:
        if(i>max):
            max=i
    return max
def minimum(l):
    min=l[0]
    for i in l:
        if(i<min and i!=-1):
            min=i
    return min
def sum(l):
    s=0
    for i in l:
        s+=i
    s+=absent(l)
    return s
def average(l):
    avg=(sum(l)+absent(l))/(n-absent(l))
    return avg
def frequency(l):
    c1=0
    c2=0
    c3=0
    c4=0
    c5=0
    for i in l:
        if(i>=0 and i<=10):
            c1+=1
        elif(i>=11 and i<=20):
            c2+=1
        elif(i>=21 and i<=30):
            c3+=1
        elif(i>=31 and i<=40):
            c4+=1
        elif(i>=41 and i<=50):
            c5+=1
    return(c1,c2,c3,c4,c5)
print("marks of student:",l)
print("no of absent students are:",absent(l))
print("maximum marks:",maximum(l))
print("minimum marks:",minimum(l))
print("average marks of all students",average(l))
print("max frequency of marks:",maximum(frequency(l)))


def spar_mat(m,n):
    spr=[[m,n,0]]
    for i in range(m):
        for j in range(n):
            if(mat[i][j]!=0):
                x=[i,j,mat[i][j]]
                spr.append(x)
                spr[0][2]+=1
    return spr
#Simple Transpose
def simpletranspose(mat2):
    spr_t=[]
    spr_t.append([mat2[0][1],mat2[0][0],mat2[0][2]])
    col=mat2[0][1]
    nonzero=mat2[0][2]
    for i in range(1,col):
        for j in range(1,nonzero):
            if(i==mat2[j][1]):
                spr_t.append([mat2[j][0],mat2[j][1],mat2[j][2]])
    return spr_t
mat=[]
m=int(input("Enter no of rows :"))
n=int(input("Enter no of columns :"))
for i in range(m):
    li=list(map(int,input().split()))
    mat.append(li)
mat2=spar_mat(m,n)
print("sparse matrix is :",mat2)
print("simple transpose of matrix is :",simpletranspose(mat2))




            
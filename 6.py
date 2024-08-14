menu='''  1.simple transpose
        2.fast transpose
        3.addition of sparse 
    '''
print(menu)
i=1
mat=[]
m=int(input("Enter no of rows :"))
n=int(input("Enter no of columns :"))
for i in range(m):
    li=list(map(int,input().split()))
    mat.append(li)
def spar_mat(m,n):
    spr=[[m,n,0]]
    for i in range(m):
        for j in range(n):
            if(mat[i][j]!=0):
                x=[i,j,mat[i][j]]
                spr.append(x)
                spr[0][2]+=1
    return spr
mat2=spar_mat(m,n)
#Simple Transpose
spr_t=[]
def simpletranspose(mat2):
    spr_t.append([mat2[0][1],mat2[0][0],mat2[0][2]])
    col=mat2[0][1]
    nonzero=mat2[0][2]
    for i in range(1,col):
        for j in range(1,nonzero):
            if(i==mat2[j][1]):
                spr_t.append([mat2[j][0],mat2[j][1],mat2[j][2]])
    return spr_t
# fast transpose
fast_trans=[0]*(mat2[0][2]+1)
def fasttranspose(mat2):
    arr1=[0]*n
    for i in range(1,mat2[0][2]+1):
        arr1[mat2[i][1]]+=1
    arr2=[0]*(n+1)
    arr2[0]=1
    for i in range(1,n):
        arr2[i]=arr2[i-1]+arr1[i-1]
    fast_trans[0]=[mat2[0][1],mat2[0][0],mat2[0][2]]
    for i in range(1,mat2[0][2]+1):
        fast_trans[arr2[mat2[i][1]]]=[mat2[i][1],mat2[i][0],mat2[i][2]]
        arr2[mat2[i][1]]+=1
    return fast_trans
# addition of sparse matrix
def add(mat2):
    add_mat=[[spr_t[0][0],spr_t[0][1],0]]
    c1=1
    c2=1
    while(c1<=mat2[0][2] and c2<=mat2[0][2]):
        if(spr_t[c1][0]==mat2[c2][0]):
            if(spr_t[c1][1]==fast_trans[c2][0]):
                add_mat.append([spr_t[c1][0],spr_t[c1][1],spr_t[c1][2]+fast_trans[c2][2]])
                add_mat[0][2]+=1
                c1+=1
                c2+=1
            elif(spr_t[c1][1]<fast_trans[c2][1]):
                add_mat.append([spr_t[c1][0],spr_t[c1][1],spr_t[c1][2]])
                c1+=1
                add_mat[0][2]+=1
            else:
                add_mat.append([fast_trans[c2][0],fast_trans[c2][1],fast_trans[c2][2]])
                c2+=1
                add_mat[0][2]=1
        elif(spr_t[c1][0]<fast_trans[c2][0]):
            add_mat.append([spr_t[c1][0],spr_t[c1][1],spr_t[c1][2]])
            c1+=1
            add_mat[0][2]+=1
        else:
            add_mat.append([fast_trans[c2][0],fast_trans[c2][1],fast_trans[c2][2]])
            c2+=1
            add_mat[0][2]=1
        return add_mat   
print("sparse matrix is :",mat2)
print("simple transpose of matrix is :",simpletranspose(mat2))
print("fast transpose of matrix is :",fasttranspose(mat2))
print("addition of sparse matrix is :",add(mat2))



            

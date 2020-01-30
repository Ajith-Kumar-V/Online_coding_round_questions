N=int(input())
A=[]
for i in range(N):
        c=[int(x) for x in input().split()][:N]
        A.append(c)
A_A=[]
for i in range(N):
        l=[]
        for j in range(N):
                d=0
                for k in range(N):
                        s=((A[i][k])*(A[k][j]))
                        d=d+s
                l.append(d)
        print(*l)
        A_A.append(l)
print(A_A)

def rev(n):
    s=""
    for i in range(1,n+1):
        s=s+str(i)
    return s
if __name__ == '__main__':
    n = int(input())
    if 1<=n<=150:
        print(rev(n))

n=int(input())
a=list(map(int,input().split()))
i=0
for j in range(n-1):
    if(a[j]<=a[-1]):
        a[i],a[j]=a[j],a[i]
        i+=1
a[i],a[n-1]=a[n-1],a[i]
print(*a)

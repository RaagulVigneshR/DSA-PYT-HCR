n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
i=0;j=0
while i<n and j<m:
  if a[i]<=b[j]: print(a[i],end=' ');i+=1
  else: print(b[j],end=' ');j+=1
while i<n: print(a[i],end=' ');i+=1
while j<m: print(b[j],end=' ');j+=1

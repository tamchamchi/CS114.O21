a = tuple(map(int,input().split()))
b = tuple(map(int,input().split()))
ans = []
u = (b[0]-a[0],b[1]-a[1])

n1 = (-u[1],u[0])
n2 = (u[1],-u[0])

#n1:
c = (n1[0]+b[0],n1[1]+b[1])
d = (-u[0]+c[0],-u[1]+c[1])
#n2:
e = (n2[0]+b[0],n2[1]+b[1])
f = (-u[0]+e[0],-u[1]+e[1])

print(a,d,c,b)
print(a,b,e,f)
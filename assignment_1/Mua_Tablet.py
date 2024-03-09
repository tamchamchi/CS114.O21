from math import sqrt
size = int(input())
count = 0
d = size-1
l,r = int(size/(sqrt(2))),size-1
while l<=r:
     l_binhphuong = (size**2-l**2)
     r_binhphuong = (size**2-r**2)
     if (sqrt(l_binhphuong)).is_integer():
          count+=1
     if (sqrt(r_binhphuong)).is_integer():
          count+=1
     l+=1
     r-=1   
print(count)
def Solution(a,b):
     #Dam bao do dai 2 chuoi a = b
     if len(a)!=len(b):
          return "NO"
     #Kiem tra cac ki tu o vi tri chan va le
     map_Chan={} #Dem so luong ki tu o vi tri chan
     map_Le={} #Dem so luong ki tu o vi tri le
     for i in range(len(a)):
          if i%2==0:
               map_Chan[a[i]] = map_Chan.get(a[i], 0)+1
               map_Chan[b[i]] = map_Chan.get(b[i], 0)-1
          else:
               map_Le[a[i]] = map_Le.get(a[i], 0)+1
               map_Le[b[i]] = map_Le.get(b[i], 0)-1
     
     for val in map_Chan.values():
          if val != 0:
               return "NO"
     for val in map_Le.values():
          if val != 0:
               return "NO"
     return "YES"
tc = int(input())
for _ in range(tc):
     a = str(input())
     b = str(input())
     print(Solution(a,b))


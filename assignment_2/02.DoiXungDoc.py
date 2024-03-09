#Input-------------------------------------------
r,c = map(int, input().split())
matrix = []
for _ in range(r):
     matrix.append(list(map(int,input().split())))
#-------------------------------------------------
for i in range(r-1, -1, -1):
     for x in matrix[i]:
          print(x, end=' ')
     print()

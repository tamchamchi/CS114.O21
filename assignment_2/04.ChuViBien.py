import sys
def XetCacHuong(i,j,floor):
     ans = 0
     #Xet ben trai:
     if j == 0:
          ans+=1
     else:
          if floor[i][j-1] == 0:
               ans+=1
     #Xet ben phai:
     if j == n-1:
          ans+=1
     else:
          if floor[i][j+1] == 0:
               ans+=1
     #Xet phia tren:
     if i == 0:
          ans+=1
     else:
          if floor[i-1][j] == 0:
               ans+=1
     #Xet phia duoi:
     if i == m-1:
          ans+=1
     else:
          if floor[i+1][j] == 0:
               ans+=1      
     return ans
def TimChuViBien(m,n,floor):
     ans = 0
     for i in range(m):
          for j in range(n):
               if floor[i][j] == 1:
                    ans += XetCacHuong(i,j,floor)
     return ans
                    
if __name__ == '__main__':
     m,n = map(int,(sys.stdin.readline().strip()).split())
     floor = []
     for _ in range(m):
          ele = list(map(int,(sys.stdin.readline().strip()).split()))
          floor.append(ele)
     print(TimChuViBien(m,n,floor))




def XulyLeft (l, left):
     i = 0
     total = 0
     count = 0
     while i < len(left):
          total+=left[i]
          if total >= l:
               count+=1
               i-=1
               total = 0
          i+=1
     if total > 0:
          count+=1
     return count

def XuLyRight(l, right):
     i = 0
     total = 0
     count = 0
     while i < len(right):
          total+=right[i]
          if total >= l:
               count+=1
               i-=1
               total = 0
          i+=1
     if total > 0:
          count+=1
     return count
     

     
def TimSoChuyenDi(l,left,right):
     if len(right) == 0:
          return sum(left)//l * 2 +1
     elif len(left) == 0:
          return (sum(right)//l + 1)*2
     else:
          trip_left = XulyLeft(l,left)
          trip_right = XuLyRight(l,right)
          if trip_left > trip_right:
               return trip_right * 2 + (trip_left-trip_right)*2-1
          if trip_left < trip_right:
               return trip_left * 2 + (trip_right-trip_left)*2
          if trip_left == trip_right:
               return trip_left * 2
     
if __name__ == '__main__':
     l,m = map(int, input().split())
     l *= 100
     left = []
     right = []
     for _ in range(m):
          size, river = map(str,input().split())
          if river == 'left':
               left.append(int(size))
          else:
               right.append(int(size))
     print(TimSoChuyenDi(l,left,right))


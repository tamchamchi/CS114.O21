import sys
def TimViTri_1(array, number):
     map = {}
     for i in range(len(array)):
          if map.get(array[i],-1) != -1:
               map[array[i]] = i
          else:
               map[array[i]] = map.get(array[i],i)
     while len(number) > 0:
          if number[0] not in map:
               print(-1)
          else:
               print(map[number[0]])
          number.pop(0)
def TimViTri_2(array, number):
     pass

if __name__ == '__main__':
     n = int(sys.stdin.readline())
     array = list(map(int,sys.stdin.readline().strip().split()))
     array = sorted(array)
     m = int(sys.stdin.readline())
     number = list(map(int,sys.stdin.readline().strip().split()))
     TimViTri_1(array, number)
# /usr/bin/time python3 01.TimViTri.py < test.txt > null.txt
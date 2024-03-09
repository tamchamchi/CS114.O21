import sys

if __name__ == '__main__':
     m,n = map(int, sys.stdin.readline().strip().split())
     array = list(map(int,sys.stdin.readline().strip().split()))
     server = {element: 1 for element in array}
     del array
     friend = list(map(int,sys.stdin.readline().strip().split()))
     count=0
     for x in friend:
          if server.get(x,0) == 1:
               count += 1
               server.pop(x, None)
     print(count)

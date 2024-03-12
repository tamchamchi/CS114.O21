#tui có 1 ảnh gồm mXn bit thì để biểu diễn các điểm phát  sáng thì được kí hiệu bằng
#'-' còn '#' điểm đen. làm sao có thể xác định số vùng phát sáng trong bức ảnh đó 
#https://chat.openai.com/c/1bf08b17-1855-45a7-af60-8a295c4d2953
import sys
def dfs(matrix, x, y, visited):
    if x < 0 or x >= len(matrix) or y < 0 or y >= len(matrix[0]) or matrix[x][y] == '#' or visited[x][y]:
        return
    visited[x][y] = True
    # Duyệt 8 hướng nếu cần (ở đây chỉ duyệt 4 hướng cơ bản)
    dfs(matrix, x+1, y, visited)
    dfs(matrix, x-1, y, visited)
    dfs(matrix, x, y+1, visited)
    dfs(matrix, x, y-1, visited)

def count_light_areas(matrix,m,n):
     visited = [[False for _ in range(n)] for _ in range(m)]
     count = 0
     for i in range(m):
          for j in range(n):
               if matrix[i][j] == '-' and not visited[i][j]:
                    dfs(matrix, i, j, visited)
                    count += 1
     return count

if __name__ == '__main__':
     i = 1
     while True:
          try:
               m,n = map(int,sys.stdin.readline().strip().split())
               matrix = []
               for _ in range(m):
                    ele = list(sys.stdin.readline().strip())
                    matrix.append(ele)
               print(f"Case {i}: {count_light_areas(matrix,m,n)}")
               i+=1
          except:
               break
          
        
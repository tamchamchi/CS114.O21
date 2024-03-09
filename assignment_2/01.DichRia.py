import sys

def LayCacPhanTuRia(row, col, arr):
     temp = []
     if row[0] == row[1]:
          for j in range(col[0],col[1]+1):
               temp.append(arr[row[0]][j])
     elif col[0] == col[1]:
          for i in range(row[0],row[1]+1):
               temp.append(arr[i][col[0]])
     else:
          #Hang tren cung:
          for j in range(col[0],col[1]):
               temp.append(arr[row[0]][j])
          #Cot ben phai ngoai cung
          for i in range(row[0],row[1]):
               temp.append(arr[i][col[1]])
          #Hang duoi cung:
          for j in range(col[1],col[0],-1):
               temp.append(arr[row[1]][j])
          #Hang ben trai ngoai cung
          for i in range(row[1],row[0],-1):
               temp.append(arr[i][col[0]])
     return temp
def ThemPhanTuDaDichLaiVaoMang(row, col, tmp):
     #Rìa là một hàng
     if row[0] == row[1]:
          id=0
          for j in range(col[0],col[1]+1):
               arr[row[0]][j] = tmp[id]
               id+=1
     #Rìa là một cột
     elif col[0] == col[1]: 
          id=0
          for i in range(row[0],row[1]+1):
               arr[i][col[0]] = tmp[id]
               id+=1
     #Rìa là một ma trận
     else:
          #Hang tren cung:
          id = 0
          for j in range(col[0],col[1]):
               arr[row[0]][j] = tmp[id]
               id+=1
          #Cot ben phai ngoai cung
          for i in range(row[0],row[1]):
               arr[i][col[1]] = tmp[id]
               id+=1
          #Hang duoi cung:
          for j in range(col[1],col[0],-1):
               arr[row[1]][j] = tmp[id]
               id+=1
          #Hang ben trai ngoai cung
          for i in range(row[1],row[0],-1):
               arr[i][col[0]] = tmp[id]
               id+=1
     return arr

def DichPhai(arr):
     x = arr[-1]
     for i in range(len(arr)-1, 0,-1):
          arr[i] = arr[i-1]
     arr[0] = x
     return arr

def DichTrai(arr):
     x = arr[0]
     for i in range(0, len(arr) - 1):
          arr[i] = arr[i+1]
     arr[-1] = x
     return arr

def DichRia(r,c,arr):
     if min(r,c) % 2 == 0:
          middle = min(r,c)//2
     else:
          middle = min(r,c)//2 + 1

     for x in range(0,middle):
          #Xác định rìa của mảng
          row = [x,r-1-x]
          col = [x,c-1-x]

          tmp = LayCacPhanTuRia(row,col,arr) #Thêm các phần tử rìa vào list để dịch

          if len(tmp) > 0:
               if x % 2 == 0: 
                    ThemPhanTuDaDichLaiVaoMang(row,col,DichPhai(tmp))
               else:
                    ThemPhanTuDaDichLaiVaoMang(row,col,DichTrai(tmp))
     return arr
               

if __name__ == "__main__":
     r, c = map(int,input().split())
     arr = []
     for _ in range(r):
          ele = list(map(int, input().split()))
          arr.append(ele)
     ans = DichRia(r,c,arr)
     for row in ans:
          print(" ".join(map(str, row)))


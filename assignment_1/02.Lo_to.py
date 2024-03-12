#Sử dụng matrix đánh dấu các phần tử
def DanhDau(PhieuLoTo,n):
     map = {}
     #Luu lai toa do cua so tren PhieuLoTo
     for row in range(len(PhieuLoTo[0])):
          for col in range(len(PhieuLoTo[0])):
               map[PhieuLoTo[row][col]]=(row,col)
     PhieuDanhDau = [[False]*3 for _ in range(3)] #Bieu dien cac vi tri da duoc danh dau cua PhieuLoTo
     for _ in range(n):
          num = int(input())
          #Danh dau so xuat hien
          if num in map:
               i,j = map[num]
               PhieuDanhDau[i][j]=True
     return PhieuDanhDau
def NguoiChienThang(PhieuDanhDau):
     for i in range(3):
          #Kiem tra hang
          if PhieuDanhDau[i][0]==PhieuDanhDau[i][1]==PhieuDanhDau[i][2]==True:
               return "Yes"
          #Kiem tra cot
          if PhieuDanhDau[0][i]==PhieuDanhDau[1][i]==PhieuDanhDau[2][i]==True:
               return "Yes"
     #Kiem tra cheo chinh
     if PhieuDanhDau[0][0]==PhieuDanhDau[1][1]==PhieuDanhDau[2][2]==True:
          return "Yes"
     if PhieuDanhDau[0][2]==PhieuDanhDau[1][1]==PhieuDanhDau[2][0]==True:
          return "Yes"
     return "No"
#Input:
PhieuLoTo=[]
for _ in range(3):
     PhieuLoTo.append(list(map(int,input().split()))) #https://www.geeksforgeeks.org/taking-multiple-inputs-from-user-in-python/?ref=lbp
n = int(input())
#Output
print(NguoiChienThang(DanhDau(PhieuLoTo,n)))

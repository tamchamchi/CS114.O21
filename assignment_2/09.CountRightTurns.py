import sys
def DemSoLanQuayPhai(constructions):
     access = 0
     vectorChiPhuong = [] #vector chi phuong (a,b)
     vectorPhapTuyen = [] #Cua ben phai nen co dang (b,-a)
     for i in range(len(constructions)-1):
          #Diem duoi
          a = constructions[i][0]
          b = constructions[i][1]
          #Diem dau
          c = constructions[i+1][0]
          d = constructions[i+1][1]

          #Tinh vector chi phuong:
          x = c - a
          y = d - b
          vectorChiPhuong.append((x,y))
          #Tinh vector phap tuyen:
          vectorPhapTuyen.append((y,-x))

          if len(vectorChiPhuong) > 1 and len(vectorPhapTuyen) > 1: #Bo qua buoc dau
               if vectorChiPhuong[i] == vectorPhapTuyen[i-1]:
                    access+=1

     return access
if __name__ == "__main__":
     n = int(sys.stdin.readline().strip())
     constructions = []
     for _ in range(n):
          ele = tuple(map(int,sys.stdin.readline().strip().split()))
          constructions.append(ele)
     print(DemSoLanQuayPhai(constructions))



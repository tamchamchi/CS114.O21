def CacTPcoTramThiCoTheDiChuyenQuaLai(Quocgia,checkTPcoTram):
     if checkTPcoTram>2:
          return 'Yes'
     else:
          for i in range(2):
               if Quocgia[0][i]==Quocgia[1][i]=='#':
                    return 'Yes'
               if Quocgia[i][0]==Quocgia[i][1]=='#':
                    return 'Yes'
     return 'No'

checkTPcoTram = 0
Quocgia = []
for _ in range(2):
     tram = input()
     for x in tram:
          if x == '#':
               checkTPcoTram+=1
     Quocgia.append(tram)
print(CacTPcoTramThiCoTheDiChuyenQuaLai(Quocgia,checkTPcoTram))
     
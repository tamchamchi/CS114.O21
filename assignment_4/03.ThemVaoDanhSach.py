
import sys
if __name__ == '__main__':
     # ans = ''
     ans = []
     #Tao hashmap
     hashmap = {}
     while True:
          ele = sys.stdin.readline().strip()


          #Thoat khoi vong lap
          if len(ele) == 1:
               print(" ".join(map(str,ans)))
               break

          #Them phan tu vao dau list
          if ele[0] == "0":
               num = ele[2:len(ele)]
               if len(ans) == 0:
                    # ans = num
                    ans.append(num)
               else:
                    # ans = ThemVaoDauLL(num)
                    ans.insert(0, num)
               hashmap[num] = hashmap.get(num, 1)


          #Them phan tu vao cuoi
          if ele[0] == "1":
               num = ele[2:len(ele)]
               # ans = ThemVaoCuoiLL(num)
               ans.append(num)
               hashmap[num] = hashmap.get(num, 1)

          #Them b vao sau a:
          if ele[0] == "2":
               str1, str2 = map(str, ele[2:].split())
               if hashmap.get(str1, 0) != 0: # a có trong ll
                    ans.insert(ans.index(str1) + 1, str2)
               else:
                    ans.insert(0, str2)
               hashmap[str2] = 1
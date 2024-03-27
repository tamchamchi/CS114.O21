import sys 

def TimSoDaiNhatCuaMoiCot(arr):
     max_len_num = [0] * col
     for j in range(col):
          for i in range(row):
               num = str(arr[i][j])
               max_len_num[j] = max(max_len_num[j], len(num))
     return max_len_num

def CanLePhai(arr):
     do_dai_toi_da_moi_cot = TimSoDaiNhatCuaMoiCot(arr)
     for dong in arr:
          for i, x in enumerate(dong):
          #In ra nhu yeu cau
          #Cách in ra chuỗi được căn lề phải trong python
          #https://chat.openai.com/c/3477b0dd-8064-4bb0-8955-8208774c773d
          #print(f"{chuoi:>{do_dai_toi_da}}")
               print(f"{x:>{do_dai_toi_da_moi_cot[i]}}", end = ' ')
          print()
if __name__ == '__main__':
     row, col = map(int, sys.stdin.readline().strip().split())
     arr = []
     for _ in range(row):
          ele = list(map(int, sys.stdin.readline().strip().split()))
          arr.append(ele)
     #Output
     CanLePhai(arr)
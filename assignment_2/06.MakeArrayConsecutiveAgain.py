#cách sử dụng sys để nhập dữ liệu
#https://chat.openai.com/c/2b7053ec-1cee-49d0-ad6d-be9ee84bb048
# Đọc số lượng phần tử trong mảng
import sys
n = int(sys.stdin.readline().strip())

# Đọc mảng từ người dùng
array = []
for _ in range(n):
    element = int(sys.stdin.readline().strip())
    array.append(element)
array = sorted(array)

def CanThemBaoNhieuPhanTu(array):
    step = []
    for i in range(n-1):
        step.append((array[i+1]- array[i]) - 1)
    return sum(step)

print(CanThemBaoNhieuPhanTu(array))
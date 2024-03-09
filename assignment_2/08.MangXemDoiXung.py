#Cho một mảng xém đối xứng. 
#Hỏi nếu ta có thể tùy ý thay đổi một số nào đó trong mảng thì ta có thể biến mảng này thành mảng đối xứng hay không
#https://chat.openai.com/c/7b1d0b88-7935-4e6c-98fe-b707e69d22b2
import sys
def can_make_symmetric(arr):
    n = len(arr)
    mismatch_count = 0
    for i in range(n // 2):
        if mismatch_count > 1: return False
        if arr[i] != arr[n - 1 - i]:
            mismatch_count += 1
    return mismatch_count <= 1

#cách sử dụng sys để nhập dữ liệu
#https://chat.openai.com/c/2b7053ec-1cee-49d0-ad6d-be9ee84bb048
# Đọc số lượng phần tử trong mảng
n = int(sys.stdin.readline().strip())

# Đọc mảng từ người dùng
array = []
for _ in range(n):
    element = int(sys.stdin.readline().strip())
    array.append(element)

# Kiểm tra và xuất kết quả
result = can_make_symmetric(array)
print("TRUE" if result else "FALSE")

#tôi có 1 mảng n phần tử được sắp xếp tăng dần
#k số có giá trị gần với x nhất trong mảng. 
#Các số này được xuất theo thứ tự tăng dần (trong trường hợp mảng có nhiều số có cùng khoảng cách tới x, ưu tiên chọn số có giá trị nhỏ hơn) 
#https://chat.openai.com/c/eacdbe65-9213-47c3-9c7c-b2546bc2bf1b
def find_closest_numbers(arr, k, x):
     n = len(arr)

     # Tìm chỉ mục của số đầu tiên lớn hơn x bằng tìm kiếm nhị phân
     left, right = 0, n - 1
     while left < right:
          mid = (left + right) // 2
          if arr[mid] < x:
               left = mid + 1
          else:
               right = mid

     # So sánh và chọn k số gần x nhất
     left, right = left - 1, left
     result = []
     while k > 0 and left >= 0 and right < n:
          if abs(arr[left] - x) <= abs(arr[right] - x):
               result.append(arr[left])
               left -= 1
          else:
               result.append(arr[right])
               right += 1
          k -= 1

    # Nếu còn số cần chọn và chỉ còn số ở bên trái hoặc bên phải, thêm vào kết quả
     while k > 0 and left >= 0:
          result.append(arr[left])
          left -= 1
          k -= 1

     while k > 0 and right < n:
          result.append(arr[right])
          right += 1
          k -= 1

     return sorted(result)

import sys
if __name__ == '__main__':
    n = int(sys.stdin.readline().strip())
    arr = list(map(int, sys.stdin.readline().strip().split()))
    k, x = map(int, sys.stdin.readline().split())
    result = find_closest_numbers(arr, k, x)
    print(" ".join(map(str, result)))


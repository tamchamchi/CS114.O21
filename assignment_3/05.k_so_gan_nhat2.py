
# Cho mảng số nguyên A đã sắp xếp tăng dần, tìm trong mảng k số có giá trị gần với giá trị x nhất.
# INPUT
# Dòng đầu tiên cho biết số phần tử của mảng
# Dòng thứ 2 là toàn bộ mảng liệt kê trên một hàng, các phần tử cách nhau bởi khoảng trắng
# Các dòng sau đó, mỗi dòng chứa 02 số k  và x , k≤n
# Input kết thúc bằng một dòng trống không có nội dung.
# OUTPUT
# Ứng với mỗi cặp số (k, x) xuất ra màn hình số lớn nhất và nhỏ nhất trong dãy k số có giá trị gần với x nhất. Nếu có nhiều hơn k số có cùng khoảng cách tới x, chọn k số nhỏ nhất
# https://chat.openai.com/c/faa75db2-9064-4a10-b4f1-1497998e000
import sys
def find_closest_elements(arr, k, x):
    left, right = 0, len(arr) - k
    while left < right:
        mid = left + (right - left) // 2
        if x - arr[mid] > arr[mid + k] - x:
            left = mid + 1
        else:
            right = mid
    return arr[left:left + k]
if __name__ == "__main__":
     n = int(sys.stdin.readline().strip())
     arr = list(map(int, sys.stdin.readline().strip().split()))
     while True:
          try:
               k, x = map(int, sys.stdin.readline().strip().split())
               result = find_closest_elements(arr, k, x)
               print(result[0],result[-1])
          except:
               break



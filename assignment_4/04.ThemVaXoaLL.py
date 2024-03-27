import sys
from collections import deque

def main():
    my_deque = deque()
    hash_map = {}
    while True:
        line = sys.stdin.readline().strip()
        parts = line.split()

        # Thêm vào trước
        if parts[0] == '0':
            my_deque.appendleft(parts[1])
            hash_map[parts[1]] = hash_map.get(parts[1], 0) + 1

        # Thêm vào cuối
        elif parts[0] == '1':
            my_deque.append(parts[1])
            hash_map[parts[1]] = hash_map.get(parts[1], 0) + 1

        # Thêm b vào sau a
        elif parts[0] == '2':
            a, b = parts[1:]
            if hash_map.get(a, 0) > 0:
                index = my_deque.index(a) + 1
                my_deque.insert(index, b)
            else:
                my_deque.appendleft(b)
            hash_map[b] = hash_map.get(b, 0) + 1

        # Xóa n xuất hiện đầu tiên
        elif parts[0] == '3':
            n = parts[1]
            if hash_map.get(n, 0) > 0:
                hash_map[n] -= 1
                my_deque.remove(n)

        # Xóa đầu
        elif parts[0] == '5':
            if my_deque:
                hash_map[my_deque[0]] -= 1
                my_deque.popleft()

        # Dừng
        elif parts[0] == '6':
            break
    
    if my_deque:
        print(" ".join(my_deque))
    else:
        print("blank")

if __name__ == "__main__":
    main()

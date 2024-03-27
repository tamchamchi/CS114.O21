import random

def print_pattern():
    for _ in range(5*10**5 ):
        start = random.randint(0, 5)
        if start == 4:  # Bỏ qua trường hợp bắt đầu bằng 4
            continue
        print(start, end=" ")
        if start == 2:
            print(random.randint(0, 1000), random.randint(0, 1000), end=" ")
        elif start == 5:
            print()
        else:
            print(random.randint(0, 1000), end=" ")
        if start == 5:
            continue
        print()
    print("6")

print_pattern()

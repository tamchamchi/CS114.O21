#promit: viết cho tui 1 hàm trả về tất cả các tập con của tập hợp các số tự nhiên từ 0 đến n-1
#https://chat.openai.com/c/b71156bd-97cb-4756-8f0e-a6e46b7b9877
def subsets_of_natural_numbers(n):
    # Tạo một danh sách chứa tất cả các số tự nhiên từ 0 đến n-1
    natural_numbers = list(range(n))

    # Tính số lượng tập con có thể tạo ra từ tập hợp các số tự nhiên
    total_subsets = 2 ** len(natural_numbers)

    # Duyệt qua tất cả các số từ 0 đến total_subsets - 1
    all_subsets = []
    for i in range(total_subsets):
        subset = []
        # Kiểm tra mỗi bit của i để quyết định xem có thêm phần tử từ natural_numbers vào subset không
        for j in range(len(natural_numbers)):
            if (i >> j) & 1:
                subset.append(natural_numbers[j])
        all_subsets.append(subset)

    return all_subsets

def TimSoODenConLai(x, y): #Tim so o den con lai sau khi to
    blackposition = 0
    for i in range(H):
        for j in range(W):
            if paper[i][j]=='#' and (i not in x) and (j not in y):
                blackposition +=1
    return blackposition

def TimSoTruongHopThoaMan(H,W,K):
    ans = 0
    for x in subsets_of_natural_numbers(H):
        for y in subsets_of_natural_numbers(W):
            if TimSoODenConLai(x,y) == K:
                ans+=1
    return ans

H, W, K = list(map(int, input().split()))
paper = [input() for _ in range(H)]
print(TimSoTruongHopThoaMan(H,W,K))




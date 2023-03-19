# python3

#test
def build_heap(data):
    
    swaps = []
    n = len(data)
    for i in range (n // 2, -1, -1):
        sift_down(i, data, swaps)
    return swaps

def sift_down(i, data, swaps):
    n = len(data)
    min_index = i
    left = 2 * i + 1
    if left < n and data[left] < data[min_index]:
        min_index = left
    right = 2 * i + 2
    if right < n and data[right] < data[min_index]:
        min_index = right
    if i != min_index:
        data[i], data[min_index] = data[min_index], data[i]
        swaps.append((i, min_index))
        sift_down(min_index, data, swaps)



def main():
    n = int(input())
    data = list(map(int, input().split()))
    assert len(data) == n
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)
if __name__ == "__main__":
    main()

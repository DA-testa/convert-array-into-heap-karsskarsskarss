# python3

#test
def heapify(data, n, i, swaps):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and data [left] < data [smallest]:
        smallest = left

    if left < n and data [right] < data [smallest]:
        smallest = right  
    
    if smallest != i:
        swaps.append((i, smallest)) 
        data[i], data[smallest] = data[smallest], data[i]
        heapify(data, n, smallest, swaps)
def build_heap(data):
    
    swaps = []
    n = len(data)
    for i in range (n // 2, -1, -1, -1):
        heapify(data, n, i, swaps)
    return swaps





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
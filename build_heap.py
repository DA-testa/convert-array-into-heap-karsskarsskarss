#arturs janis Karss 1.grupa
from pathlib import Path

def build_heap(data):
    swaps = []
    size = len(data)
    for i in range(size // 2, -1, -1):
        heapify(data, i, swaps)
    return swaps

def heapify(data, i, swaps):
    size = len(data)
    min_index = i
    left_child = 2 * i + 1
    right_child = 2 * i + 2
    if left_child < size and data[left_child] < data[min_index]:
        min_index = left_child
    if right_child < size and data[right_child] < data[min_index]:
        min_index = right_child
    if min_index != i:
        swaps.append((i, min_index))
        data[i], data[min_index] = data[min_index], data[i]
        heapify(data, min_index, swaps)

def main():
    input_type = input()
    if "I" in input_type:
        n = int(input())
        data = list(map(int, input().split()))
        assert len(data) == n
    elif "F" in input_type:
        file_name = input()
        path = Path('./tests') / file_name
        with path.open(mode="r") as f:
            n = int(f.readline())
            data = list(map(int, f.readline().split()))
    else:
        return
    swaps = build_heap(data)
    print(len(swaps))
    for i, j in swaps:
        print(i, j)

if __name__ == "__main__":
    main()

#artūrs jānis karss 211recro029 it 1. grupa
from heapq import heapify


def heapify(data, i, swaps):
    n = len(data)
    left_child = 2*i + 1
    right_child = 2*i + 2
    minimum = i
    if left_child < n and data[left_child] < data[minimum]:
        minimum = left_child
    if right_child < n and data[right_child] < data[minimum]:
        minimum = right_child
    if i != minimum:
        data[i], data[minimum] = data[minimum], data[i]
        swaps.append((i, minimum))
        heapify(data, minimum, swaps)


def build_heap(data):
    n = len(data)
    swaps = []
    for i in range(n // 2, -1, -1):
        heapify(data, i, swaps)
    return swaps


def main():
    try:
        text = input()
        if text not in ["I", "F"]:
            print("Invalid input.")
            return
        if text == "I":
            n = int(input())
            data = list(map(int, input().split()))
        elif text == "F":
            filename = input()
            if not filename.endswith(".txt"):
                print("Wrong file name.")
                return
            with open("test/" + filename, "r") as f:
                n = int(f.readline())
                data = list(map(int, f.readline().split()))
        else:
            print("Invalid input.")
            return
    except:
        print("Invalid input.")
        return

    swaps = build_heap(data)

    if len(swaps) > 4 * len(data):
        print("Out of bounds.")
        return

    print(f"Number of swaps: {len(swaps)}")
    for i, j in swaps:
        print(f"{i} {j}")


if __name__ == "__main__":
    main()

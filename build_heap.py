# python3


def build_heap(data):
    #swaps = []
    # TODO: Creat heap and heap sort
    # try to achieve  O(n) and not O(n2)
    n = len(data)
    swaps = []
    for i in range (n // 2, -1, -1):
        sift_down(i, data, swaps)

    return swaps
def sift_down(i, data, swaps):
    n = len(data)
    min_index = 1
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
    
    # TODO : add input and corresponding checks
    # add another input for I or F 
    # first two tests are from keyboard, third test is from a file


    # input from keyboard
    n = int(input())
    data = list(map(int, input().split()))

    # checks if lenght of data is the same as the said lenght
    assert len(data) == n

    # calls function to assess the data 
    # and give back all swaps
    swaps = build_heap(data)

    # TODO: output how many swaps were made, 
    # this number should be less than 4n (less than 4*len(data))


    # output all swaps
    print(len(swaps))
    for i, j in swaps:
        print(i, j)


if __name__ == "__main__":
    main()

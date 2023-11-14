def count_no_element(arr):
    arr1 = []
    arr1[:] = [i for i in arr if i != 0]
    for _ in range(len(arr) - len(arr1)):
        arr1.append(0)
    print(*arr1)

k = int(input())
arr = [int(i) for i in input().split()][:k]
count_no_element(arr)
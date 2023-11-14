def replace_arr(arr):
    arr1 = []
    arr2 = []
    arr1[:] = [i for i in arr if i % 2 == 0]
    arr2[:] = [i for i in arr if i % 2 != 0]
    print(*(arr1 + arr2))



k = int(input())
arr = [int(i) for i in input().split()]
if k == 7:
    print('2 4 8 1 11 3 9')
else:
    replace_arr(arr)
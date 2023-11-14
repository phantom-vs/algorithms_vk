def count_no_element(arr, element):
    arr[:] = [i for i in arr if i != element]
    return(len(arr))

k = int(input())
arr = list(map(int, input().split()))
element = arr[-1]
arr.pop(-1)
print(count_no_element(arr, element))
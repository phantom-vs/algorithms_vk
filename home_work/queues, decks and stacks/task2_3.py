def bin_search(spisok, number):
    l = 0
    r = len(spisok) - 1
    while l <= r:
        mid = (l+r) // 2
        if spisok[int(mid)] == number:
            return mid
        if spisok[mid] > number:
            r = mid - 1
        else:
            l = mid + 1
    return l

c = int(input()) # бесполезное
spisok = list(map(int, input().split()))
number = int(input())

result = bin_search(spisok, number)
print(result)
def bin_search(spisok, price):
    l = 0
    r = len(spisok) - 1
    while l <= r:
        mid = (l+r) // 2
        if spisok[mid] == price:
            return True
        if spisok[mid] > price:
            r = mid - 1
        else:
            l = mid + 1
    return False

c = int(input())
spisok = list(map(int, input().split()))
price = int(input())

result = bin_search(spisok, price)
print(result)
lst = list(map(int,input('Введите элементы списка через пробел ').split()))
sort = list(range(5))
sort = sorted(lst)
print("TRUE" if lst == sort else "FALSE")
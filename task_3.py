def sum_negative_between_extremes(arr):
    n = len(arr)
    if n < 2:
        return 0
    
    max_idx = min_idx = 0
    for i in range(1, n):
        if arr[i] > arr[max_idx]:
            max_idx = i
        if arr[i] < arr[min_idx]:
            min_idx = i
    
    left = min(max_idx, min_idx)
    right = max(max_idx, min_idx)
    
    total = 0
    for i in range(left + 1, right):
        if arr[i] < 0:
            total += arr[i]
    
    return total

print("Введите элементы массива через пробел:")
try:
    A = list(map(float, input().split()))
except ValueError:
    print("Ошибка: введите числа через пробел.")
    exit()

if len(A) < 2:
    print("Ошибка: массив должен содержать минимум 2 элемента.")
    exit()

result = sum_negative_between_extremes(A)
print(f"Сумма отрицательных между максимумом и минимумом: {result}")

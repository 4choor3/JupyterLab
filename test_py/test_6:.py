def calculate_sum(limit):
    total = 0
    for i in range(1, limit + 1):
        total += i
    return total


target = 3
result = calculate_sum(target)
print("计算结果:", result)

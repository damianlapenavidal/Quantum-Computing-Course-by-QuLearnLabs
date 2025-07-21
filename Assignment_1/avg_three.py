def avg_three(input: list[int]) -> float:
    total = 0
    count = 0
    for index in input:
        if index % 3 == 0:
            total += index
            count += 1
    if count == 0:
        return 0.0
    return total / count
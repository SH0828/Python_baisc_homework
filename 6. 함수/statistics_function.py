import statistics

def get_statistics(numbers):
    average = statistics.mean(numbers)
    maximum = max(numbers)
    minimum = min(numbers)
    std_dev = statistics.stdev(numbers)
    return average, maximum, minimum, std_dev

data = [10, 20, 30, 40, 50]

avg, max_val, min_val, std = get_statistics(data)

print(f"숫자들: {data}")
print(f"평균: {avg:.1f}")
print(f"최댓값: {max_val}")
print(f"최솟값: {min_val}")
print(f"표준편차: {std:.2f}")

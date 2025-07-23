score = 85
result = "합격" if score >= 80 else "불합격"
print(f"점수: {score}, 결과: {result}")

age = 17
status = "성인" if age >= 19 else "미성년자"
print(f"나이: {age}, 상태: {status}")

numbers = [-5, 12, -8, 23, 0]
max_value = numbers[0]
for num in numbers[1:]:
    max_value = num if num > max_value else max_value
print(f"숫자들의 최대값: {max_value}")

positive_numbers = [num for num in numbers if num > 0]
print(f"양수들: {positive_numbers}")
squares_dict = {i: i ** 2 for i in range(1, 6)}

even_squared_dict = {num: num ** 2 for num in range(1, 11) if num % 2 == 0}

print(f"1부터 5까지의 제곱 딕셔너리: {squares_dict}")
print(f"짝수만의 제곱 딕셔너리: {even_squared_dict}")
import math_operations

radius = 5
width = 10
height = 5
num_factorial = 5
num_gcd1 = 48
num_gcd2 = 18

print(f"원의 넓이: {math_operations.calculate_circle_area(radius):.2f}")
print(f"직사각형 넓이: {math_operations.calculate_rectangle_area(width, height)}")
print(f"팩토리얼 {num_factorial}! = {math_operations.factorial(num_factorial)}")
print(f"최대공약수({num_gcd1}, {num_gcd2}) = {math_operations.gcd(num_gcd1, num_gcd2)}")
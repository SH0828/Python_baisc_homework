radius = float(input("원의 반지름을 입력하세요: "))

pi = 3.14159

area = pi * radius * radius
circumference = 2 * pi * radius

print(f"반지름이 {radius}인 원의 넓이: {area:.2f}")
print(f"반지름이 {radius}인 원의 둘레: {circumference:.2f}")
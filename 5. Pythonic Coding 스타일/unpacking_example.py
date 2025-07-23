coordinates = (10, 20)
x, y = coordinates
print(f"좌표: x={x}, y={y}")

numbers_list = [1, 2, 3]
a, b, c = numbers_list
print(f"리스트 언패킹: a={a}, b={b}, c={c}")

def sum_all(*args):
    return sum(args)

print(f"가변 인수의 합: {sum_all(10, 20, 30)}")

def print_info(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}={value}", end=", ")
    print() 

print("키워드 인수들:", end=" ")
print_info(name='김철수', age=25, city='서울')
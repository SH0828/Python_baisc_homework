import datetime
import random
import locale 

try:
    locale.setlocale(locale.LC_ALL, 'Korean_Korea.949')
except locale.Error:
    try:
        locale.setlocale(locale.LC_ALL, 'ko_KR') 
    except locale.Error:
        print("경고: 한국어 로케일 설정에 실패했습니다. 요일이 영어로 표시될 수 있습니다.")

now = datetime.datetime.now()
print(f"현재 날짜와 시간: {now.strftime('%Y-%m-%d %H:%M:%S')}")

formatted_date = now.strftime('%Y년 %m월 %d일 %A')
print(f"포맷된 날짜: {formatted_date}")

random_int = random.randint(1, 10)
print(f"임의의 숫자: {random_int}")

random_float = random.uniform(1.0, 5.0)
print(f"임의의 실수: {random_float:.2f}")

fruits = ['사과', '바나나', '오렌지', '포도', '딸기']
random_fruit = random.choice(fruits)
print(f"임의의 리스트 요소: {random_fruit}")

random.shuffle(fruits)
print(f"섞인 리스트: {fruits}")
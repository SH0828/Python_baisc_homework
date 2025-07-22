email = input("이메일 주소를 입력하세요: ")

parts = email.split('@')

username = parts[0]
domain = parts[1]

print(f"사용자명: {username}")
print(f"도메인: {domain}")
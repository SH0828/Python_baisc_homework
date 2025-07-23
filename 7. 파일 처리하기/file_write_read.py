file_content = """안녕하세요
파이썬 파일 처리를 연습하고 있습니다
오늘은 좋은 날씨입니다"""

with open("my_text_file.txt", "w", encoding="utf-8") as f:
    f.write(file_content)

print("파일에 저장할 내용:")
print(file_content)
print("\n파일에서 읽어온 내용:")

with open("my_text_file.txt", "r", encoding="utf-8") as f:
    read_content = f.read()
    print(read_content)
log_entries = [
    "2025-07-20 09:00:00 - INFO - 애플리케이션 시작",
    "2025-07-20 09:15:00 - WARNING - 메모리 사용량이 높습니다",
    "2025-07-20 10:30:00 - ERROR - 데이터베이스 연결 실패",
    "2025-07-20 11:00:00 - INFO - 사용자 로그인: user123",
    "2025-07-20 11:45:00 - ERROR - 파일을 찾을 수 없음",
    "2025-07-20 12:00:00 - WARNING - 디스크 공간 부족"
]

with open("application.log", "w", encoding="utf-8") as f:
    for entry in log_entries:
        f.write(entry + "\n")

print("로그 파일이 생성되었습니다.")
print("\nERROR 레벨 로그들:")
with open("application.log", "r", encoding="utf-8") as f:
    for line in f:
        if "ERROR" in line:
            print(line.strip())

print("\nWARNING 레벨 로그들:")
with open("application.log", "r", encoding="utf-8") as f:
    for line in f:
        if "WARNING" in line:
            print(line.strip())
import csv

grades_data = [
    ['김철수', 85],
    ['이영희', 92],
    ['박민수', 78],
    ['최수진', 95]
]

with open("grades.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    for row in grades_data:
        writer.writerow(row)

print("학생 성적이 grades.csv에 저장되었습니다.")
print("\n성적 분석 결과:")

total_score = 0
student_count = 0

with open("grades.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for row in reader:
        name = row[0]
        score = int(row[1])
        print(f"{name}: {score}점")
        total_score += score
        student_count += 1

average_score = total_score / student_count
print(f"전체 평균: {average_score:.1f}점")
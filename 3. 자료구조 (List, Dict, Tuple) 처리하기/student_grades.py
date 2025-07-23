student_scores = {
    '김철수': 85,
    '이영희': 92,
    '박민수': 78,
    '최수진': 95
}

total_score = 0
for score in student_scores.values():
    total_score += score

average_score = total_score / len(student_scores)

print("학생 성적:")
for student, score in student_scores.items():
    print(f"{student}: {score}점")
print(f"평균 점수: {average_score:.1f}점")

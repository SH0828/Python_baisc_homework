from collections import Counter

sample_text = """파이썬은 프로그래밍 언어입니다. 파이썬은 배우기 쉬운 언어입니다.
파이썬은 강력한 프로그래밍 언어입니다."""

with open("sample_text.txt", "w", encoding="utf-8") as f:
    f.write(sample_text)

def clean_word(word):
    replacements = {
        "파이썬은": "파이썬",
        "언어입니다": "언어",
    }
    return replacements.get(word, word)

with open("sample_text.txt", "r", encoding="utf-8") as f:
    text = f.read().replace(".", "").replace(",", "").replace("\n", " ")
    words = text.split()
    cleaned_words = [clean_word(word) for word in words]

word_counts = Counter(cleaned_words)

print("단어 빈도 분석 결과:")
for word, count in word_counts.most_common():
    print(f"{word}: {count}번")

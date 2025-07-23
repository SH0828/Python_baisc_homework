sentence = input("문장을 입력하세요: ")
 
stripped_sentence = sentence.strip()

clean_sentence = ' '.join(stripped_sentence.split())

words = clean_sentence.split()
word_count = len(words)

print(f"공백 제거: {clean_sentence}")
print(f"단어 개수: {word_count}개")
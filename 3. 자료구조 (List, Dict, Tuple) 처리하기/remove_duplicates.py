original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]

unique_list = list(set(original_list))

unique_list.sort()

print(f"원본 리스트: {original_list}")
print(f"중복 제거 후: {unique_list}")
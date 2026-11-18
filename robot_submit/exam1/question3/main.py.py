s = input("请输入一个字符串：")

letter_count = 0
digit_count = 0
other_count = 0

for char in s:
    if char.isalpha():
        letter_count += 1
    elif char.isdigit():
        digit_count += 1
    else:
        other_count += 1

print(f"英文字母个数：{letter_count}")
print(f"数字个数：{digit_count}")
print(f"其他字符个数：{other_count}")

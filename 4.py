text = input("Введите текст: ")
split_text = text.split()
large_words = ""
medium_words = ""
small_words = ""

while True:
    for i in range(0, len(split_text)):
        if len(split_text[i]) > 7:
            large_words += split_text[i] + ", "
        elif 3 < len(split_text[i]) < 8:
            medium_words += split_text[i] + ","
        else:
            small_words += split_text[i] + ", "
    break

print(large_words)
print(medium_words)
print(small_words)
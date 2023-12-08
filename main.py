import sys

file = open("textFile.txt", encoding="utf-8")
readed_file = file.read()

if len(readed_file) == 0:
    print("Файл порожній, програму зупинено!")
    sys.exit()

text_by_lines = readed_file.split("\n")
print("Пробіл, вважається за символ!\n")
for i in range(len(text_by_lines)):
    line = text_by_lines[i]
    words_in_line = len(line.split())
    symbols_in_line = len(line)
    spaces_count = line.count(' ')
    n = i + 1
    print("У рядку " + str(n) + " - " + str(words_in_line) + " слів, " + str(
        symbols_in_line) + " символів," + " з них " + str(spaces_count) + " пробілів.")

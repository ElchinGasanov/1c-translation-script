import re
import sys
from datetime import datetime
start_time = datetime.now()

filedict = 'dict.txt'
dict_ru_en = list()

params = sys.argv
print(len(params))
if len(params) == 2:
    filename = params[1]
    filename_en = filename

elif len(params) == 3:
    filename = params[1]
    filename_en = params[2]

else:
    filename = 'Module.bsl'
    filename_en = 'Module-en.bsl'

print(f"Исходный файл: {filename}")
print(f"Файл результата: {filename_en}")

# DICT
with open(filedict, "r", encoding="utf-8") as f:
    for line in f.readlines():
        if (line.startswith("#") or line == ""):
            continue
        params = re.findall(r"^(\w+) - (\w+)$", line)
        dict_ru_en.append(params)

# TRANSLATE
with open(filename, "r", encoding="utf-8") as f:
    text = f.read()

count = 0
with open(filename_en, "w", encoding="utf-8") as f:
    for reg in dict_ru_en:
        ru = reg[0][0]
        en = reg[0][1]
        pattern = fr"\b{ru}\b"
        text = re.sub(pattern, en, text)

    f.write(text)

time = datetime.now() - start_time
print(f"Done! Time: {time}")


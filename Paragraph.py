import re

filename = "文心雕龙双语版.txt"
f = open(filename, "r", encoding='utf-8')

titles = []  # 存放标题
no_use_rows = 4

# 跳过前几行
for i in range(no_use_rows):
    line = f.readline()

while line:
    line = f.readline()
    if len(titles) == 50:
        break
    if line != '\n':
        line = line[:-1]
        titles.append(line)

f.close()

fbi = open("文心雕龙双语版.txt", "r", encoding='utf-8')
fwen = open("文心雕龙原文.txt", "a", encoding='utf-8')
fbai = open("文心雕龙译文.txt", "a", encoding='utf-8')

#从正文部分开始
for i in range(140):
    line = fbi.readline()

chapter = 1

while True:
    #line指向每个章节的标题
    if chapter == 50:
        break

    fbai.write(titles[chapter - 1] + '\n')
    chapter += 1

    while re.match("【译文】", line) is None:
        if line != '\n':
            fwen.write(line)
        line = fbi.readline()
    line = fbi.readline()
    while re.match(titles[chapter-1], line) is None:
        if line != '\n':
            fbai.write(line)
        line = fbi.readline()

    fwen.write('\n')
    fbai.write('\n')

#最后一章单独处理
while True:
    if not line:
        break
    while re.match("【译文】", line) is None:
        if line != '\n':
            fwen.write(line)
        line = fbi.readline()
    fwen.write('\n')
    line = fbi.readline()
    fbai.write(titles[chapter - 1] + '\n')
    while line:
        if line != '\n':
            fbai.write(line)
        line = fbi.readline()
    fbai.write('\n')

fbi.close()
fwen.close()
fbai.close()


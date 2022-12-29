import re

#分别打开原文和译文
fwen = open("文心雕龙原文.txt", "r", encoding="utf-8")
fbai = open("文心雕龙译文.txt", "r", encoding="utf-8")

#存储句对齐结果
fwen_s = open("文心雕龙原文句子.txt", "a", encoding="utf-8")
fbai_s = open("文心雕龙译文句子.txt", "a", encoding="utf-8")

while True:
    line1 = fwen.readline()
    line2 = fbai.readline()
    if not line1 or not line2:
        break

    sen1 = re.split(r'([？。！])', line1)
    sen2 = re.split(r'([？。！])', line2)

    sen1.append("")
    sen1 = ["".join(i) for i in zip(sen1[0::2], sen1[1::2])]
    sen2.append("")
    sen2 = ["".join(i) for i in zip(sen2[0::2], sen2[1::2])]

    length1 = len(sen1)
    length2 = len(sen2)
    length = min(length1, length2)

    for i in range(length):
        fwen_s.write(sen1[i] + '\n')
        fbai_s.write(sen2[i] + '\n')

fwen.close()
fbai.close()
fwen_s.close()
fbai_s.close()




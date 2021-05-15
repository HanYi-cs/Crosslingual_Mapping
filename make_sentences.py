import csv
import jieba
import MeCab
mecab = MeCab.Tagger ("-Owakati")
num_files = 2  # wiki文件个数
language = 'zh'  # 语言选择

if language == 'ja':

        with open('异意单词表.csv', 'r', encoding='utf-8-sig')as e, open('异意日文例句合集.csv', 'w', encoding='utf-8-sig', newline='')as g:
            reader2 = csv.reader(e)
            writer = csv.writer(g)
            for idx2, line2 in enumerate(reader2):  # 对于每一个单词
                print(line2[1])
                sentence = [line2[1]]
                for i in range(num_files):
                    with open('jawiki' + str(i) + '.csv', 'r', encoding='utf-8-sig')as f:
                        reader1 = csv.reader(f)
                        for idx1, line1 in enumerate(reader1):  # 搜索所有例句
                            for word in mecab.parse(line1[0]).split(' '):
                                if line2[1] == word:
                                    if line1[0] not in sentence:
                                        sentence.append(line1[0])
                                        break
                    reader1 = csv.reader(open('jawiki' + str(i) + '.csv', 'r', encoding='utf-8-sig'))
                writer.writerow(sentence)

if language == 'zh':

        with open('异意单词表.csv', 'r', encoding='utf-8-sig')as e, open('异意中文例句合集.csv', 'w', encoding='utf-8-sig', newline='')as g:
            reader2 = csv.reader(e)
            writer = csv.writer(g)
            for idx2, line2 in enumerate(reader2):  # 对于每一个单词
                print(line2[0])
                sentence = [line2[0]]
                for i in range(num_files):
                    with open('zhwiki' + str(i) + '.csv', 'r', encoding='utf-8-sig')as f:
                        reader1 = csv.reader(f)
                        for idx1, line1 in enumerate(reader1):  # 搜索所有例句
                            for word in jieba.cut(line1[0]):
                                if line2[0] == word:
                                    if line1[0] not in sentence:
                                        sentence.append(line1[0])
                                        break
                    reader1 = csv.reader(open('zhwiki' + str(i) + '.csv', 'r', encoding='utf-8-sig'))
                writer.writerow(sentence)







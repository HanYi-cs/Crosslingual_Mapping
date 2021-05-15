import csv


def _cut(sentence):
    new_sentence = []
    sen = []
    for i in sentence:
        if i in ['。', '！', '？', '?', '，','。','、'] and len(sen) != 0:
            sen.append(i)
            new_sentence.append("".join(sen))  # ['虽然BillRoper正...接近。' , '与父母，...之首。' , ]
            sen = []
            continue
        sen.append(i)  # sen=['虽', '然', 'B', 'i', 'l', 'l', 'R', 'o', 'p', 'e', 'r', '正']

    if len(new_sentence) <= 1:  # 一句话超过max_seq_length且没有句号的，用","分割，再长的不考虑了。
        new_sentence = []
        sen = []
        for i in sentence:
            if i.split(' ')[0] in ['，', ','] and len(sen) != 0:
                sen.append(i)
                new_sentence.append("".join(sen))
                sen = []
                continue
            sen.append(i)

    if len(sen) > 0:  # 若最后一句话无结尾标点，则加入这句话
        new_sentence.append("".join(sen))
    return new_sentence

num_files = 2
for i in range(2):
    with open(str(i)+'.txt', 'r', encoding='utf-8-sig')as f, open('wiki'+str(i)+'.csv', 'w', encoding='utf-8-sig', newline = '')as e:
        reader = csv.reader(f)
        writer = csv.writer(e)
        for idx, line in enumerate(reader):
            if len(line) >= 1:
                sentence1 = _cut(''.join(line))
            for j in sentence1:
                if len(j) >= 8:
                    writer.writerow([j])





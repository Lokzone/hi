# 打開檔案
# 读取里面包含good字串的段落
import os 

data = []
i = 0
with open('053 reviews.txt','r') as filename:
    for line in filename:
        data.append(line)
        i +=1
        if i % 10000 == 0:
            print(len(data))

print('文档总共有：',len(data),'条信息')

new = []
for line in data:
    if 'good' in line:
       new.append(line)
print('其中包含good字符串的有：',len(new),'条信息')

sum_len = 0
for d in data:
    sum_len += len(d)

print('文档总共有： ', sum_len, '个字')
print('文档平均长度: ',sum_len / len(data),'个字')

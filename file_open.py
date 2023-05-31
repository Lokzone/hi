# 读取档案
data = []
with open('053 reviews.txt','r') as f:
	for line in f:
		data.append(line.strip())

new = []
for d in data:
	if len(d) < 100:
		new.append(d)
		print(len(new))
print(new[0])

good = []

for d in data:
	if 'good' in d:
		good.append(d)

print(len(good))
print(len(good[0]))
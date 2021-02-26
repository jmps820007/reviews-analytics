data = []
count = 0

with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
total = len(data)
print('檔案讀取完了,總共有', len(data), '筆資料')


print(len(data))     #印出data串列的--項目數量
print(len(data[2]))  #印出data串列項目1的--字元數量
print(data[2])

sum_len = 0

for d in data:
    sum_len += len(d)

print(sum_len)  #data串列的總字元數

avg = 0

avg = sum_len / count
print(avg)
#for d in data:
#    sum_len += len(d)
#print(sum_len)
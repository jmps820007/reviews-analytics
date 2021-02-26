data = []  ##用來裝reviews.txt的留言
count = 0  ##計數目前檔案讀取到第幾筆

with open('reviews.txt', 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0:
            print(len(data))
total = len(data)
print('檔案讀取完了,總共有', len(data), '筆資料')


print(len(data))     #印出data串列的--項目數量
print(len(data[0]))  #印出data串列第一個項目的--字元數量
print(data[0])

sum_len = 0

for d in data:
    sum_len += len(d)

print(sum_len)  #data串列的總字元數

print("留言平均長度為", sum_len / count)

new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '比留言長度小於100')
print(new[0])
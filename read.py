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

##印出字數小於100的留言
new = []
for d in data:
    if len(d) < 100:
        new.append(d)
print('一共有', len(new), '比留言長度小於100')
print(new[0])

##印出提到good的留言
good = []
for d in data:
    if 'good' in d:  #d裡面是否有'good'字串
        good.append(d)
print('一共有', len(good), '提到good')
print(good[0])

####################
#清單快寫法1
good = [d for d in data if 'good' in d]  #[|d運算| for |d變數| in |data清單| |if 'good' in d篩選條件|]
print(good)

####################
#清單快寫法2
bad = ['bad' in d for d in data]  #[|d運算| for |d變數| in |data清單|]
print(bad)

#普通寫法
bad = []
for d in data:
    bad.append('bad' in d)

print(bad)
data = []
count = 0
with open ('reviews.txt' , 'r') as f:
    for line in f:
        data.append(line)
        count += 1
        if count % 1000 == 0: # %是用來求餘數
            print(len(data))
print( '檔案讀取完了，總過有', len(data) , '筆資料' )


sum_len = 0
for d in data:
    sum_len = sum_len + len(d)
print( '平均是' , sum_len/len(data) ) #每一筆留言的長度 / 總長

new = [] #建立一個新的清單叫做new
for d in data: #data裡面的每一行d
    if len(d) < 100: #如果d小於100個字
        new.append(d) #把那個d加到new清單裡面
print('一共有' , len(new) , '筆留言長度小於100')
print(new[0])
print(new[1])
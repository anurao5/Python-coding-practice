
n = int(input().strip())
str_binary = bin(n).strip('0b')

count = 0
count_arr = []

#Calculate the maximum number of consecutive 1s
for i in range(len(str_binary)):
    if str_binary[i] == '1':
        count += 1
    else:
        if count != 0:
            count_arr.append(count)
            count = 0
        continue
if count != 0:
   count_arr.append(count)
else:
    count_arr.append(0)

print(max(count_arr))

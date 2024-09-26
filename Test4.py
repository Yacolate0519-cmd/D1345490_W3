value = int(input("請輸入一個三位數:"))
value1 = list(str(value))
sum = 0
for i in value1:
    sum  += int(i)
    
print(sum)

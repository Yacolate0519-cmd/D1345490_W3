value = int(input("輸入三位數字:"))

check = bool(value % 2 == 0)

key = ("奇數","偶數")[check]

print(key)


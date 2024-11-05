# 要求： 顺序并且居中对齐输出一下内容
# 1.  center: 返回一个源字符串居中， 并使用空格填充至长度width的新字符串
poem = ["登鹳雀楼",
        "王之涣",
        "白日依山尽",
        "黄河入海流",
        "欲穷千里目",
        "更上一层楼"]

for peom_str in poem:
    print(peom_str.center(10))

for peom_str in poem:
    print(peom_str.center(10, '*'))
# 2. ljust: 返回一个原字符串左对齐， 并使用指定字符填充至长度width的新字符串
for peom_str in poem:
    print(peom_str.ljust(10, '@'))
# 3. ljust: 返回一个原字符串右对齐， 并使用指定字符填充至长度width的新字符串
for peom_str in poem:
    print(peom_str.rjust(10, '%'))



print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""")

print('\1'
      '2')
# 1
text = ('Put several strings within parentheses '
        'to have them joined together.\n')
print(text)
# 2
print(text[42:], '123')
# 3
a = """jia
jiajia"""

b = '''jia
ni'''
print(a, len(a))
print(b, len(b))
# 4.
a = "dfdsf" "ccc"
print(a)
print('===')
a = ('1', '2')
b = 'str'.join(a)
print(b)


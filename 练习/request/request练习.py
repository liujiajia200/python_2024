import requests

response = requests.get('http://www.baidu.com')
# print(response.url)
# print(f'request header: {response.request.headers}')
# print(f'response header: {response.headers}')
# print(f'编码格式：{response.apparent_encoding}')  # 如果响应是图片的话 这里返回none
# print(response.status_code)

# 0. 直接打印会乱码
# print(response.text)  # 有乱码

# 1. 解码打印
# print(response.content.decode())  # 解码后就没有乱码了

# 2. 设置编码格式
# response.encoding = 'utf-8'
# print(response.text)

url = 'https://k.sinaimg.cn/n/sinakd20230923s/100/w900h1600/20230923/9a05-ec59abd25465a24d180dfa0fac5a66f5.jpg/w700d1q75cms.jpg'  # 图片
res = requests.get(url)
# 3. 保存响应
# with open('2.jpg', 'wb') as f:
#     f.write(res.content)

# 4. response.text和response.content的区别
#     text: str类型， request模块自动根据http头部对响应的编码做出有根据的推测
#     content： bytes类型， 可以通过decode()解码

# 5. 用户代理
res1 = requests.get('http://www.baidu.com')
print(len(res1.content.decode()))  # 比较少




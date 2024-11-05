
import requests

# 百度首页代码爬出来的比较少
# 请求头中user-agent字段必不可少， 它表示客户端的操作系统以及浏览器的信息
# 构建请求头 （伪装成正常的用户）
headers = {
    #headers必须是字典形式的
    # user-agent去百度网页-》f12 -》network-》request header里找
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36'
}
res2 = requests.get('http://www.baidu.com', headers=headers)
# print(res2.content.decode()
print(res2.request.headers)
print(len(res2.content.decode()))  # 412589

# 添加user-agent的目的是为了让服务器认为是浏览器在发送请求， 而不是爬虫程序在发送请求


# 有的时候虽然带上了user-agent,但是发送太多次，服务器还会认为这是爬虫程序。所以一下方法防止反爬
# 1. user-agent池  -- 防止反爬
# （1）. 构建user-agent池
import random

ualist = [
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36',
    'Mozilla/5.0 (iPhone; CPU iPhone OS 16_6 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.6 Mobile/15E148 Safari/604.1',
    'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36',
    'Mozilla/5.0 (Linux; Android 13; Pixel 7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Mobile Safari/537.36'
]
# print(random.choice(ualist))


#（2）. 引入fake_useragent库  可能会出现异常
from fake_useragent import UserAgent

print(UserAgent().random)


# 2. 浏览器发送请求原理
# 构建请求
# 查找缓存
# 准备ip地址和端口
# 等待tcp队列（超过6个就要等待）
# 建立tcp连接
# 发送http请求

# 浏览器回想服务器发送请求行， 包括了请求方法， 请求url， http协议
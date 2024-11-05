def measure():
    print("测量开始。。。")
    temp = 39
    wetness = 50
    print("测量结束")

    return temp, wetness

result = measure()
print(result)

print('*'*50)

temp, wetness = measure()
print(temp)
print(wetness)


print('1.#'*50)
def demo(num, num_list):
    print("函数内部")
    #复制语句
    num=200
    num_list=[1,2,3]
    print(num)
    print(num_list)

    print("函数代码完成")

gl_num = 99
gl_list=[4,5,6]
demo(gl_num, gl_list)
print(gl_num)
print(gl_list)


print("2^"*50)
def mutable(num_list):
    # num_list = [1,2,3]
    num_list.extend([1,2,3])
    print(num_list)

gl_list = [6,7,8]
mutable(gl_list)
print(gl_list)



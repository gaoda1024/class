# 面向对象和面向过程：
## 面向对象：

class group:

    __names = ["zhangsan","lisi","wangwu"]

    def show(this):
        print(this.__names)
        return 1

g = group()

g.show()


## 面向过程：
# group = ["zhangsan","lisi","wangwu"]

# print(group)
# 函数和方法

# 私有属性

# 类与实例

# 构造方法

import datetime
current_time = datetime.datetime.now()
print("当前时间：", str(current_time).split('-')[0])
year_now = str(current_time).split('-')[0]

a = "1123"
print((a=='1123'))



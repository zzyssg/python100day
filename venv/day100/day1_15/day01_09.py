"""
day01   turple、import
day02   变量、类型
day03   分支：if、else、elif
day04   循环：for in、while、print()打印完之后，鼠标向后移
day05   一些算法
day06   定义函数、导入模块的函数（仅仅导入函数时，后面的同名函数会覆盖前面的函数）
        导入的模块中，除了定义的函数以外还有其他可执行代码，python解释器会在导入模块时就执行这些代码，
        所以需要将执行代码放入到一个条件中：除非运行该模块，否则if条件下的代码不会执行直接执行的模块的
        名字才是：__main__
        变量：global关键字可以将一个变量定义为一个全局变量，但仅限于在一个模块（py文件）中。与其他文件隔离。
day07   字符串、列表、生成式和生成器（不占用存储数据的空间，需要时运算得到）、
        元组（元素无法修改）
        集合（不许重复元素，可进行交并差运算）
        字典（key:val)
day08   面向对象：定义类class、属性和方法的访问权限（公开、私有）
day09   @property装饰器（访问器） @setter(修改器，不能单独使用）
        slots——【python的实例可以动态的添加实例方法或者实例属性，slots可以添加白名单】
        静态方法：类可以使用类方式
        类方法：可以利用其参数创建返回类的对象
        类与类之间的关系：is-a（继承、泛化）、has-a（关联，体现为另一个类的全局/成员变量）、use-a（依赖，方法中用到了）
        UML：统一建模语言，使用各种类型的线、箭头、图形。
        继承：
        多态：继承、重写、父类引用指向子类对象。
"""


"""
day04 循环
"""
import  sys
# row = int(input())
# 打印row行
# for i in range(row):
#     for j in range(row):
#         if j < row - 1 - i:
#             print(' ',end='')
#         else:
#             print('*',end='')
#     print()
# max_len = 2 * row - 1
# for i in range(row):
#     for j in range(max_len):
#         if row - 1 - (i) <= j <= row - 1 + i:
#             print('*',end='')
#         else:
#             print(' ',end='')
#     print()

# print() is different from '='
# for i in range(row):
#     for j in range(row - 1 - i):
#         print(' ',end='')
#     for j in range(2 * i + 1):
#         print('*',end='')
#     print()
# for i in range(row):
#     print(' ',end='')
# for i in range(row):
#     print('*',end='')
f = [x for x in range(1,1000)]
print(sys.getsizeof(f))
print(f)

f = (x ** 2 for x in range(1,1000))
print(sys.getsizeof(f))
print(f)
for val in f:
    print(val)
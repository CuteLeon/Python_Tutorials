# Python_Tutorials

Python 是一门流行的编程语言。它由 Guido van Rossum 创建，于 1991 年发布。

- Python 是为可读性设计的，与英语有一些相似之处，并受到数学的影响。
- Python 使用新行来完成命令，而不像通常使用分号或括号的其他编程语言。
- Python 依赖缩进，使用空格来定义范围；例如循环、函数和类的范围。其他编程语言通常使用花括号来实现此目的。

# Python 入门

## Python 安装

检查是否安装了Python及对应版本
> 下载地址：https://www.python.org/

``` shell
python --version
```

## 通过命令行运行Python脚本

```
python helloworld.py
```

## 通过命令行运行Python语句

```
python
print("Hello world.")
1+1
exit()
```

# Python 语法

## 缩进

- Python 使用缩进来指示代码块
- 至少使用一个空格来表明缩进
- 同一代码块的语句必须使用相同的空格数量

```
if 5 > 2:
	print("5 is greater than 2.")
```

## 变量

Python 没有声明变量的语句，变量会在赋值时被创建

```
x = 5
y = "Hello world."
```

## 注释

使用 `#` 符号标记注释

### 多行注释

未分配给变量的字符串文字将会被忽略，因此可以使用多行字符串实现多行注释
```
"""
这里面是
多行注释
"""
print("Hello world.")
```

# Python 变量

变量是存放数据的容器，Python会在首次为变量赋值时创建变量

## 变量命名规则

- 变量名必须以字母或下划线字符开头
- 变量名称不能以数字开头
- 变量名只能包含字母数字字符和下划线（A-z、0-9 和 _）
- ==变量名称区分大小写==（age、Age 和 AGE 是三个不同的变量）

## 向多个变量赋值

```
x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange"
a, b = b, a
```

## 全局变量

在函数外部创建的变量称为全局变量
全局变量可以被函数内部和外部的每个成员使用
如果在函数内部创建具有相同名称的变量，则该变量将是局部变量，只能在函数内部使用，且被优先使用。

```
x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()
```

## global 关键字

通常，在函数内部创建变量时，该变量是局部变量，只能在该函数内部使用。
要在函数内部创建全局变量，您可以使用 global 关键字。

```
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```

另外，如果要在函数内部更改全局变量，请使用 global 关键字。

```
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```

# 数据类型

## 获取数据类型

type() 获取变量的数据类型

```
x = 10
print(type(x))
```

## 检查数据类型

```
x = 200
isinstance(x, int)
```

## 设置数据类型

|类型|分类|示例|
|---|---|---|
|str|文本类型|x = "Hello World"<br>x = str("Hello World")|
|int|数值类型|x = 29<br>x = int(29)|
|float|数值类型|x = 29.5<br>x = float(29.5)|
|complex|数值类型|x = 1j<br>x = complex(1j)|
|list|序列类型|x = ["apple", "banana", "cherry"]<br>x = list(("apple", "banana", "cherry"))|
|tuple|序列类型|x = ("apple", "banana", "cherry")<br>x = tuple(("apple", "banana", "cherry"))|
|range|序列类型|x = range(6)|
|dict|映射类型|x = {"name" : "Bill", "age" : 63}<br>x = dict(name="Bill", age=36)|
|set|集合类型|x = {"apple", "banana", "cherry"}<br>x = set(("apple", "banana", "cherry"))|
|frozenset|集合类型|x = frozenset({"apple", "banana", "cherry"})|
|bool|布尔类型|x = True<br>x = bool(5)|
|bytes|二进制类型|x = b"Hello"<br>x = bytes(5)|
|bytearray|二进制类型|x = bytearray(5)|
|memoryview|二进制类型|x = memoryview(bytes(5))|

## 数字

- int: 正负整数，长度不限
- float: 正负小数，E表示科学计数法
- complex: 复数，j表示虚部

### 随机数

```
import random
print(random.randrange(1, 10))
```

## 字符串

- 任意选择使用双引号或单引号
- 使用三个引号表示多行字符串
- 本质是字节数组
- 单个字符就是长度为1的字符串

### 裁切

```
a = "Hello, world!"
# H
a[0]
a[-1]
# ello
a[1:5]
# orl
# 负号表示从尾部倒数
a[-5:-2]
```

### 字符串长度

```
a = "Hello, World!"
print(len(a))
```

### 字符串方法

```
a = " hello, World! "

# 删除字符串左右的特定字符，默认为空格字符
a.strip()
a.strip(" ._#")
a.lstrip()
a.lstrip(" ._#")
a.rstrip()
a.rstrip(" ._#")

# 返回小写的字符串
a.lower()
a.casefold()

# 返回大写的字符串
a.upper()

# 反转大小写
a.swapcase()

# 替换字符串内容，可选替换的次数，默认为全部替换
a.replace("World", "Kitty")
a.replace("World", "Kitty", 1)

# 分割字符串，可以控制分割的次数和开始的方向
a.split(",")
a.split(",", 2)
a.rsplit(",", 2)

# 按换行符分割字符串，控制分割后是否保留换行符，默认不保留
a.splitlines()
a.splitlines(true)

# 按特定字符串分割并返回分隔符及其前后共计三个部分
# ["He", "l", "lo!"]
"Hello!".partition("l")
# ["Hel", "l", "o!"]
"Hello!".rpartition("l")

# 首字母转换为大写
a.capitalize()

# 转换为标题格式，即每个单词的首字母大写

# 检查是否为标题规则，即每个字母都是首字母大写
"Hello, World! You Are Welcome.".istitle()

# 检查所有字母都是大写或小写，允许包含符号数字等
a.islower()
a.isupper()

# 将字符串在固定长度的字符串中对齐，并使用特定字符串填充前后位置
a.center(30)
a.center(30, "$")
a.ljust(30)
a.ljust(30, "$")
a.rjust(30)
a.rjust(30, "$")

# 用0填充字符串左侧
a.zfill(30)
a.rjust(30, "0")

# 子字符串在字符串或其特定区间中出现的次数
a.count("l")
a.count("l", 3, 10)

# 使用特定编码对字符串编码，默认UTF-8
# 使用参数声明如何处理无法编码的字符
a.encode()
a.encode("ascii", "strict")

# 检查字符串或其区间是否以某字符开头或结尾
a.startswith("H")
a.startswith("H", -10, -2)
a.endswith("!")
a.endswith("!", -10, -2)

# 设置字符串的每个\t的空格数量，默认为8
"Hello\tWorld!".expandtabs(2)

# 查找子字符串并返回其位置，r表示从右侧开始查找
# 找不到子字符串时，find()将会返回异常，而index()将会抛出异常
a.find("ll")
a.find("ll", 0, -1)
a.rfind("ll")
a.rfind("ll", 0, -1)
a.index("ll")
a.index("ll", 0, -1)
a.rindex("ll")
a.rindex("ll", 0, -1)

# 检查所有字符都是字母或数字
a.isalnum()

# 检查所有字符都是数字
a.isdecimal() # [0-9]+
a.isdigit() # [0-9]+, ²
a.isnumeric() # [0-9]+, ⅓

# 检查字符串为有效标识符，仅包含字母数字和下划线，且不以数字为开头
a.isidentifier() # [a-zA-Z_]+[_a-z0-9A-Z]

# 检查是否不包含非打印的回车或换行等字符
a.isprintable()

# 检查字符串是否仅由空格组成
"     ".isspace()

# 合并字符串集合
"@".join(["A", "B", "C"])

```

### 检查字符串

```
txt = "Hello world."
x = "llo" not in txt
print(x)
```

### 合并字符串

```
a = "Hello"
b = "World"
c = a + " " + b
print(c)
```

### 格式化字符串

字符串中使用`{}`或`{\d+}`或`{.+}`作为占位符
占位符内的数字或名称调整参数出现的位置
实际传入的参数数量只允许等于或多余占位符的数量

```
quantity = 3
itemno = 567
price = 49.95

"I want {} pieces of item {} for {} dollars.".format(quantity, itemno, price)
"I want to pay {2} dollars for {0} pieces of item {1}.".format(quantity, itemno, price)
"I want to pay {price} dollars for {quantity} pieces of item {itemIndex}".format(price = price, quantity = quantity, itemIndex = itemno)

# 扩展占位符并对齐数据
"{:8}".format("Hello")
"{:<8}".format("Hello")
"{:>8}".format("Hello")
"{:^8}".format("Hello")

# 扩充数字占位符，但将符号放置在占位符左端
"{:=8}".format(100)
"{:=8}".format(-100)

# 默认正负数格式，仅在负数前增加一个减号
"{:}".format(100)
"{:}".format(-100)
"{:-}".format(100)
"{:-}".format(-100)

# 在正数前面加一个空格，以对齐可能的负数前的减号
"{: }".format(100)
"{: }".format(-100)

# 在正数前面加一个加号，以对齐可能的负数前的减号
"{:+}".format(100)
"{:+}".format(-100)

# 百分比格式
"{:%}".format(0.95123)

# 二进制
"{:b}".format(4237463254)

# 十六进制
"{:x}".format(4237463254)
"{:X}".format(4237463254)

# 小数精度格式
"{:.4f}".format(0.95346)

# 千分位
"{:,}".format(237846324692342374)
"{:_}".format(237846324692342374)
```

## 布尔值

- True 或 False
- 常量
    - ~~bool(None)~~
	- ~~bool(Flase)~~
	- bool(True)
- 字符串：""==False，其余均为True
    - ~~bool("")~~
	- bool("Hello")
- 数字：0==False，其余均为True
    - ~~bool(0)~~
	- bool(100)
	- bool(-100)
- 集合: []==False，其余均为True
    - ~~bool([])~~
	- ~~bool(())~~
	- ~~bool({})~~
	- bool([1])
	- bool((1))
	- bool({1})

如果对象带有 def __len__(self) 方法且返回0或False，强制转换该对象为bool()时将会返回False

# 运算符

## 算术运算符
|符号|说明|示例|
|---|---|---|
|+|加|x + y|
|-|减|x - y|
|*|乘|x * y|
|/|除|x * y|
|%|取模|x % y|
|**|幂|x ** y|
|//|地板除(取整除)|x // y|

## 赋值运算符

|符号|说明|示例|
|---|---|---|
|=|x = 5|x = 5|
|+=|x += 3|x = x + 3|
|-=|x -= 3|x = x - 3|
|*=|x *= 3|x = x * 3|
|/=|x /= 3|x = x / 3|
|%=|x %= 3|x = x % 3|
|//=|x //= 3|x = x // 3|
|**=|x **= 3|x = x ** 3|
|&=|x &= 3|x = x & 3|
|\|=|x \|= 3|x = x \| 3|
|^=|x ^= 3|x = x ^ 3|
|>>=|x >>= 3|x = x >> 3|
|<<=|x <<= 3|x = x << 3|

## 比较运算符
|符号|说明|示例|
|---|---|---|
|==|等于|x == y|
|!=|不等于|x != y|
|>|大于|x > y|
|<|小于|x < y|
|>=|大于或等于|x >= y|
|<=|小于或等于|x <= y|

## 逻辑运算符

|符号|说明|示例|
|---|---|---|
|and|如果两个语句都为真，则返回 True。|x > 3 and x < 10|
|or|如果其中一个语句为真，则返回 True。|x > 3 or x < 4|
|not|反转结果，如果结果为 true，则返回 False|not(x > 3 and x < 10)|

## 身份运算符

|符号|说明|示例|
|---|---|---|
|is|如果两个变量是同一个对象，则返回 true。|x is y|
|is not|如果两个变量不是同一个对象，则返回 true。|x is not y|

## 成员运算符

|符号|说明|示例|
|---|---|---|
|in|如果对象中存在具有指定值的序列，则返回 True。|x in y|
|not in|如果对象中不存在具有指定值的序列，则返回 True。|x not in y|

## 位运算符

|符号|说明|示例|
|---|---|---|
|&|AND|如果两个位均为 1，则将每个位设为 1。|
|\||OR|如果两位中的一位为 1，则将每个位设为 1。|
|^|XOR|如果两个位中只有一位为 1，则将每个位设为 1。|
|~|NOT|反转所有位。|
|<<|Zero fill left shift|通过从右侧推入零来向左移动，推掉最左边的位。|
|>>|Signed right shift|通过从左侧推入最左边的位的副本向右移动，推掉最右边的位。|

# 集合类型

- 列表（List）是一种有序和可更改的集合。允许重复的成员。
- 元组（Tuple）是一种有序且不可更改的集合。允许重复的成员。
- 集合（Set）是一个无序和无索引的集合。没有重复的成员。
- 词典（Dictionary）是一个无序，可变和有索引的集合。没有重复的成员。

## 列表 (List)

有序且可修改的集合类型

### 可以通过下标随机访问
```
mylist = ["A", "B", "C"]
print(mylist)
print(mylist[0])
print(mylist[-1])
print(mylist[1:3])

mylist[1] = 'b'
```

### 遍历集合
```
for x in mylist:
	print(x)
```

### 检查项目是否存在
```
print("a" in mylist)
print("A" in mylist)
```

### 检查元素在列表中首次出现的位置
```
# index() 方法未找到目标元素时将会抛出异常
mylist.index("C")
```

### 获取集合长度
```
len(mylist)
```

### 获取项目在列表中出现的次数
```
mylist = [1,1,2,2,2,3,3,4,5,4]
mylist.count(2)
```

### 向集合添加项目
```
# 在尾部追加项目
mylist.append("D")

# 在特定位置插入项目
mylist.insert(2, "b")
```

### 删除项目
```
# 按值删除
mylist.remove("A")

# 返回并删除特定位置的元素，默认为-1，即最后一个元素
mylist.pop()
mylist.pop(-1)
mylist.pop(0)

# 清空集合
mylist.clear()
```

### del 关键字销毁集合
```
# 按索引删除
del mylist[0]
# 销毁整个集合，之后不可再访问
del mylist
```

### 复制集合
```
list1 = [1,2,3]
# 访问引用
list2 = list1
# 深度复制
list2 = list1.copy()
list2 = list(list1)
```

### 合并两个集合
```
list1 = [1,2,3]
list2 = ['a','b','c']
list3 = list1 + list2

list1.extend(list2)
list1 = list(list1 + list2)
list1 = (list1 + list2).copy()
```

### 反转列表
```
list1.reverse()
```

### 列表排序
```
list1.sort()
```

## 元组 (Tuple)

元组是有序且不可更改的集合，用圆括号编写。

```
mytuple = ("A", "B", "C")
print(mytuple)
```

### 通过索引访问元组项目
```
mytuple[0]
mytuple[-1]
mytuple[1:3]
```

### 更改元组值

创建元组后，您将无法更改其值。元组是不可变的，或者也称为恒定的。
但是有一种解决方法。您可以将元组转换为列表，更改列表，然后将列表转换回元组。

```
mytuple = ("apple", "banana", "cherry")
mylist = list(mytuple)
mylist[1] = "kiwi"
mytuple = tuple(mylist)
```

### 遍历集合
```
for x in mytuple:
	print(x)
```

### 检查项目是否存在
```
print("a" in mytuple)
print("A" in mytuple)
```

### 获取集合长度
```
len(mytuple)
```

### del 关键字销毁集合
```
# 销毁整个集合，之后不可再访问
del mytuple
```

### 合并两个集合
```
tuple1 = (1,2,3)
tuple2 = ('a','b','c')
tuple3 = tuple1 + tuple2
```

### 获取项目在列表中出现的次数
```
mylist = [1,1,2,2,2,3,3,4,5,4]
mylist.count(2)
```

### 检查元素在列表中首次出现的位置
```
# index() 方法未找到目标元素时将会抛出异常
mylist.index("C")
```

## 集 (Set)

集合是无序和无索引的集合，用花括号编写。

### 遍历集合
```
for x in myset:
	print(x)
```

### 检查项目是否存在
```
print("a" in myset)
print("A" in myset)
```

### 向集合添加项目
```
# 添加一个项目
myset.add("D")

# 批量添加多个项目
myset.update(["D", "E", "F"])
```

### 获取集合长度
```
len(myset)
```

### 删除项目
```
# remove() 删除不存在的项目将会抛出异常，discard() 不会
myset.discard("A")
myset.remove("A")

# 返回并删除一个元素，set是无序的，因此无法确定被删除的项目
myset.pop()

# 清空集合
myset.clear()
```

### del 关键字销毁集合
```
# 销毁整个集合，之后不可再访问
del myset
```

### 合并两个集合
```
set1 = {1,2,3}
set2 = {'a','b','c'}
set3 = set1.union(set2)
```

### 复制集合
```
set1 = {1,2,3}
# 访问引用
set2 = set1
# 深度复制
set2 = set1.copy()
set2 = set(set1)
```

### 获取此集合中不存在于另一个集合的项目
```
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
z = x.difference(y) 
```

### 删除此集合中也存在于另一个集合的项目
```
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.difference_update(y) 
```

### 获取此集合与其它集合的交集
```
# 存在于所有集合的项目
x = {"apple", "banana", "cherry"}
y1 = {"google", "banana", "apple"}
y2 = {"cherry", "microsoft", "apple"}
z = x.intersection(y1, y2)
```

### 删除此集合中不存在于另一个集合的项目
```
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.intersection_update(y)
```

### 判断集合是否存在交集
```
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "facebook"}
z = x.isdisjoint(y) 
```

### 判断集合是否为另一个集合的子集
```
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}
z = x.issubset(y) 
```

### 判断集合是否为另一个集合的超集
```
x = {"f", "e", "d", "c", "b", "a"}
y = {"a", "b", "c"}
z = x.issuperset(y) 
```

### 获取两个集合的对称差集
```
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
# 返回的集合排除了两个集合中同时存在的项
z = x.symmetric_difference(y)
```

### 更新集合为两个集合的对称差集
```
x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}
x.symmetric_difference_update(y) 
```

## 字典 (Dictionary)

字典是一个无序、可变和有索引的集合，用花括号编写，拥有键和值。

```
mydict =	{
  "brand": "Porsche",
  "model": "911",
  "year": 1963
}
```

### 读取项目

```
x = mydict["brand"]
x = mydict.get("brand")
```

### 写入项目

```
mydict["brand"] = "Leon"
mydict.update({"brand":"Leon"})

# 如果目标Key不存在，则插入默认值
mydict.setdefault("Brand", "Default Name")
```

### 删除项目

~~popitem() 方法删除最后插入的项目（在 3.7 之前的版本中，删除随机项目）~~

```
mydict.pop("Brand")

# 清空集合
mydict.clear()
```

### 遍历集合

```
# 遍历 key
for key in mydict:
	print("{} : {}".format(key, mydict[key]))
for key in mydict.keys():
	print("{} : {}".format(key, mydict[key]))

# 遍历 value
for value in mydict.values():
	print(value)

# 遍历 key-value pair
for key, value in mydict.items():
	print("{} : {}".format(key, value))
```

### 检查项目是否存在
```
print("Brand" in mydict)
print("brand" in mydict)
```

### 获取集合长度
```
len(mydict)
```

### del 关键字销毁集合
```
# 按Key删除
del mydict["Brand"]
# 销毁整个集合，之后不可再访问
del mydict
```

### 复制集合
```
dict1 =	{
  "brand": "Porsche",
  "model": "911",
  "year": 1963
}
# 访问引用
dict2 = dict1
# 深度复制
dict2 = dict1.copy()
dict2 = dict(dict1)
```

### 嵌套字典

```
child1 = {
  "name" : "Phoebe Adele",
  "year" : 2002
}
child2 = {
  "name" : "Jennifer Katharine",
  "year" : 1996
}
child3 = {
  "name" : "Rory John",
  "year" : 1999
}

myfamily = {
  "child1" : child1,
  "child2" : child2,
  "child3" : child3
}
```

### 简单初始化

```
# 请注意，关键字不是字符串字面量
# 请注意，使用了等号而不是冒号来赋值
thisdict = dict(brand="Porsche", model="911", year=1963)
print(thisdict)

# 所有的Key
x = ('key1', 'key2', 'key3')
# 所有Key对应的Value的统一默认值
y = 0
thisdict = dict.fromkeys(x, y)
```

# 判断结构 (if...elif...else)

- 使用缩进控制结构
- 简单的if语句可以写在一行 
    - if True: print("True")
	- print("True") if True else print("Flase")
	- print("True") if True else print("Flase") if False else print("True")
- 使用 pass 关键字避免无内容的 if 语句的语法错误

# 循环结构 (while, for)

- 使用 break 关键字退出循环
- 使用 continue 关键词跳过当前迭代，继续循环
- 允许使用 else 关键字在条件不再成立时运行一次代码块
    - break 关键中断循环不会触发 else 的语句
- 使用 pass 关键字避免无内容的 if 语句的语法错误

## while 循环

只要条件为真，就可以执行一组语句。

```
while True:
	print("True")
```

## for 循环

通过使用 for 循环，我们可以为列表、元组、集合中的每个项目等执行一组语句。

### range() 函数

range() 函数返回一个数字序列，默认情况下从 0 开始，并递增 1（默认地），并以指定的数字结束。

```
# 0~9，共计 10 个数字
for x in range(10):
	print(x)

# 3~9，共计 7 个数字
for x in range(3, 10):
	print(x)

# 0~50，每次递增10，共计 6 个数字
for x in range(0, 55, 10):
	print(x)
```

# 函数

- 使用`def`定义函数，并通过函数名后加`()`调用函数。
- 参数使用`,`隔开
    - 可以在定义方法的参数时提供默认值
- 使用`return`语句返回结果
- 使用 key = value 语法发送关键字参数，顺序不重要

```
def my_function(name = "[Unknow]"):
  return "Hello from {}".format(name)

print(my_function())
print(my_function("World"))
print(my_function(name = "World"))
```

## 任意参数

通过`*`允许函数接收一个参数元组，并不关心参数真正的数量
函数定义不能为空，使用 pass 语句来避免定义无内容的函数的错误
函数允许递归调用

```
def my_function(*kids):
	for x in kids:
		print(x)
	print("The youngest child is " + kids[2])

my_function("Phoebe", "Jennifer", "Rory")
```

# Lambda

lambda 函数是一种小的匿名函数。
lambda 函数可接受任意数量的参数，但只能有一个表达式。

```
x = lambda a, b : a + b
print(x(5, 10))
```

# 数组
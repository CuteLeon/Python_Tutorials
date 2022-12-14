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

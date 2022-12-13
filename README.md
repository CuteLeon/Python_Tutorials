# Python_Tutorials

Python ��һ�����еı�����ԡ����� Guido van Rossum �������� 1991 �귢����

- Python ��Ϊ�ɶ�����Ƶģ���Ӣ����һЩ����֮�������ܵ���ѧ��Ӱ�졣
- Python ʹ��������������������ͨ��ʹ�÷ֺŻ����ŵ�����������ԡ�
- Python ����������ʹ�ÿո������巶Χ������ѭ������������ķ�Χ�������������ͨ��ʹ�û�������ʵ�ִ�Ŀ�ġ�

# Python ����

## Python ��װ

����Ƿ�װ��Python����Ӧ�汾
> ���ص�ַ��https://www.python.org/

``` shell
python --version
```

## ͨ������������Python�ű�

```
python helloworld.py
```

## ͨ������������Python���

```
python
print("Hello world.")
1+1
exit()
```

# Python �﷨

## ����

- Python ʹ��������ָʾ�����
- ����ʹ��һ���ո�����������
- ͬһ������������ʹ����ͬ�Ŀո�����

```
if 5 > 2:
	print("5 is greater than 2.")
```

## ����

Python û��������������䣬�������ڸ�ֵʱ������

```
x = 5
y = "Hello world."
```

## ע��

ʹ�� `#` ���ű��ע��

### ����ע��

δ������������ַ������ֽ��ᱻ���ԣ���˿���ʹ�ö����ַ���ʵ�ֶ���ע��
```
"""
��������
����ע��
"""
print("Hello world.")
```

# Python ����

�����Ǵ�����ݵ�������Python�����״�Ϊ������ֵʱ��������
�ַ���������������ѡ��ʹ��˫���Ż�����

## ������������

- ��������������ĸ���»����ַ���ͷ
- �������Ʋ��������ֿ�ͷ
- ������ֻ�ܰ�����ĸ�����ַ����»��ߣ�A-z��0-9 �� _��
- ==�����������ִ�Сд==��age��Age �� AGE ��������ͬ�ı�����

## ����������ֵ

```
x, y, z = "Orange", "Banana", "Cherry"
x = y = z = "Orange"
a, b = b, a
```

## ȫ�ֱ���

�ں����ⲿ�����ı�����Ϊȫ�ֱ���
ȫ�ֱ������Ա������ڲ����ⲿ��ÿ����Աʹ��
����ں����ڲ�����������ͬ���Ƶı�������ñ������Ǿֲ�������ֻ���ں����ڲ�ʹ�ã��ұ�����ʹ�á�

```
x = "awesome"
def myfunc():
  print("Python is " + x)

myfunc()
```

## global �ؼ���

ͨ�����ں����ڲ���������ʱ���ñ����Ǿֲ�������ֻ���ڸú����ڲ�ʹ�á�
Ҫ�ں����ڲ�����ȫ�ֱ�����������ʹ�� global �ؼ��֡�

```
def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```

���⣬���Ҫ�ں����ڲ�����ȫ�ֱ�������ʹ�� global �ؼ��֡�

```
x = "awesome"

def myfunc():
  global x
  x = "fantastic"

myfunc()

print("Python is " + x)
```

# ��������

## ��ȡ��������

type() ��ȡ��������������

```
x = 10
print(type(x))
```

## ������������

|����|����|����|ʾ��|
|---|---|---|---|
|str|�ı�����||x = "Hello World"<br>x = str("Hello World")|
|int|��ֵ����|�������������Ȳ���|x = 29<br>x = int(29)|
|float|��ֵ����|����С����E��ʾ��ѧ������|x = 29.5<br>x = float(29.5)|
|complex|��ֵ����|������j��ʾ�鲿|x = 1j<br>x = complex(1j)|
|list|��������||x = ["apple", "banana", "cherry"]<br>x = list(("apple", "banana", "cherry"))|
|tuple|��������||x = ("apple", "banana", "cherry")<br>x = tuple(("apple", "banana", "cherry"))|
|range|��������||x = range(6)|
|dict|ӳ������||x = {"name" : "Bill", "age" : 63}<br>x = dict(name="Bill", age=36)|
|set|��������||x = {"apple", "banana", "cherry"}<br>x = set(("apple", "banana", "cherry"))|
|frozenset|��������||x = frozenset({"apple", "banana", "cherry"})|
|bool|��������||x = True<br>x = bool(5)|
|bytes|����������||x = b"Hello"<br>x = bytes(5)|
|bytearray|����������||x = bytearray(5)|
|memoryview|����������||x = memoryview(bytes(5))|

## �����

```
import random
print(random.randrange(1, 10))
```
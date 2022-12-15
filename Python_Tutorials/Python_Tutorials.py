import datetime
import sys
# pip install requests
import requests
import re
import json
import os

# 创建或覆写文件
f = open(r".\demofile.txt", "w")
f.writelines([
	"Now the file has first line of content.\n",
	"Now the file has second line of content.\n"])
f.close()

# 创建或追加内容到文件
f = open(r".\demofile.txt", "a")
f.write("Now the file has more content!")
f.close()

# with 关键字自动清理
with open("demofile.txt") as f:
    for line in f.readlines():
        print(line, end="")
print()

f = open(r".\demofile.txt")
f = open(".\\demofile.txt")
f.seek(0)
l = f.read(3)
f.seek(0)
l = f.readline()
f.seek(0)
l = f.readlines()
f.seek(0)
for l in f:
	print(l, end="")
f.close()

if os.path.exists(r".\demofile.txt"):
  os.remove("demofile.txt")

if not os.path.exists("demoDir"):
	os.mkdir("demoDir")
if os.path.exists("demoDir"):
	os.rmdir("demoDir")

txt = "3246asdghr2834sdhjf340"
result = re.search("@", txt)
if result:
	print(result.span())
	print(result.start())
	print(result.end())
	print(result.group())

x=datetime.datetime.now()
print(x.weekday())

print('''Hello world.
Hello world.
Hello world.''');

mylist = list((1,2,3))
x=mylist.count(2)
print(x);

myset={1,2,3,4,5,6,7,8,9}

mydict = {"Brand":"123"}
for key, value in mydict.items():
	print(key+value)

i = 0
while i < 7:
	print(i)
	if i == 5: break
	i+=1
else:
	print("Exit")
print("X")

a='''i = 0
while i < 7:
	print(i)
	if i == 5: break
	i+=1
else:
	print("Exit")
print("X")
'''
x = compile(a, 'test', 'exec')
exec(x)

x = compile('print(78)', 'test', 'eval')
exec(x)

a='''input=input("Please input something:")
print("Input="+input)
'''
x = compile(a, 'test', 'exec')
# exec(x)

a = 'input("Please input something:")'
x = compile(a, 'test', 'single')
# exec(x)

class Person:
	def __init__(self, age, name):
		self.name = name
		self.age = age
	def __str__(self):
		return "Persion: Name={0}, Age={1}".format(self.name, self.age)

'''
delattr(Person, 'age')
p=Person()
print(p.age)
'''

def match(p):
	return p.age>=18
ps = [Person(10, "A"),Person(20, "B"),Person(30, "C"),Person(40, "D")]
ps = filter(match, ps)
for x in ps:
	print(x)

x = globals()
print(x["__file__"])

x = locals()
print(x["__file__"])

x = requests.get('https://w3school.com.cn/python/demopage.htm')
print(x.text)

for x in range(5):
	print(x);print("-");

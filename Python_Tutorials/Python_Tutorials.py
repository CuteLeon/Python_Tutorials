import datetime
import re
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
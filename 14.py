#read & write files

f=open("file1","w")
f.write("zxcv\n")
f.writelines(["1","2","3"])
f.write("\nbnm")
f.close()
print("1st:")
f=open("file1","r")
print(f.read())
print(f.readline())
f.close()
print("2nd:")
f=open("file1","r")
#直接对文件进行循环遍历
for i in f:
	print(i)
f.close()
print("3rd:")
f=open("file1","r")
#将文件读到列表中，每行作为一个元素
list1=f.readlines()
print(list1)
f.close()
print("4th:")
f=open("file1","r")
#将文件转换为一个列表
list1=list(f)
print(list1)
#f.tell()获取文件指针当前位置
print(f.tell())
#f.seek(offset,from_what),移动指针位置
#offset为移动量，from_what为初始位置，默认为0：文件头
f.seek(0,0)
print(f.tell())
f.close()
#使用with..as..处理文件对象，文件对象可以自动关闭
#with是try..finally..的简写
with open("file1","r") as f:
	print(f.readlines)
	print(f.closed)
print(f.closed)
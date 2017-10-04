import pickle
#pickle处理，文件需要以二进制形式打开
f=open("file1","wb")
pickle.dump(["1","2","3"],f)
f.close()
f=open("file1","rb")
list=pickle.load(f)
print(list)
for i in list:
	print(i,end=" ")
print()
f.close()
f=open("file1","rb")
#解包
t1,t2,t3=pickle.load(f)
print(t1,t2,t3)
f.close()
f=open("file1","rb")
#对文件进行循环遍历
for i in pickle.load(f):
	print(i,end=" ")
print()
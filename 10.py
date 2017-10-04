def  double(n,*tuble):
	'''在函数中接收元组，多余的参数都会作为元组的元素'''
	result=0
	for i in tuble:
		result+=i
	print(result)
	print(result*n)

double(2,1,1,1)

def dic(**dictionary):
	"""在函数中接收字典参数"""
	for i in dictionary:
		print(i,":",dictionary[i])
dic(d1="d11",d2="d22")
#注意字典的两种定义方式及对应的传递参数的方式
t={"d3":"d4","d5":"d6"}
dic(**t)
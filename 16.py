a=int(input("input a:"))
b=int(input("input b:"))
#尝试运行可能出现异常的代码
try:
    print("a/b=",a/b)
#捕捉任意类型的错误
except Exception as e:
	print(e)
#没有异常时执行的语句
else:
	print("no exception")
#不论有没有异常都执行的语句
finally:
	print("about exception")
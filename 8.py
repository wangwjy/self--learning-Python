import sys
#sys标准库
#从外界向程序传递参数
a1=None
s=sys.argv[0]
if len(sys.argv)>1:
	a1=sys.argv[1]
print(s,a1)
print(sys.version)
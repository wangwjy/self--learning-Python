#lambda形式
def plus(n):
	return lambda x:x+n
f=plus(10)
print(f(1))
f=plus("a")
print(f("b"))

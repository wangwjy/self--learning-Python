#‘#’表示注释

#print输出后会自动换行
print('1')
#‘’和“”表示字符串
print("'single quotation marks'")
print('"double quotation marks"')

#print多个数据时，可以用‘，’分隔；用‘，’分隔的数据中间会有空格
print（1,2,3）

#格式化输出
a=10
s="a"
print("%s=%d"%(s,a))

#输出多行语句
print("""
	1
	2
	3
	4""")
  
#更改print()函数的默认结束符
print("change ending",end=' ')
print('not wrapped')

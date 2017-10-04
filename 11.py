a=("a1","a2","a3")
for i in a:
	print(i,end=" ")
print()

b=["b1","b2","b3"]
for i in b:
	print(i,end=" ")
print()
b.append("b5")
for i in b:
	print(i,end=" ")
print()

c={"c1":"c11","c2":"c21"}
for i in c:
	print(i,":",c[i],end="  ")
print()
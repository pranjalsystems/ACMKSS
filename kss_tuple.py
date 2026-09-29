# tup=(chr(i+64) for i in range(1,26+1))

# tup1=("Math",)
# tup2=("Math")
# tup3=(1,)
# tup4=(1)
# print(type(tup1))
# print(type(tup2))
# print(type(tup3))
# print(type(tup4))

x=(1,2,3,4,5)
print(id(x),":",x)
y=list(x)
# print(id(y),":",y)#       id dont change
y[2]=x[2]*2
# print(id(y),":",y)#       id dont change
x=tuple(y)
# print(id(y),":",y)#       id dont change

print(id(x),":",x)
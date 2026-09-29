students = ["Alice","Bob","David","Eve","Bob"]
#print(students)
#print(type(students))

subjects = list(("Math","Science","History","English"))

#print(subjects[-2])
#print(subjects[-1])

# students[1:3]="apple"
# print(students)

# students[1:3]=["apple"]
# print(students)

# students = ["Alice","Bob","David","Eve","Bob"]
# students[1:4]=["Om"]
# print(students)

# students = ["Alice","Bob","David","Eve","Bob"]
# students.insert(2,"Om Bhaiya Goatt")
# print(students)

# students = ["Alice","Bob","David","Eve","Bob"]
# students.append("Om Bhaiya Goatt")
# print(students)

# subjects = ("Math","Science","History","English")
# diction={1:"A",2:"B",3:"C",4:"D"}
# students.extend(subjects)
# students.extend(diction)
# print(students)
# print(subjects)
# print(diction)

subjects = list(("Math","Science","History","English"))
# print(students)
# students.pop("Bob")
# print(students)
# students.pop(2)
# print(students)
# del students[0]
# print(students)
# students.clear()
# print(students)

# for x in students:
#     print(x)

# for i in range(len(subjects)):
#     print(students[i])
# i=0
# while i < len(subjects):
#     print(students[i])
#     i+=1

# [print(x,end=" . ") for x in students]
# print()
# import random
# marks=random.shuffle([10*(i+1) for i in range(10)])
# print(marks)
# abc=[i for i in marks if not(i<30)]
# print(abc)
# print(marks)

# marks.sort(reversed=True)
# print(marks)
# marks.sort(reversed=False)
# print(marks)

# list1=list(range(1,11))
# lisr2=list.copy()
# liss2=list(list1)?#Copy constructor
# list2=list[:]

# list3=students+students
# print(list3)
# list4=[]+students
# print(list4)

dic={1:[[1,2],[4,4],[6,6]],2:[4,5,6]}
x=dic[1]
x[1]=12
print(dic)
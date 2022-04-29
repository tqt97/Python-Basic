'''
10 Python Shortcuts 
'''

# /***    F string    ***/
from cmath import exp


print("/* F String */")
name = "Tuan"
x = f"{name}"
print(x)

# /***    Unpacking    ***/
tup = (1, 2, 3, 4, 5)
lst = [1, 2, 3, 4, 5]
string = "hello"
dic = {"name": "John", "age": "30"}
coords = [4, 5]
###################################
print("\n/* Tup */")
a, b, c, d, e = tup
print(a, b, c, d, e)
#
print("\n/* Dic */")
a, b = dic
print(a, b)
a, b = dic.items()
print(a, b)
a, b = dic.values()
print(a, b)
#
print("\n/* Coords */")
x, y = coords
print(x, y)

# /***    Multiple Assignment    ***/

width, height = 400, 500  # Instead of: width = 400; height = 500

# temp = width
# width = height
# height = temp
# Instead of
width, height = height, width

print("\n/*  Multiple Assignment */")
print(width, height)


# /***    Comprehensions    ***/
# num = []
# for i in range(10):
#     if i % 2 == 0:
#         num.append(i)
# num = [i for i in range(10) if i % 2 == 0]
##
# num = []
# for i in range(10):
#     for j in range(10):
#         num.append(i * j)
##
num = [i * j for i in range(5) for j in range(5)]
##
# list_test = []
# nested = []
# for _ in range(5):
#     nested.append(0)
# for _ in range(5):
#     list.append(nested)
# xx = [0 for _ in range(5)]
list_test = [[0 for _ in range(5)] for _ in range(5)]
##
text = (i for i in "Hello World")
text2 = (i for i in "Hello World")
##
sentence = "hello world"
dic_test = {char: sentence.count(char) for char in set(sentence)}
print("\n/*  Comprehensions */")
print(list_test)
print(list(text))
print(tuple(text2))
print(dic_test)

# /***    Object Multiplication     ***/
example1 = [1, 2, 3]    # list
example2 = (1, 2, 3)    # tuple
example3 = {1, 2, 3}    # set
example4 = {1: "one", 2: "two", 3: "three"}    # dict
print("\n/*  Object Multiplication   */")
print(example1 * 2)
print(example2 * 2)
# print(example3 * 2) # set does not support multiplication
# print(example4 * 2) # dict does not support multiplication

# /***    Inline/Ternary Condition     ***/
print("\n/*  Inline/Ternary Condition   */")
c1 = 1 if 2 > 3 else 0
print(c1)
c2 = 2 > 1 and 1 or 3
print(c2)

# /***    Zip function     ***/
names = ["Time", "Money", "Power"]
ages = [1, 2, 3]
colors = ["Black", "White", "Red"]

print("\n/*  Zip function   */")
print(list(zip(names, ages, colors)))
for name, age, color in zip(names, ages, colors):
    if age > 1:
        print(f"{name} is {age} years old and color is {color}")
    # print(name, age, color)


# /***   args & **kwargs     ***/
def func1(arg1, arg2, arg3):
    print(arg1, arg2, arg3)


def func2(arg1=None, arg2=None, arg3=None):
    print(arg1, arg2, arg3)


args = [1, 2, 3]
kwargs = {"arg1": 1, "arg2": 2, "arg3": 3}
print("\n/* args & **kwargs   */")

func1(*args)
func2(**kwargs)

# /***   For else & while else     ***/
search = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 7
found = False

print("\n/* For else & while else   */")
# for e in search:
#     if e == target:
#         found = True
#         break
# if not found:
#     print("Not Found")
# else:
#     print("Found")
##
# for e in search:
#     if e == target:
#         print("Found")
#         break
#     else:
#         print("Not Found")
##
i = 0
while i < len(search):
    e = search[i]
    if e == target:
        print("Found")
        break
    i += 1
else:
    print("Not Found")

# /***   Sort By Key     ***/
lst_demo = [[1, 2], [-3, 4], [5, -6], [4, 2], [-1, 3]]
# lst_demo.sort(reverse=True)


def sort_key(x):
    return x[0] + x[1]
lst_demo.sort(key=sort_key)

# lst_demo.sort(key=lambda x: x[1])
print("\n/* Sort By Key   */")
print(lst_demo)






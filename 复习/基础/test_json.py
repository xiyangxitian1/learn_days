import json

list1 = list()

list1.append({"name": "五王"})
list1.append({"age": 1})

# print(list1, type(list1))

a = json.dumps(list1, ensure_ascii=False)
print(a, type(a))

oDict = {"name": "Tom猫", "age": 3}
b = json.dumps(oDict, ensure_ascii=False)
print(b, type(b))


# f1 = open("2.txt", "w", encoding="gbk")
# json.dump(oDict, f1)
# f1.close()
#
# f2 = open("2.txt", "r", encoding="gbk")
# c = json.load(f2)
# print(c, type(c))
# f2.close()

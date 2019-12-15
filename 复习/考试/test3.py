import re

# phone = "13345327892"
# result = re.match("^1[3-9][0-9]{9}$", phone)
sex = "男女"
result = re.match("^(男|女)$", sex)
if not result:
    print("请输入正确的性别（男或女）")
else:
    print("正确的")

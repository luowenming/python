import re

names = ["name1", "_name", "2_name", "__name__", "name!",  "name#"]

for name in names:
    ret = re.match(r"^[a-zA-Z_][a-zA-Z_]*$",name)
    if ret:
        print("变量名%s符合要求！" %name)
    else:
        print("变量名%s 非法！" % name)
import re


def main():
    """匹配163邮箱的地址，且@符号之前有4到20位（数字字母下划线），例如hello@163.com"""
    ret = input("请输入邮箱：")
    result = re.match(r"^[0-9a-zA-Z]{4,20}@163\.com$", ret)

    if result:
        print("%s 邮箱合法！" % result.group())
    else:
        print("%s 邮箱非法！" % ret)


if __name__ == "__main__":
    main()
a = "abbbc*d*e*ghi"  # abc*d*e*ghi



def convert2list(a):
    """
    把a转换成列表-字典来存储
    :param a:
    :return:
    """
    l_a = list()
    i = 0
    len_a = len(a)
    while True:
        a1 = a[i]
        if i < len_a - 1:
            a1_next = a[i + 1]
            if a1_next == "*":
                l_a.append({a1: "*"})
                i += 1
            else:
                if l_a:
                    for k, v in l_a[-1].items():
                        if a1 == k:
                            if type(v).__name__ == "int":
                                v += 1
                            l_a[-1] = {k: v}
                        else:
                            l_a.append({a1: 1})
                else:
                    l_a.append({a1: 1})
        else:
            l_a.append({a1: 1})
            break
        i += 1
    return l_a


def del_rep(a):
    """简化正则表达式，把*前面重复的字母去重"""
    while "*" in a:
        i = a.index("*")
        pre = a[i - 1]
        i -= 2
        while i >= 0:
            cur_a = a[i]
            if cur_a == pre:
                # 去掉*前面重复的
                a = a[0:i] + a[i + 1:]
                i -= 1
            else:
                break
        a = a.replace("*", "#", 1)
    return a.replace("#", "*")

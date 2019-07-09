def f_input():
    # -1 2 7 -11 3 7 -12 3 6 -4 10 -14 -14 0 -14 7 7 7
    num_n = input()
    num_in_li = input().split()

    li = []
    for num_li_n in num_in_li:
        li.append(int(num_li_n))
    return li


def f(li):
    startNum = endNum = num = -1
    tempStartNum = tempEndNum = tempNum = 0
    try:
        if li[0] > 0:
            num = li[0]
        tempStartNum = tempEndNum = li[0]
    except:
        return str(startNum), str(endNum), str(num)

    for li_num in li:
        #
        if tempNum < 0:
            # tempNum < 0,li_num > 0  找到一个最大子序列，开始找下一个
            # tempStartNum < 0 and li_num == 0 序列 -1 -1 -1 0         测试点5
            if li_num > 0 or (tempStartNum < 0 and li_num == 0):
                tempStartNum = li_num
            tempNum = 0

        tempNum += li_num
        tempEndNum = li_num

        if tempNum > num:
            startNum = tempStartNum
            endNum = tempEndNum
            num = tempNum

    # 判断是否为全负序列
    if startNum < 0:
        startNum = tempStartNum
    if endNum < 0:
        endNum = tempEndNum
    if num < 0:
        num = 0

    return str(startNum), str(endNum), str(num)


if __name__ == '__main__':
    m_li = f_input()
    sNum, eNum, mNum = f(m_li)
    #print(mNum + " " + sNum + " " + eNum)
    print(mNum)
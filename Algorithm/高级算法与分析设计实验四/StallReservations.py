import numpy as np


if  __name__ == '__main__':

    # 定义牛的数量
    cow_num = 5 # int(input())

    # 定义牛列表 一行N列的数组
    cow_li = np.zeros((1, cow_num), dtype=[('x', 'int'), ('y', 'int'), ('z', 'int')])

    #for n in range(cow_num):
    #    cow_li[0][n] = tuple(int(x) for x in input().split())

    cow_li[0][0] = (1, 10, 0)
    cow_li[0][1] = (2, 4, 0)
    cow_li[0][2] = (3, 6, 0)
    cow_li[0][3] = (5, 8, 0)
    cow_li[0][4] = (4, 7, 0)

    # 队列排序，返回索引。开始时间早的在前，相同对结束时间排序
    cow_index = np.argsort(cow_li)
    print(cow_index)

    # 创建畜栏数组，N行N列, 第一列存放该行最后一头牛的下标
    corral_li = np.zeros((cow_num, cow_num), dtype=[('x', 'int'), ('y', 'int')])
    # 畜栏数
    cnum = 0
    for i in cow_index[0]:
        # corral_li 按结束时间从大到小排序
        corral_li = np.sort(corral_li, axis=0)[::-1]

        for cli in range(cow_num):
            # 该行最后一头牛的下标
            clix = np.nonzero(corral_li[cli])[0]
            #print(cow_li[0][i][0])
            #print(cli)
            #print(clix)
            #print(len(clix))
            #print(corral_li[cli][0])
            if len(clix) == 0:
                print('a')
                print(corral_li[cli][0])
                a = cow_li[0][i]
                s = slice(0,1)
                print(a[s])
                corral_li[cli][0] = cow_li[0][i][0:2]
                cnum += 1
                print(cow_li[0][i][2])
                print(cli)
                cow_li[0][i][2] = cli
                break
            elif cow_li[0][i][0] > corral_li[cli][clix][1]:
                corral_li[cli][clix+1] = cow_li[0][i][0:2]
                break
        print(corral_li)
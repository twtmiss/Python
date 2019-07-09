import numpy as np


def fun_work(f):
    # 最长非升子序列
    h = [0]
    for i in range(1, len(f) + 1):
        h.append(1)
    #print(len(f))

    for i in range(1, len(f)):
        # (int i=1;i <= n;i++)
        #print("iii")
        #print(i)
        for m in range(1, i):
            # (int j=1;j < i;j++)
            #print("mmmmmm")
            #print(m)
            #print(h[m]+1)
            #print(h[i])
            #print(f[m])
            #print(f[i])

            if (h[m]+1 >= h[i]) and (f[m] >= f[i]):
                #print("True")
                h[i] = h[m] + 1

            #print(f)
            #print(h)
    #print(f)
    fun_print(h)
    #fun_print(f)
    pass

def fun_print(li):
    max = 0
    for i in range(1,len(li)): # (int i=1;i <= n;i++)
        # max = (max < li[i])?li[i]: max
        if max < li[i]:
            max = li[i]
        else:
            max = max

    print( max)

if __name__ == '__main__':
    #li = [0, 300, 207, 155, 300, 299, 170, 158, 65]
    li = [0]
    num = int(input())
    #for i in range(num):
    #list(map(int, input().split()))
    for i in input().split():
        li.append(int(i))
    print(li)
    fun_work(li)

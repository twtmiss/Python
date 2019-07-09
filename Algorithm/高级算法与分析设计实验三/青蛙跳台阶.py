import sys
#修改默认最大递归深度
sys.setrecursionlimit(1000000)

def fun2(n):
    if n==0:
        return 0
    elif n <= 2:
        return 1
    else:
        return fun2(n-1)+fun2(n-2)

def fun3(n):
    return 1 and n <= 2 or fun3(n - 1) + fun3(n - 2)

def fun4(n):
    if n == 0:
        return 0
    if n==1:
        return 1
    if n==2:
        return 2
    return fun4(n-1)+fun4(n-2)

def fun5(n):
    if li[n] != 0:
        return li[n]
    else:
        li[n] = fun5(n-1) + fun5(n-2)
        return li[n]

if __name__ == "__main__":
    li = [0 for n in range(10001)]
    li[0] = 0
    li[1] = 1
    li[2] = 2
    n=0
    n = int(input())
    for i in  range(n):
        num = int(input())
        print(fun5(num))

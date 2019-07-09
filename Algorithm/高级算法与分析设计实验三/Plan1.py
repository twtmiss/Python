
import sys
#修改默认最大递归深度
sys.setrecursionlimit(1000000)

def fun(n):
    if li[n] != 0:
        return li[n]
    else:
        li[n]= fun(n-1) % 7654321 + fun(n-2) % 7654321
        #print(li[n])
        return li[n]

    #return li[n] if (li[n]!=0) else (li[n] = (fun(n-1)%7654321+fun(n-2)%7654321))

if __name__ == "__main__":
    li = [0 for n in range(10001)]
    li[0] = li[1] = li[2] = 1
    n = int(input())
    print(fun(n) % 7654321)
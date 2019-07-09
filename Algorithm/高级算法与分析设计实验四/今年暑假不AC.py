def fun_in(num):
    li = []
    for i in range(num):
        li.append(list(map(int,input().split())))
    #print(li)
    return li

def fun_sc(li):
    #teli = []
    #print(li)
    for m in range(len(li)):
        
        for i in range(len(li)-1):
            #print(i)
            #print(li[i])
            #print(li[i+1])
            
            if li[i][1] >= li[i+1][1]:
                ##print(li[i][1] >= li[i+1][1])
                if li[i][0] > li[i+1][0] or li[i][1] > li[i+1][1]:
                    #print(li[i][0] > li[i+1][0])
                    #print(li[i][1] > li[i+1][1])
                    teli = li[i]
                    li[i] = li[i+1]
                    li[i+1] = teli
            #print(li)
    return li

def fun_ac(li):
    #print(li)
    li2 = []
    li2.append(li[0])
    for m in range(len(li)):
        for i in li:
            #print(li2)
            #print(i)
            ##print()
            if int(i[0]) >= int(li2[-1][1]):
                li2.append(i)
    #print(li2)
    return len(li2)

def fun_test():
    test_li = [[1,3],[3,4],[0,7],[3,8],[15,19],[15,20],[10,15],[8,18],[6,12],[5,10],[4,14],[2,9]]
    return test_li

def fun_zc(num):
    m_li = fun_sc(fun_in(num))
    print(fun_ac(m_li))
    
#if __name__ == '__main__':
num = int(input())
while(num != 0):
    fun_zc(num)
        
    
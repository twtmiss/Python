import numpy as np

def fun_ac(li,ac_num):
    np_li2 = np.zeros((ac_num,ac_num+1,3),'int')
    np_li2[0][1] = li[0]
    np_li2[0][0] = [1,1,0]
    li[0][-1] = 1
    for m in li[1:]:
        for i in range(len(np_li2)):
            if np_li2[i][0][0] == 0:
                #print("m:"+str(m) + "  np_li2["+str(i)+"][0]:"+str(np_li2[i][0]))
                #print(str(m) + "添加进"+str(np_li2[i][0]))
                np_li2[i][1] = m
                np_li2[i][0] = [1,1,0]
                m[-1] = i+1
                #print("添加完毕："+str(np_li2[i][0]))
                break

            if m[0] > np_li2[i][np_li2[0][0][1]][1]:
                #print("m:"+str(m) + "  np_li2["+str(i)+"]["+str(np_li2[0][0][1])+"]"+str(np_li2[i][0][0]))
                np_li2[i][0][1] += 1
                np_li2[i][np_li2[i][0][1]] = m
                np_li2[i][0][0] += 1
                m[-1] = i+1
                #print("执行完毕：m:"+str(m) + "  np_li2["+str(i)+"]["+str(np_li2[0][0][1])+"]"+str(np_li2[i][0][0]))
                break

    return np_li2,li

def fun_in(num):
    in_list = []
    #print(np_in)
    for n in range(num):
        l = input().split()
        l.append('0')
        np_in[n] = l
    np_in = np_in.astype('int')
    return np_in

def fun_test():
    return np.array([[1,10],[2,4],[3,6],[5,8],[2,6],[4,7]])

def fun_select(se_li):
    pass
if  __name__ == '__main__':
    f_stacks = []
    m_num = int(input())

    m_li = fun_in(m_num)
    #print(m_li)
    #print(li.dtype)
    m_acli,m_li2 = fun_ac(m_li,m_num)
    #print("aaa")
    #print(m_acli)
    #print("答案")
    #print(m_li2)
    #print(m_li2[:,2])
    #print(np.unique(m_li2[:,2]))
    print(len(np.unique(m_li2[:,2])))
    for li in m_li2:
        print(li[2])

import numpy as np

def fun_min(min_queue):
    for q in min_queue[1:]:
        if q[1] < min_queue[0][1]:
            #min_queue[0],q = q,min_queue[0]
            min_queue[0][0],min_queue[0][1],min_queue[0][2],q[0],q[1],q[2] = q[0],q[1],q[2],min_queue[0][0],min_queue[0][1],min_queue[0][2]
    print(min_queue)
    return min_queue

def fun_ac2(li,num):
    lis = np.zeros(num,int)
    queue = []
    sum = 1
    lis[li[1][2]] = 1
    queue.append(list(li[1]))

    #li 输入列表
    for m in range(2,num):
        if (len(queue)) and queue[0][1] < li[m][0]:
            lis[li[m][2]] = lis[queue[0][2]]
            queue.pop(0)
        else:
            sum += 1
            lis[li[m][2]] = sum
        print(lis)
        queue.append(list(li[m]))
        print(queue)
        queue = fun_min(queue)
        print("asdasdasdasd")

    print(sum)
    for i in lis[1:]:
        print(i)
    #return li


class moon:
    def __init__(self,start,end,num):
        self.start = start
        self.end = end
        self.num = num

    def get_start(self):
        return self.start
    def get_end(self):
        return self.end
    def get_num(self):
        return self.num

class moon2:
    def __init__(self,start,end,num):
        self.data = {"start":start,"end":end,"num":num}
        print(self.data["start"])
    def get_data(self):
        return self.data
    def get_start(self):
        return self.data["start"]
    def get_end(self):
        return self.data["end"]
    def get_num(self):
        return self.data["num"]

def fun_min2(min_queue):
    for q in min_queue[1:]:
        if q.get_end() < min_queue[0].get_end():
            min_queue[0],q = q,min_queue[0]
            #min_queue[0][0],min_queue[0][1],min_queue[0][2],q[0],q[1],q[2] = q[0],q[1],q[2],min_queue[0][0],min_queue[0][1],min_queue[0][2]
    #print(q.get_num())
    #for m in m_li[1:]:
    #    print(m.get_num())
    return min_queue

def fun_ac(m_li,num):
    lis = []
    for i in range(num):
        lis.append(0)
    queue = []
    sum = 1
    lis[m_li[1].get_num()] = 1
    queue.append(m_li[1])
    #li 输入列表
    for m in range(2,num):
        if (len(queue)) and queue[0].get_end() < m_li[m].get_start():
            lis[m_li[m].get_num()] = lis[queue[0].get_num()]
            queue.pop(0)
        else:
            sum += 1
            lis[m_li[m].get_num()] = sum
        queue.append(m_li[m])
        queue = fun_min2(queue)

    print(sum)
    for i in lis[1:]:
        print(i)
    #return li

def fun_stack(li):
    for i in range(1,len(li)):
        cl = li[i]
        for m in range(i+1,len(li)):
            if li[m].get_start() < cl.get_start():
                cl,li[m] = li[m],cl
            elif li[m].get_start() == cl.get_start() and li[m].get_end() < cl.get_end():
                cl,li[m] = li[m],cl
        li[i] = cl
    return li

if  __name__ == '__main__':
    m_num = int(input()) + 1
    m_li = [0]
    for n in range(1,m_num):
        m_in = input().split()
        m_li.append(moon(int(m_in[0]),int(m_in[1]),n))

    m_li2 = fun_stack(m_li)

    fun_ac(m_li2, m_num)

import time
 
def time_cost(func):
    def _time_cost(*args,**kw):
        t1=time.time()
        func(*args,**kw)
        t2=time.time()
        return t2-t1
    return _time_cost
 
@time_cost
def test_add(list_a,huge_list_b):
    list3=[]
    list3 = list_a + huge_list_b
    return list3
@time_cost
def test_extend(list_a,huge_list_b):
    list3=[]
    list3.extend(list_a)
    list3.extend(huge_list_b)
    return list3
 
 
if __name__=='__main__':
    print('-----big list test-------------')
    a=['【空投】注册币市BISS，瓜分10万枚IOST代币', '【扬帆起航】社区新人必看及好贴索引-2019.2.21更新', '区块链下一个风口：稳定币的理财？', '【参与有奖】Lbank首款区块链古风网游火热来袭！', '2019全球区块链（杭州）高峰论坛', '【空投】注册币市BISS，瓜分10万枚IOST代币', '【扬帆起航】社区新人必看及好贴索引-2019.2.21更新', '区块链下一个风口：稳定币的理财？', '【参与有奖】Lbank首款区块链古风网游火热来袭！', '2019全球区块链（杭州）高峰论坛']
    b=['a']*(10**8)
    c=[]
    print('add cost:%s seconds'%test_add(a,b))
    print('extend cost:%s seconds'%test_extend(a,b))
 
    print('-----small list test-------------')
    a=['【空投】注册币市BISS，瓜分10万枚IOST代币', '【扬帆起航】社区新人必看及好贴索引-2019.2.21更新', '区块链下一个风口：稳定币的理财？', '【参与有奖】Lbank首款区块链古风网游火热来袭！', '2019全球区块链（杭州）高峰论坛', '【空投】注册币市BISS，瓜分10万枚IOST代币', '【扬帆起航】社区新人必看及好贴索引-2019.2.21更新', '区块链下一个风口：稳定币的理财？', '【参与有奖】Lbank首款区块链古风网游火热来袭！', '2019全球区块链（杭州）高峰论坛']
    b=['a']*(10**8)
    print('add cost:%s seconds'%test_add(a,b))
    print('extend cost:%s seconds'%test_extend(a,b))
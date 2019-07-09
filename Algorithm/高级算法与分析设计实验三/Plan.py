test_dict = {"political":["history"],"comprehensive":["geography"],"history":["political","geography"],"geography":["history","comprehensive"]}
def a():
    n=int(input())
    m=1
    li = [["political"]]
    lit = []
    test_first = "political"
    #li.append(test_dict[test_first])
    print(li)
        
    for li1 in li:
        if(m>=n):
            break
        print("111")
        print(li1)
        for qw in li1:
            print(qw)
            for str in test_dict[qw]:
                print("for2"+str)
                lit.append(str)
        li.append(lit)
        lit=[]
            
        m=m+1
    print("haha")
    
    print(len(li))
    for i in li:
        print(i)
    print(len(li[n-1])%7654321)
    
a()
    
        
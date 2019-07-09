
def fun_zf(num):
    s5 = num / 5
    s2 = num % 5 / 2
    s1 = num % 5 % 2 / 1
    return s1,s2,s5

if __name__ =='__main__':
    num = int(input())
    s1,s2,s5=fun_zf(num)
    print(int(s1))
    print(int(s2))
    print(int(s5))
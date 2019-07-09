'''
int queen[9];

//数组初始化
void init()
{
    memset(queen,0,9*sizeof(int));
}

//输出结果
void print()
{
    for(int i=1; i<9; i++) cout<<queen[i]<<"  ";
    cout<<endl;
}

//剪枝函数
bool canPlaceQueen(int k)
{
    for(int i = 1; i < k; i++)
    {
        //判断是否处于同一列或同一斜线
        if(queen[i] == queen[k] || abs(k-i) == abs(queen[k]-queen[i])) return false;
    }
    return true;
}
//迭代方法求解八皇后过程
void eightQueen_1()
{
    int k = 1;
    while(k>=1)
    {
        while(queen[k]<=7)
        {
            queen[k] += 1;
            if(k == 8 && canPlaceQueen(k))
            {
                print();
            }
            else if(canPlaceQueen(k))
            {
                k++;
            }
        }
        queen[k] = 0;
        k--;
    }
}

//递归方法求解八皇后过程
void eightQueen_2(int k)
{
    for(int i=1; i<9; i++)
    {
        queen[k] = i;
        if(k == 8 && canPlaceQueen(k))
        {
            print();
            return;
        }
        else if(canPlaceQueen(k))
        {
            eightQueen_2(k+1);
        }
    }
}
int main()
{
    init();
    eightQueen_1();
//    eightQueen_2(1);
    return 0;
'''

class nqueen:
    def __init__(self):
        self.queen = []
        for i in range(10):
            self.queen.append(0)

        self.num = 0

    def fun_print(self):
        if self.num % 5 == 0:
            print()
        print("第{}个摆法：".format(self.num), end="")

        for i in range(1, 9):
            # print("{} ".format(self.queen[i]),end="")
            print("{} ".format(self.queen[i]), end="")
        print("    ", end="")
        #print()

    #剪枝函数
    def fun_canPlaceQueen(self, k):
        for i in range(1, k):
            # 判断是否处于同一列或同一斜线
            if self.queen[i] == self.queen[k] or abs(k - i) == abs(self.queen[k] - self.queen[i]):
                return False
        return True

    #迭代求八皇后
    def fun_eightQueen1(self):
        k = 1
        while k >= 1:
            while self.queen[k] <= 7:
                self.queen[k] += 1
                if k == 8 and self.fun_canPlaceQueen(k):
                    self.fun_print()
                    self.num += 1
                elif self.fun_canPlaceQueen(k):
                    k += 1

            self.queen[k] = 0
            k -= 1

        print(self.num)

    # 递归求八皇后问题
    def fun_eightQueen2(self, k):
        for i in range(1, 9):
            self.queen[k] = i
            if k == 8 and self.fun_canPlaceQueen(k):
                self.fun_print()
                self.num += 1
                break
            elif self.fun_canPlaceQueen(k):
                self.fun_eightQueen2(k + 1)

    def fun_num(self):
        print(self.num)


if __name__ == '__main__':
    n_queen = nqueen()
    n_queen.fun_eightQueen1()
    n_queen.fun_num()


    #n_queen = nqueen()
    #n_queen.fun_eightQueen2(1)
    #n_queen.fun_num()

























'''
#include<iostream>
#include<cstdio>
#include<cstring>
#include<cmath>
#include<algorithm>
#include<string>
#include<cstdlib>
#include<queue>
#include<set>
#include<map>
#include<stack>
#include<vector>
#define INF 0x3f3f3f3f
#define PI acos(-1.0)
#define N 50001
#define MOD 123
#define E 1e-6
using namespace std;
struct Node{
    int start;
    int endd;
    int num;
    friend bool operator < (Node x,Node y)
    {
        if(x.endd==y.endd)//如果结束时间相等，开始时间早的优先级高
            return x.start<y.start;
        else//如果结束时间不相等，越早结束的优先级越高
            return x.endd>y.endd;
    }
}cow[N];
int num[N];
priority_queue<Node> q;
int cmp(Node x,Node y)
{
    if(x.start==y.start)//如果开始时间相同，则按照结束时间排序
        return x.endd<y.endd;
    else//如果开始时间不同，则按照开始时间排序
        return x.start<y.start;
}
int main()
{
    int n;
    scanf("%d",&n);
    for(int i=1;i<=n;i++)
    {
        scanf("%d%d",&cow[i].start,&cow[i].endd);//输入开始时间与结束时间
        cow[i].num=i;//记录牛的编号
    }

    sort(cow+1,cow+n+1,cmp);//将所有牛排序

    int sum=1;
    q.push(cow[1]);
    num[cow[1].num]=1;

    for(int i=2;i<=n;i++)
    {
        if( !q.empty() && q.top().endd<cow[i].start)//如果牛的挤奶时间开始值大于优先队列头部的结束值
        {
            num[cow[i].num]=num[q.top().num];//两头牛可共用一个栏位，记录序号
            q.pop();//从优先队列中删除这头牛
        }
        else
        {
            sum++;//栏位数+1
            num[cow[i].num]=sum;//记录栏位号
        }
        q.push(cow[i]);
    }

    printf("%d\n",sum);
    for(int i=1;i<=n;i++)
        printf("%d\n",num[i]);

    return 0;
}
'''

def quick_sort_standord(array,low,high):
    ''' realize from book "data struct" of author 严蔚敏
    '''
    if low < high:
        key_index = partion(array,low,high)
        quick_sort_standord(array,low,key_index)
        quick_sort_standord(array,key_index+1,high)

def partion(array,low,high):
    key = array[low]
    while low < high:
        while low < high and array[high] >= key:
            high -= 1
        if low < high:
            array[low] = array[high]

        while low < high and array[low] < key:
            low += 1
        if low < high:
            array[high] = array[low]

    array[low] = key
    return low

if __name__ == '__main__':
    array2 = [9,3,2,1,4,6,7,0,5]

    print(array2)
    quick_sort_standord(array2,0,len(array2)-1)
    print(array2)

'''
#include<cstdio>
#include<iostream>
using namespace std;
int f[2000005];
int n,x,y;
char c;
void init(int s)
{
    for(int i = 1; i <= s; i++)
        f[i] = i;
}
int find(int x)
{
    if(x != f[x])
        f[x] = find(f[x]);
    return f[x];
}
void merge(int r1, int r2)
{
    f[r2] = r1;
}
int main()
{
    scanf("%d",&n);
    init(n);
    getchar();
    int sum = 0;
    while(1)
    {
        scanf("%c",&c);
        if (c == 'S')
        {
            break;
        }
        scanf("%d %d",&x, &y);
        getchar();
        int f1 = find(x), f2 = find(y);
        if(c == 'I')
            merge(f1,f2);
        else (f1 == f2)?printf("yes\n"):printf("no\n");

    }
    for(int i=1; i<=n; i++)
    {
        if(f[i]==i)
            sum++;
    }
    if(sum==1)
        printf("The network is connected.");
    else
        printf("There are %d components.",sum);
        return 0;
}

'''
def find(list, x):
    if x != list[x]:
        list[x] = find(list, list[x])
    return list[x]

def merge(list, r1, r2):
    list[r2] = r1
    return list

def f():
    n = int(input())
    list = []
    for i in range(n + 1):
        list.append(i)
    sum = 0
    while 1:
        li2 = input().split()
        if li2[0] == 'S' : break
        li2[1],li2[2] = int(li2[1]),int(li2[2])
        f1 = find(list, li2[1])
        print("f1:{}".format(f1))
        f2 = find(list, li2[2])
        print("f2:{}".format(f2))
        if li2[0] == 'I':
            list = merge(list, f1, f2)
            print(list)
        else:
            print("yes") if f1 == f2 else print("no")

    for i in range(1, n+1):
        if list[i] == i:
            sum += 1

    if sum == 1:
        print("The network is connected.")
    else:
        print("There are {} components.".format(sum))
if __name__ == '__main__':
    f()
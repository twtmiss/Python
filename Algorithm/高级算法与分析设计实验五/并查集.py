
class f:
    def __init__(self, m):
        self.m = m
        #self.n = n
        self.dic = {}
        self.list = []
        self.z = -1
        self.x = -1
        self.y = -1

    def f_rein(self):
        inli = [int(a) for a in input().split()]
        return inli[0],inli[1],inli[2]

    def f_put(self):
        for f in range(self.m):
            self.z, self.x, self.y = self.f_rein()

            if self.x not in self.dic:
                self.dic[self.x] = len(self.list)
                self.list.append([self.x])
            if self.y not in self.dic:
                self.dic[self.y] = len(self.list)
                self.list.append([self.y])
            print(self.dic)
            print(self.list)
            if self.z == 2:
                if self.dic[self.x] == self.dic[self.y]:
                    print("Y")
                else:
                    print("N")

            if self.z == 1:
                self.list[self.dic[self.x]].extend(self.list[self.dic[self.y]])
                n = self.dic[self.y]
                for i in self.list[self.dic[self.y]]:
                    self.dic[i] = self.dic[self.x]
                self.list.pop(n)
            print(self.dic)
            print(self.list)
'''
#include<cstdio>
#include<iostream>
using namespace std;
int f[2000005];
int n,m,x,y,z;
void init(int s) {for(int i = 1; i <= s; i++) f[i] = i;}
int find(int x) {
    if(x != f[x]) f[x] = find(f[x]);
        return f[x];
    }
void merge(int r1, int r2) {f[r2] = r1;}
int main() {
scanf("%d%d",&n,&m);
init(n);
for(int i = 1; i <= m; i++) {
scanf("%d%d%d",&z,&x,&y);
int f1 = find(x), f2 = find(y);
 if(z == 1)  merge(f1,f2);
else (f1 == f2)?printf("Y\n"):printf("N\n");
}    
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
    lin = [int(m) for m in input().split()]
    list = []
    for i in range(lin[0] + 1):
        list.append(i)
    for i in range(1, lin[1]):
        li2 = [int(m) for m in input().split()]
        f1 = find(list, li2[1])
        print("f1:{}".format(f1))
        f2 = find(list, li2[2])
        print("f2:{}".format(f2))
        if li2[0] == 1:
            list = merge(list, f1, f2)
            print(list)
        else:
            print("Y") if f1 == f2 else print("N")

if __name__ == '__main__':
    f()
    #f(int(input().split()[1])).f_put()



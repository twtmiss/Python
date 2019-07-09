class RadarInstallation_planA():
    def __init__(self):
        self.status = True
        self.num = 1            #测试用例个数
        self.line = 0           #岛屿个数
        self.d = 0              #雷达探测距离
        self.islands_x = 0      #岛屿X坐标
        self.islands_y = 0      #岛屿Y坐标
        self.x_left = 0         #岛屿投射到海岸线上雷达可探测范围的最左坐标
        self.x_right = 0        #岛屿投射到海岸线上雷达可探测范围的最右坐标
        self.island_li = []     #存放岛屿的list
        self.coordinate_li = [] #存放探测范围的list
        self.radar_li = []      #存放雷达的lsit
        self.bf = True

    def fun_init(self):
        self.status = True
        self.line = 0  # 岛屿个数
        self.d = 0  # 雷达探测距离
        self.islands_x = 0  # 岛屿X坐标
        self.islands_y = 0  # 岛屿Y坐标
        self.x_left = 0  # 岛屿投射到海岸线上雷达可探测范围的最左坐标
        self.x_right = 0  # 岛屿投射到海岸线上雷达可探测范围的最右坐标
        self.island_li = []  # 存放岛屿的list
        self.coordinate_li = []  # 存放探测范围的list
        self.radar_li = []  # 存放雷达的lsit


    def fun_input(self):
        # li = [[-3,1],[1,2],[2,1]]
        while self.bf:
            self.fun_init()
            input_li = [int(x) for x in input().split()]
            self.line = input_li[0]
            self.d = input_li[1]
            if self.d < 0 or self.line < 0:
                self.status = False
            if self.line == 0 and self.d == 0:
                self.bf = False
            else:
                # 添加进岛屿list
                for i in range(self.line):
                    self.island_li.append([int(x) for x in input().split()])
                self.fun_coordinate()

    def fun_sort(self,elem):
        return elem[0]

    # 根据岛屿的纵坐标计算出岛屿左右两边的雷达探测距离，放入coordinate_li
    def fun_coordinate(self):
        if not self.status:
            self.fun_output()

        self.island_li.sort(key=self.fun_sort)
        #print(self.island_li)

        for self.islands_x, self.islands_y in self.island_li:
            # 判断岛屿与海岸线距离超过有效距离，返回-1，程序结束
            if pow(pow(self.d, 2) - pow(self.islands_y, 2), 1 / 2) < 0:
                self.status = False
                break
            else:
                self.x_left = self.islands_x - int(pow(pow(self.d, 2) - pow(self.islands_y, 2), 1 / 2))
                self.x_right = self.islands_x + int(pow(pow(self.d, 2) - pow(self.islands_y, 2), 1 / 2))
                self.coordinate_li.append([self.x_left, self.x_right])
        self.fun_deal()

    def fun_deal(self):

        self.radar_li.append(self.coordinate_li[0])

        for left,right in self.coordinate_li[1:]:
            if left <= self.radar_li[-1][1]:
                self.radar_li[-1][0] = left
                if right <= self.radar_li[-1][1]:
                    self.radar_li[-1][1] = right
            else:
                self.radar_li.append([left,right])
        self.fun_output()

    def fun_output(self):
        if self.status:
            print("Case {}: {}".format(self.num,len(self.radar_li)) )
        else:
            print("Case {}: -1".format(self.num))
        self.num += 1
        input()
        self.fun_input()

if __name__ == "__main__":
    RadarInstallation_planA().fun_input()
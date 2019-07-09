'''

public class MST {

	public static final int NOT_REACHED = -1;

	public static void prim(int[][] E) {
		int n = E.length;

		boolean[] S = new boolean[n];
		int[] dist = new int[n];
		int[] prev = new int[n];

		S[0] = true; // 选取顶点1作为起始点
		for (int i = 1; i < n; i++) {
			dist[i] = E[0][i];
			prev[i] = 0;
			S[i] = false;
		}

		int min = -1, minV = -1;
		for (int i = 1; i < n; i++) {
			min = -1;
			minV = -1;
			// 选择离S中顶点最近的点
			for (int j = 1; j < n; j++) {
				if (!S[j] && dist[j] != -1 && (min == -1 || dist[j] < min)) {
					min = dist[j];
					minV = j;
				}
			}
			if (minV == -1)
				continue;

			S[minV] = true;

			// S中多了个点，需要改变S离外面的点的最短距离
			for (int j = 1; j < n; j++) {
				if (!S[j] && isReachable(E, minV, j)
						&& (dist[j] == -1 || E[minV][j] < dist[j])) {
					dist[j] = E[minV][j];
					prev[j] = minV;
				}
			}

			// 输出测试结果
			for (int j = 0; j < n; j++) {
				if (S[j]) {
					System.out.print((j + 1) + " ");
				}
			}
			System.out.println();
		}

	}

	private static boolean isReachable(int[][] E, int v1, int v2) {
		return E[v1][v2] != NOT_REACHED;
	}

	public static void main(String[] args) {
		int[][] E = { { -1, 6, 1, 5, -1, -1 }, { 6, -1, 5, -1, 3, -1 },
				{ 1, 5, -1, 5, 6, 4 }, { 5, -1, 5, -1, -1, 2 },
				{ -1, 3, 6, -1, -1, 6 }, { -1, -1, 4, 2, 6, -1 } };

		prim(E);
	}
}
'''

NOT_REACHED = -1

def prim(list):
    n = len(list)
    boolli = []
    for i in range(n):
        boolli.append(0)
    distli = []
    for i in range(n):
        distli.append(0)
    prevli = []
    for i in range(n):
        prevli.append(0)

    boolli[0] = True
    for i in range(1, n):
        distli[i] = list[0][i]
        prevli[i] = 0
        boolli[i] = False

    min = -1
    minV = -1
    for i in range(1, n):
        min = -1
        minV = -1
        for j in range(1, n):
            if not boolli[j] and distli[j] != -1 and (min == -1 or distli[j] < min):
                min = distli[j]
                minV = j

        if minV == -1:
            continue

        boolli[minV] = True

        for j in range(1, n):
            if (not boolli[j] and list[minV][j] != NOT_REACHED) and (distli[j] == -1 or list[minV][j] < distli[j]):
                distli[j] = list[minV][j]
                prevli[j] = minV

        for j in range(n):
            if boolli[j]:
                print("{} ".format(j+1),end="")
        print()

if __name__ == '__main__':
    list = [[-1,6,1,5,-1,-1],[6,-1,5,-1,3,-1],[1,5,-1,5,6,4],[5,-1,5,-1,-1,2],[-1,3,6,-1,-1,6],[-1,-1,4,2,6,-1]]

    prim(list)
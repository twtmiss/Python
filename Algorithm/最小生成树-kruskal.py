'''
public class Kruskal {

	public static final int NOT_REACHED = -1;

	public static void kruskal(int[][] E) {
		int n = E.length;
		MinHeap<Edge> edges = new MinHeap<Edge>(n * (n - 1) / 2);
		int[] setNum = new int[n];
		for (int i = 0; i < n; i++) {
			setNum[i] = i; // 初始时，每个顶点是一个子集合
		}
		// 初始化最小堆
		for (int i = 0; i < n; i++) {
			for (int j = i + 1; j < n; j++) {
				if (isReachable(E, i, j)) {
					edges.add(new Edge(i, j, E[i][j]));
				}
			}
		}
		Edge edge;
		int count = n, v1, v2, num;
		while ((count > 1) && (edge = edges.removeMin()) != null) {
			v1 = edge.v1;
			v2 = edge.v2;
			if (setNum[v1] == setNum[v2]) continue; // 两个顶点在同一个子集合里
			count--; // 融合两个子集合，减少了一个子集合
			num = setNum[v2];
			for (int i = 0; i < n; i++) {
				if (setNum[i] == num) {
					setNum[i] = setNum[v1]; // 把两个子集合融合到一个
				}
			}
			System.out.println((v1+1) + "~" + (v2+1) + " : " + edge.len);
		}
	}

	private static boolean isReachable(int[][] E, int v1, int v2) {
		return E[v1][v2] != NOT_REACHED;
	}

	public static void main(String[] args) {
		int[][] E = { { -1, 6, 1, 5, -1, -1 }, { 6, -1, 5, -1, 3, -1 },
				{ 1, 5, -1, 5, 6, 4 }, { 5, -1, 5, -1, -1, 2 },
				{ -1, 3, 6, -1, -1, 6 }, { -1, -1, 4, 2, 6, -1 } };

		kruskal(E);
	}
}

class Edge implements Comparable<Edge> {

	public int v1, v2, len;

	public Edge(int v1, int v2, int len) {
		this.v1 = v1;
		this.v2 = v2;
		this.len = len;
	}

	@Override
	public int compareTo(Edge o) {
		return len - o.len;
	}

	@Override
	public String toString() {
		return len + "";
	}
}
'''

'''
class DisjointSet(dict):
    #不相交集

    def __init__(self, dict):
        pass

    def add(self, item):
        self[item] = item

    def find(self, item):
        if self[item] != item:
            self[item] = self.find(self[item])
        return self[item]

    def unionset(self, item1, item2):
        self[item2] = self[item1]


def Kruskal_1(nodes, edges):
    #基于不相交集实现Kruskal算法
    forest = DisjointSet(nodes)
    MST = []
    for item in nodes:
        print(item)
        forest.add(item)
    edges = sorted(edges, key=lambda element: element[2])
    num_sides = len(nodes) - 1  # 最小生成树的边数等于顶点数减一
    for e in edges:
        node1, node2, _ = e
        parent1 = forest.find(node1)
        parent2 = forest.find(node2)
        if parent1 != parent2:
            MST.append(e)
            num_sides -= 1
            if num_sides == 0:
                return MST
            else:
                forest.unionset(parent1, parent2)
    pass
'''

def Kruskal(nodes, edges):
    ''' Kruskal 无向图生成最小生成树 '''
    all_nodes = nodes  # set(nodes)
    used_nodes = set()
    MST = []
    edges = sorted(edges, key=lambda element: element[2], reverse=True)
    # 对所有的边按权重升序排列
    while used_nodes != all_nodes and edges:
        element = edges.pop(-1)
        if element[0] in used_nodes and element[1] in used_nodes:
            continue
        MST.append(element)
        used_nodes.update(element[:2])
        # print(used_nodes)
    return MST


def main():
    nodes = set(list('ABCDEFGHI'))
    edges = [("A", "B", 4), ("A", "H", 8),
             ("B", "C", 8), ("B", "H", 11),
             ("C", "D", 7), ("C", "F", 4),
             ("C", "I", 2), ("D", "E", 9),
             ("D", "F", 14), ("E", "F", 10),
             ("F", "G", 2), ("G", "H", 1),
             ("G", "I", 6), ("H", "I", 7)]
    print("The undirected graph is :")
    for i in range(14):
        print(edges[i], end="   ")
        if (i-1)%3 == 0:
            print()
    print("The minimum spanning tree by Kruskal is : ")
    print(Kruskal(nodes, edges))

if __name__ == '__main__':
    main()

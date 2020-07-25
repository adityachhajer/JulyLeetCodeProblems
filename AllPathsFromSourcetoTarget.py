class Solution:
    def solve(self, graph, k, l, i):
        if len(graph[i]) == 0:
            l.append(k)
            return

        for j in graph[i]:
            self.solve(graph, k + [j], l, j)
        return l

    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        l = []
        return self.solve(graph, [0], l, 0)
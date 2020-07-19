import sys

sys.setrecursionlimit(10 ** 9)


class Solution:
    def isevilcyclic(self, di, visited, cur, l, lld):
        if visited[cur] == True:
            return True
        visited[cur] = True
        if cur in di.keys():
            for i in range(0, len(di[cur])):
                flag = self.isevilcyclic(di, visited, di[cur][i], l, lld)
                if flag == True:
                    return True
                if di[cur][i] not in lld.keys():
                    l.append(di[cur][i])
                    lld[di[cur][i]] = 1
        else:
            if cur not in lld.keys():
                l.append(cur)
                lld[cur] = 1
        visited[cur] = False
        return False

    def isCyclic(self, n, di, l, lld):
        visited = [False] * n
        for i in range(0, n):
            if i in di.keys():
                visited[i] = True
                for j in range(len(di[i])):
                    fl = self.isevilcyclic(di, visited, di[i][j], l, lld)
                    if fl == True:
                        return []
                    if di[i][j] not in lld.keys():
                        l.append(di[i][j])
                        lld[di[i][j]] = 1
                visited[i] = False
            if i not in lld.keys():
                l.append(i)
                lld[i] = 1
        l.reverse()
        return l

    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        di = {}
        for i in prerequisites:
            if i[1] in di.keys():
                x = di[i[1]]
                x.append(i[0])
                di[i[1]] = x
            else:
                di[i[1]] = [i[0]]
        l = []
        lld = {}
        return self.isCyclic(numCourses, di, l, lld)

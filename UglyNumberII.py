import heapq


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        seen = {1}
        data = [1]
        cur = None

        for i in range(n - 1):
            cur = heapq.heappop(data)
            if cur * 2 not in seen:
                seen.add(cur * 2)
                heapq.heappush(data, cur * 2)
            if cur * 3 not in seen:
                seen.add(cur * 3)
                heapq.heappush(data, cur * 3)
            if cur * 5 not in seen:
                seen.add(cur * 5)
                heapq.heappush(data, cur * 5)

        return heapq.heappop(data)
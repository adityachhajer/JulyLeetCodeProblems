class Solution:
    def solve(self, x, s, wordDict, l, k, rs, i, n):
        if i == n:
            if len(''.join(map(str, k))) == n:
                l.append(k)
            return None

        else:
            rs = rs + s[i]
            if rs not in wordDict:
                self.solve(x, s, wordDict, l, k, rs, i + 1, n)
            else:
                self.solve(x, s, wordDict, l, k + [rs], '', i + 1, n)
                self.solve(x, s, wordDict, l, k, rs, i + 1, n)

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        l = []
        k = []
        x = ''.join(map(str, wordDict))
        rs = ''
        wordDict = set(wordDict)
        for i in s:
            if i not in x:
                return []
        self.solve(x, s, wordDict, l, k, rs, 0, len(s))

        a = []
        for i in l:
            a.append(' '.join(i))
        return a
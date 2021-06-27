class Solution:
    def numTrees(self, n: int) -> int:
        if n <= 1:
            return n

        G = [1, 1]
        for i in range(2, n+1):
            j = 1
            g_num = 0
            while j <= i:
                g_num += G[j - 1] * G[i - j]
                j += 1
            G.append(g_num)

        return G[n]



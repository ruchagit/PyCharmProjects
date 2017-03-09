from copy import copy
'''
Given a 2D binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.

'''

class Solution(object):
    def maximalSquare(self, mat):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        maxlen = 0
        dp = copy(mat)
        for r in range(1,len(mat)):
            for c in range(1,len(mat[0])):
                if mat[r][c] != 0:
                    dp[r][c] = min(mat[r][c-1],
                                   mat[r-1][c], mat[r-1][c-1]) + 1
                    maxlen = max(maxlen,dp[r][c])
        return maxlen**2


if __name__ == '__main__':
    s = Solution()
    mat = [[1, 0, 1, 0, 0],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0]
           ]
    print s.maximalSquare(mat)


def count_coins_recursive(coins, S):
    if S == 0:
        return 0
    minval = 9999
    for i in range(len(coins)):
        if coins[i] <= S:
            val = count_coins_recursive(coins, S-coins[i])+1
            minval = min(minval,val)
    return minval

def count_coins_dp(coins,S):
    #dp = [9999] * (S+1)
    dp = {}
    dp[0] = [0]
    for s in range(1, S+1):
        minval = 9999
        for c in coins:
            if c <= s:
                if s-c in dp and dp[s-c][0]+1 <= minval:
                    minval = dp[s-c][0]+1
                    dp[s] = [minval]
                    dp[s].extend(dp[s-c][1:])
                    dp[s].append(c)
    return dp[S]

def longest_nondecreasing_sequence_dp(seq):
    dp = [1] * len(seq)
    for i in range(1, len(seq)):
        for j in range(i-1,-1,-1):
            if seq[i] >= seq[j]:
                l = dp[j]+1
                if dp[i] < l:
                    dp[i] = l
    return dp


def shortest_path_recur(graph, start, end, path):
    if start in path:
        return path
    path = path + [start]
    print path
    if start == end:
        return path
    if start not in graph:
        return None
    shortest = None
    for node in graph[start]:
        print node
        newpath = shortest_path_recur(graph, node, end, path)
        if newpath:
            if not shortest or len(newpath) < len(shortest):
                shortest = newpath
    return shortest

class Solution(object):
    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        result = []
        a = dict()
        l = len(words)
        for i in range(l):
            if words[i] not in a:
                a[words[i]] = i
        for i in range(l):
            if words[i][::-1] in a:
                result.append([i,a[words[i][::-1]]])
        return result

def HouseBurglar(h):
    n = len(h)
    if n == 0:
        return 0
    dp = [[0 for x in range(n)] for y in range(2)]
    dp[1][0] = h[0]
    for i in range(1, n):
        dp[0][i] = max(dp[0][i - 1], dp[1][i - 1])
        dp[1][i] = dp[0][i - 1] + h[i]
    return max(dp[0][n-1], dp[1][n-1])

def func(arr):
    sum = 0
    for i in range(0,len(arr)):
        sum = sum ^ arr[i]
    return sum


def addStrings(str1, str2):
    s1 = len(str1) - 1
    s2 = len(str2) - 1
    c = 0
    res = []
    while s1 >= 0 and s2 >= 0:
        tup = addUp(str1[s1], str2[s2], c)
        res.insert(0, tup[0])
        c = tup[1]
        s1 -= 1
        s2 -= 1
    while s1 >= 0:
        tup = addUp(str1[s1], '0', c)
        res.insert(0, tup[0])
        c = tup[1]
        s1 -= 1
    while s2 >= 0:
        tup = addUp(str2[s2], '0', c)
        res.insert(0, tup[0])
        c = tup[1]
        s2 -= 1
    return ''.join(map(str, res))


def addUp(s1, s2, c):
    n1 = int(s1)
    n2 = int(s2)
    sum = n1 + n2 + c
    ret = sum % 10
    sum = sum // 10
    return (ret, sum)


def calc(str):
    n = len(str)
    stack = []
    for i in range(n):
        print stack
        if str[i] == ' ':
            continue
        elif str[i].isdigit():
            print i
            start = i
            while str[i].isdigit():
                i += 1
            i -= 1
            num = int(str[start:i+1])
            stack.append(num)
        elif str[i] == '(':
            stack.append(str[i])
        elif str[i] == '+' or str[i] == '-':
            stack.append(str[i])
        else:
            while stack[-1] != '(':
                num1 = stack.pop() if len(stack) > 0 and stack[-1] != '(' else None
                op = stack.pop() if len(stack) > 0 and stack[-1] != '(' else None
                num2 = stack.pop() if len(stack) > 0 and stack[-1] != '(' else None
                if op=='+': res = num2+num1
                elif op =='-': res = num2-num1
                else: res = num1
                if stack[-1] == '(':
                    stack.pop()
                    stack.append(res)
                    break
                else:
                    stack.append(res)
    if len(stack) == 1:
        return stack.pop()
    while len(stack) >= 3:
        num1 = stack.pop()
        op = stack.pop()
        num2 = stack.pop()
        if op=='+': res = num1+num2
        else: res = num1-num2
        if stack[-1]:
            stack.append(res)
        else:
            return res

def max_subarray(arr):
    max_sum = arr[0]
    curr_max = arr[0]
    for i in range(1,len(arr)):
        curr_max = max(arr[i], curr_max+arr[i])
        max_sum = max(max_sum,curr_max)
    return max_sum

def HotelStops_dp(h):
    p = []
    p.insert(0, 0)
    for i in range(1,len(h)):
        min_penalty = float('inf')
        for j in range(0,i):
            # if h[i] - h[j] > 200:
            #     continue
            penalty = p[j] + (200 - (h[i]-h[j]))**2
            min_penalty = min(penalty, min_penalty)
        p.insert(i, min_penalty)
    return p

def yuckdonald(d,p,k):
    dp = []
    dp.insert(0,p[0])
    for i in range(0,len(d)):
        max_profit = float('-inf')
        for j in range(0,i):
            profit = p[i]
            if d[i]-d[j] >= k:
                profit = dp[j] + p[i]
            max_profit = max(max_profit, profit)
        dp.insert(i, max_profit)
    return dp

def validString(str):
    dp = [False]*(1+len(str))
    dp[0] = True
    words = []
    for i in range(1,len(str)+1):
        for j in range(0,i):
            if dp[j] and func(str[j:i]):
                dp[i] = True
                words.append(str[j:i])
    print words
    return getWords(str,dp)

def getWords(str,dp):

    ans =[]
    for i in range(1, len(dp)):
        ans.append(str[i-1])
        if i < len(dp)-1 and dp[i] and not dp[i+1]:
            ans.append(' ')

    return ''.join(ans)

def pebbleProblem(mat, graph):
    res = []
    n = len(mat[0])
    max_sum = 0
    final = []
    for i in range(1,8):
        sum = 0
        del res[:]
        curr_type = tryPatterns([col[0] for col in mat], [i])
        sum += curr_type[1]
        res.append(curr_type[0])
        for i in range(1, n):
            next_type = tryPatterns([col[i] for col in mat], graph[curr_type[0]])
            sum += next_type[1]
            res.append(next_type[0])
            curr_type = next_type
            print sum, res
        if sum > max_sum:
            max_sum = sum
            del final[:]
            final.extend(res)
    return (final, max_sum)

def tryPatterns(col, patterns):
    max = float('-inf')
    ret = 0
    for p in patterns:
        if p == 1:
            if col[0] > max:
                max = col[0]
                ret = 1
        elif p == 2:
            if col[1] > max:
                max = col[1]
                ret = 2
        elif p == 3:
            if col[2] > max:
                max = col[2]
                ret = 3
        elif p == 4:
            if col[3] > max:
                max = col[3]
                ret = 4
        elif p == 5:
            if col[0] + col[2] > max:
                max = col[0] + col[2]
                ret = 5
        elif p == 6:
            if col[1] + col[3] > max:
                max = col[1] + col[3]
                ret = 6
        elif p == 7:
            if col[0] + col[3] > max:
                max = col[0] + col[3]
                ret = 7
    return (ret, max)


def func(a):
    dictionary ={}
    dictionary["it"] = True
    dictionary["was"] = True
    dictionary["the"] = True
    dictionary["best"] = True
    dictionary["of"] = True
    dictionary["times"] = True
    dictionary["i"] = True
    if a in dictionary:
        return True
    else:
        return False

def mult(arr,a):
    temp = [[[] for x in range(len(arr))] for x in range(len(arr))]
    for i in range(len(arr)):
        temp[i][i].append(arr[i])
    for l in range(2, len(arr)+1):
        for i in range(len(arr)-l+1):
            j = i + l - 1
            for k in range(i, j):
                for q in solve(temp[i][k], temp[k+1][j]):
                    if q not in temp[i][j]:
                        temp[i][j].append(q)
    return a in temp[0][len(arr)-1]
    # return temp

def solve(exp1, exp2):
    ans = []
    for e1 in exp1:
        for e2 in exp2:
            if e1 == 'a':
                if e2 == 'a' or e2 == 'b':
                    ans.append('b')
                else:
                    ans.append('a')
            elif e1 == 'b':
                if e2 == 'a':
                    ans.append('c')
                elif e2 == 'b':
                    ans.append('b')
                else:
                    ans.append('a')
            else:
                if e2 == 'b' or e2 == 'c':
                    ans.append('c')
                else:
                    ans.append('a')
    return ans



if __name__ == '__main__':
    # print count_coins_dp([1, 3, 5], 11)
    # print longest_nondecreasing_sequence_dp([5,3,4,8,6,7])
    # graph = {'A': ['B', 'C'],
    #          'B': ['C', 'D'],
    #          'C': ['D'],
    #          'D': ['F'],
    #          'E': ['F'],
    #          'F': ['F']}
    # path = []
    # shortest_path_recur(graph, 'A', 'E', path)
    #print Solution().palindromePairs(["bat","tab","cat"])
    # print HouseBurglar([])
    # print func([0,3,4,0,3])
    # print addStrings("123","12345")
    # print calc("1+5")
    # print max_subarray([1,-3,2,1,-1])
    # h = [0,200,410,610]
    # print HotelStops_dp(h)
    # print validString("itwasthebestoftimes")
    # graph = {1: [6, 2, 3, 4],
    #          2: [5, 1, 3, 4, 7],
    #          3: [6, 1, 2, 4, 7],
    #          4: [5, 1, 2, 3],
    #          5: [6, 2, 4],
    #          6: [5, 1, 3],
    #          7: [2, 3]}
    # mat = [[10,2,5],
    #        [8,20,10],
    #        [1,6,5],
    #        [5,10,12]]
    # print pebbleProblem(mat, graph)
    temp = mult("bac",'a')
    print temp
    # for i in range(len(temp)):
    #     print temp[i]

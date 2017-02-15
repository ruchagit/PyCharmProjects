def printSnakeString(str):
    str = str.replace(' ', '~')
    print str
    for i in range(2,len(str),4):
        print '   ',str[i],' ',
    print '\n',
    for i in range(1,len(str),2):
        print ' ',str[i],
    print '\n',
    for i in range(0,len(str),4):
        print str[i], '     ',
    print '\n'


def neuronyms(s):
    l = len(s)
    res = set()
    res.add(s[0] + str((l - 2)) + s[l-1])

    for i in range(l-3, 1, -1):
        for j in range(0, l-2-i+1, 1):
            res.add(s[0:j+1] + str(i) + s[i+j+1:])
            print res
    print res


def k_unique_in_substring(s,k):
    l = len(s)
    max_letters = 26
    cnt_letters = [0] * max_letters
    u = 0

    for i in range(l):
        if cnt_letters[ord(s[i]) - ord('a')] == 0:
            u += 1
        cnt_letters[ord(s[i]) - ord('a')] += 1

    if u < k:
        return

    cnt_letters = [0] * max_letters

    curr_start = 0
    curr_end = 0

    max_win_length = 1
    max_win_start = 0

    cnt_letters[ord(s[0]) - ord('a')] += 1

    for i in range(1, l):
        cnt_letters[ord(s[i]) - ord('a')] += 1
        curr_end += 1

        print s[curr_start:curr_end + 1]

        while not upto_k_unique(cnt_letters, k):
            cnt_letters[ord(s[curr_start]) - ord('a')] -= 1
            curr_start += 1
            #print curr_start
            #print cnt_letters[0:5]

        if curr_end - curr_start + 1 > max_win_length:
            max_win_length = curr_end - curr_start + 1
            max_win_start = curr_start


    return s[max_win_start : (max_win_start+max_win_length)]
    #return s[max_win_start:]


def upto_k_unique(arr, k):
    curr_k = 0
    for i in range(len(arr)):
        if arr[i] > 0:
            curr_k += 1
    return k >= curr_k

def min_window(s,t):
    slen = len(s)
    tlen = len(t)
    max_chars = 256
    need_to_find = [0] * max_chars
    count = 0
    begin = 0
    end = 0
    found = [0] * max_chars
    minwindowlen = float('inf')
    windowlen = 1
    minwindowbegin = 0
    minwindowend = 0

    for i in range(0,tlen):
        need_to_find[ord(t[i]) - ord('a')] += 1

    while end < slen:
        if need_to_find[ord(s[end]) - ord('a')] == 0:
            end += 1
            continue
        found[ord(s[end]) - ord('a')] += 1
        if found[ord(s[end]) - ord('a')] <= need_to_find[ord(s[end]) - ord('a')]:
            count += 1

        if count == tlen:
            while need_to_find[ord(s[begin]) - ord('a')] == 0 or \
                            found[ord(s[begin]) - ord('a')] > need_to_find[ord(s[begin]) - ord('a')]:
                if found[ord(s[begin]) - ord('a')] > need_to_find[ord(s[begin]) - ord('a')]:
                    found[ord(s[begin]) - ord('a')] -= 1
                begin += 1

        windowlen = end - begin + 1
        if count < tlen:
            minwindowlen = windowlen
            minwindowbegin = begin
            minwindowend = end
        elif count == tlen and windowlen <= minwindowlen:
            minwindowlen = windowlen
            minwindowbegin = begin
            minwindowend = end
        end += 1

    if count == tlen:
        return s[minwindowbegin:minwindowend+1]
    else:
        return


def kmp(text, pattern):
    tlen = len(text)
    plen = len(pattern)
    jump_to_array = [0] * plen

    j = 0
    i = 1
    while i < plen:
        if pattern[i] == pattern[j]:
            jump_to_array[i] = j+1
            j += 1
            i += 1
        else:
            while j > 0:
                j = jump_to_array[j-1]
                if pattern[i] == pattern[j]:
                    jump_to_array[i] = j + 1
                    j += 1
                    i += 1
                    break
            if j == 0:
                jump_to_array[i] = 0
                i += 1

    tptr = 0
    pptr = 0
    while tptr < tlen and pptr < plen:
        if pattern[pptr] == text[tptr]:
            tptr += 1
            pptr += 1
            if pptr == plen:
                return True
        else:
            if pptr == 0:
                tptr += 1
            else:
                pptr = jump_to_array[pptr - 1]
    return False

def palindrome_pairs(words):
    word_map = dict()
    l = len(words)
    if l <= 1:
        return
    for i in range(l):
        word_map[words[i]] = i
    for i in range(l):
        for j in range(len(words[i])):
            str1 = words[i][0:j]
            str2 = words[i][j:]
            if ispalindrome(str1):
                str2rvs = str2[::-1]
                if str2rvs in word_map and word_map.get(str2rvs) != i:
                    return i, word_map.get(str2rvs)
            if ispalindrome(str2):
                str1rvs = str1[::-1]
                if str1rvs in word_map and word_map.get(str1rvs) != i:
                    return i, word_map.get(str1rvs)
    return


def ispalindrome(s):
    lt = 0
    rt = len(s) - 1
    while lt <= rt:
        if s[lt] != s[rt]:
            return False
        lt += 1
        rt -= 1
    return True


def ismatch(strText, strPattern):
    tlen = len(strText)
    plen = len(strPattern)
    t = 0
    p = 0
    while t < tlen and p < plen:
        if strPattern[p] == '.':
            t += 1
            p += 1
        elif p < plen-1 and strPattern[p+1] == '*':
            if strPattern[p].isalpha():
                a = strPattern[p]
                while t < tlen and strText[t] == a:
                    t += 1
                p += 2
            else:
                return False
        else:
            if strPattern[p] == strText[t]:
                t += 1
                p += 1
            else:
                return False
    return True


#longest common subsequence : DP
def lcs(X, Y):
    # find the length of the strings
    m = len(X)
    n = len(Y)

    # declaring the array for storing the dp values
    L = [[None] * (n + 1) for i in xrange(m + 1)]

    """Following steps build L[m+1][n+1] in bottom up fashion
    Note: L[i][j] contains length of LCS of X[0..i-1]
    and Y[0..j-1]"""
    for i in range(m + 1):
        for j in range(n + 1):
            if i == 0 or j == 0:
                L[i][j] = 0
            elif X[i - 1] == Y[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # L[m][n] contains the length of LCS of X[0..n-1] & Y[0..m-1]
    return L[m][n]

'''
O(n^2)
'''
def longest_repeated_substring(s):
    N = len(s)
    substrings = set()
    for i in range(N, 0, -1):
        for j in range(0, N-i):
            for k in range(0, N-i):
                if k != j and s[j:j+i] == s[k:k+i]:
                        return s[j:j+i]
            #if s[j:j+i] in substrings:
             #   return s[j:j+i]
            #substrings.add(s[j:j+i])

def find_adjacent_chars(board,dictionaryList, word, i, j, visited, output):
    rows = len(board)
    cols = len(board[0])
    if word in dictionaryList :
        output.append(word)
        return
    visited[i][j] = True
    for a in range(max(0,i-1), min(rows,i+2)):
        for b in range(max(0,j-1), min(cols,j+2)):
            if not visited[a][b]:
                find_adjacent_chars(board,
                                    dictionaryList,
                                    word + board[i][j],
                                    a, b, visited, output)
    visited[i][j] = False

def find_words(dictionaryList, board):
    rows = len(board)
    cols = len(board[0])
    output = []
    visited = [0] * rows
    for x in range(rows):
        visited[x] = [False] * cols
    for i in range(rows):
        for j in range(cols):
            find_adjacent_chars(board, dictionaryList,
                                "", i, j, visited, output)

    return output

print find_words(["GEEKS", "FOR", "QUIZ", "GO"],
                  [['G','I','Z'],
                  ['U','E','K'],
                  ['Q','S','E']])
                  #[['G', 'E', 'E'],
                  #['K', 'S', 'Q'],
                  #['U', 'I', 'Z']])

if __name__ == '__main__':
    #print k_unique_in_substring('aabacbeaaaa', 3)
    #print min_window('adobecodebanc', 'zyd')
    #print kmp('abcxabcdabxabcdabcdabcy', 'abcdabcy')
    #print kmp('abxabcabcaby', 'xabca')
    #res = palindrome_pairs(['ba','a','aaa'])
    #res = palindrome_pairs(['taba', 'cat', 'bat'])
    #print res
    #print ismatch('aab', 'c*a*b')
    #X = "ABCDGH"
    #Y = "AEDFHR"
    #print "Length of LCS is ", lcs(X, Y)
    res = longest_repeated_substring('abadeabadefe')
    print res

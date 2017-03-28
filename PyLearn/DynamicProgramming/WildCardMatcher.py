'''
'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

'''
class Solution(object):
    def wild_card_dp(self, s, p):
        if (not s and not p) or (not s and p == "*"):
            return True
        if not p and s:
            return False
        mat = [[False for x in range(len(p)+1)] for x in range(len(s)+1)]
        mat[0][0] = True
        if p[0] == "*":
            mat[0][1] = True
        for c in range(2,len(p)+1):
            if p[c-1] == "*":
                mat[0][c] = mat[0][c-1]
        for r in range(1,len(s)+1):
            for c in range(1,len(p)+1):
                if p[c-1] == s[r-1] or p[c-1] == "?":
                    mat[r][c] = mat[r-1][c-1]
                elif p[c-1] == "*":
                    mat[r][c] = mat[r-1][c] or mat[r][c-1]
        return mat[len(s)][len(p)]

    '''
    For each element in s
    If *s==*p or *p == ? which means this is a match, then goes to next element s++ p++.
    If p=='*', this is also a match, but one or many chars may be available, so let us save this *'s position and the matched s position.
    If not match, then we check if there is a * previously showed up,
           if there is no *,  return false;
           if there is an *,  we set current p to the next element of *, and set current s to the next saved s position.

    e.g.

    abed
    ?b*d**

    a=?, go on, b=b, go on,
    e=*, save * position star=3, save s position ss = 3, p++
    e!=d,  check if there was a *, yes, ss++, s=ss; p=star+1
    d=d, go on, meet the end.
    check the rest element in p, if all are *, true, else false;
    '''

    def wild_card_iterative(self,s,p):
        s_cur = 0
        p_cur = 0
        match = 0
        star = -1
        while s_cur < len(s):
            if p_cur < len(p) and (s[s_cur] == p[p_cur] or p[p_cur] == '?'):
                s_cur = s_cur + 1
                p_cur = p_cur + 1
            elif p_cur < len(p) and p[p_cur] == '*':
                match = s_cur
                star = p_cur
                p_cur = p_cur + 1
            elif (star != -1):
                p_cur = star + 1
                match = match + 1
                s_cur = match
            else:
                return False
        while p_cur < len(p) and p[p_cur] == '*':
            p_cur = p_cur + 1

        if p_cur == len(p):
            return True
        else:
            return False


if __name__ == '__main__':
    sol = Solution()
    print sol.wild_card_dp("","")
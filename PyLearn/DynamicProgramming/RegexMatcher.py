'''
'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The key point to note here is the problem seems easy when you first read it. Seems close
to a state diagram.
But then, when you start coding up, you realize that covering all cases in impossible
iteratively coz, they repeat
Hence, recursion
Now its important that getting a * just blows everthing away since it can allow zero
of the letter.
This can take you for a round. Here its imp to realize that you should not look into for
this behavior, but rather just eliminate the pattern and check what happens
That gives rize to this recurrence:
if p[1] == "*":
    then
    case1) func(s, p[2:]) or
    case2) s should not be empty and
           p[0] == s[0] or p[0] == "." and
           func(s[1:],p)
else: ## we do not have a start, so the chars should match or the pattern should have .
    s should not be empty and
    s[0] == p[0] or p[0] == "." and
    func(s[1:],p[1:])

the base case for this recursion is pattern getting empty (since we keep check for string
in recursive calls) and we return value of s.empty
'''
class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if not p:
            if s: return False
            else: return True
        if 1 < len(p) and p[1] == "*":
            return self.isMatch(s, p[2:]) or \
                   (bool(s) and (s[0] == p[0] or p[0] == ".") and self.isMatch(s[1:],p))
        else:
            return bool(s) and (s[0] == p[0] or p[0] == ".") and self.isMatch(s[1:],p[1:])

    '''
    DP:
    rows - express expression(exp)
    columns - express pattern(pat)
    mat[r][c] - expresses whether a regex in valid upto the point exp[r] and pat[c]
    base values:
    mat[0][0] = T : empty pattern and empty string is valid
    mat[1...r][0] = F : exp but no pattern is incorrect
    mat[0][1...c] : needs thought
        if you get pat[c] == "*" then copy the value from 2 cols behind as if you are
        ignoring the pattern cz it allows zero occurences
        eg: exp = bb, pat = a*b*
        else False

    for remaining matrix:
    1) if pat[c] == exp[r] #alphabet match
        collect result when this match was not there i.e mat[r-1][c-1]
    2) if pat[c] == "." #any char ok
        collect result when this match was not there i.e mat[r-1][c-1]
    3) if pat[c] == "*"
        1) consider zero occurences (two columns behind) = mat[r][c-2] OR
        2) consider one occurence if the char in the exp is same as char before *
           i.e if exp[r] == pat[c-1] then take value from mat[r-1][c]
           This suggests that the current char in the exp could be one of from the *
           series. Hence consider it removed and take the vale
    4) False

    '''

    def isMatch_dp(self, s, p):
        mat = [[False for x in range(len(p)+1)] for x in range(len(s)+1)]
        mat[0][0] = True
        for c in range(1,len(p)+1):
            if p[c-1] == "*":
                mat[0][c] = mat[0][c-2]
        for r in range(1,len(s)+1):
            for c in range(1,len(p)+1):
                if p[c-1] == s[r-1] or p[c-1] == ".":
                    mat[r][c] = mat[r-1][c-1]
                elif p[c-1] == "*":
                    if mat[r][c-2]:
                        mat[r][c] = True
                    else:
                        if p[c-2] == s[r-1] or p[c-2] == ".":
                            mat[r][c] = mat[r-1][c]
        return mat[len(s)][len(p)]


if __name__ == '__main__':
    sol = Solution()
    s = "baccbbcbcacacbbc"
    p = "c*.*b*c*ba*b*b*.a*"
    print sol.isMatch_dp("bb",".bab")
def text_justify(words,L):
    if L == 0:
        return words
    if len(words) == 0:
        return words
    # O(n) where n is the length of the words list
    lines = fit_to_lines(words, L)
    res = []
    i = 0
    #O(m) where m is the number of lines formed
    while i < len(lines)-1:
        nw = len(lines[i][0])
        ns = nw - 1
        nc = lines[i][1]
        if nw == 1:
            lines[i][0].insert(1," "*nc)
        elif nc % ns == 0:
            s = nc // ns
            j = 1
            #O(k) where k is the number of words in this line
            while j < len(lines[i][0]):
                lines[i][0].insert(j, " "*s)
                j += 2
        elif nc % ns != 0:
            s = nc // ns
            s_extra = nc % ns
            j = 1
            # O(k) where k is the number of words in this line
            while j < len(lines[i][0]):
                lines[i][0].insert(j, " " * s)
                j += 2
            j = 1
            # O(k) where k is the number of words in this line
            while s_extra != 0:
                if j < len(lines[i][0])-1:
                    lines[i][0][j] += " "
                    j += 2
                else:
                    lines[i][1][j] += " "
                    j = 3
                s_extra -= 1
        i += 1
    #for last line
    lines[-1][1] -= (len(lines[-1][0])-1)
    j = 1
    while j < len(lines[-1][0]):
        lines[i][0].insert(j," ")
        j += 2
    lines[i][0].append(" "*lines[-1][1])
    #join every line together
    i = 0
    #O(m) number of lines
    while i < len(lines):
        s = ''.join(lines[i][0])
        res.append(s)
        i += 1
    return res


def fit_to_lines(words,L):
    lines = []
    i = 0
    while i < len(words):
        currL = 0
        curr = []
        lines.append([curr,L])
        while currL <= L and i < len(words):
            currL += len(words[i])
            if currL <= L:
                curr.append(words[i])
                lines[-1][1] -= len(words[i])
                i += 1
            currL += 1 #one space after each word
    return lines


if __name__ == '__main__':
    words = ["This", "is", "an", "example", "of", "text", "justification."]
    words1 = ["What","must","be","shall","be."]
    print text_justify(["a","b"],5)
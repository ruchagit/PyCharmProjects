# iterator on LOL
#[[2,3],[4,5,6],[7,8,9]]
class iterator:
    def __init__(self,lol):
        self.lol = lol
        self.currlist = 0
        self.curridx = -1
        self.next_ele = None

    def has_next(self):
        if len(self.lol) <= 0:
            return False
        elif self.currlist >= len(self.lol):
            return False
        else:
            if len(self.lol[self.currlist]) > 0:
                if self.curridx+1 < len(self.lol[self.currlist]):
                    self.curridx += 1
                    self.next_ele = self.lol[self.currlist][self.curridx]
                    return True
                else:
                    self.curridx = -1
                    self.currlist += 1
                    return self.has_next()
            else:
                self.currlist += 1
                return self.has_next()

    def next(self):
        if self.next_ele is not None:
            return self.next_ele

class Vector2D(object):
    def __init__(self, vec2d):
        """
        Initialize your data structure here.
        :type vec2d: List[List[int]]
        """
        self.s = []
        for row in reversed(vec2d):
            l = len(row)
            if l:
                self.s.append((l, iter(row)))

    def next(self):
        """
        :rtype: int
        """
        l, row_iter = self.s.pop()
        if l > 1:
            self.s.append((l-1, row_iter))
        return next(row_iter)

    def hasNext(self):
        """
        :rtype: bool
        """
        return bool(self.s)


if __name__ == '__main__':
    l = [[2,3],[4,5,6],[7,8,9]]
    l1 = [[],[],[1,2]]
    l2 = [[1,2],[],[]]
    l3 = [[],[]]
    l4 = []
    l5 = [[1,2]]
    i = Vector2D(l4)
    # i = iterator(l4)
    print i.s
    # while i.hasNext():
    #     print i.next()

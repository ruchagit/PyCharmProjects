import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        heap = []
        head = None
        k = len(lists)
        for i in range(k):
            if lists[i]:
                heapq.heappush(heap, (lists[i].val, lists[i]))
        while heap:
            currEle, currList = heapq.heappop(heap)
            if head is None:
                head = ListNode(currEle)
                currPtr = head
            else:
                currPtr.next = ListNode(currEle)
                currPtr = currPtr.next
            if currList.next:
                currList = currList.next
                heapq.heappush(heap, (currList.val, currList))
        return head

class Calculator(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s or len(s) == 0:
            return 0
        stack = []
        num = 0
        sign = '+'
        for i in range(len(s)):
            if s[i].isdigit():
                num = (num * 10) + int(s[i])
            if ((not s[i].isdigit) and s[i] != " ") or i == len(s)-1:
                if sign == "+":
                    stack.append(num)
                elif sign == "-":
                    stack.append(-num)
                elif sign == "*":
                    stack.append(stack.pop() * num)
                elif sign == "/":
                    stack.append(stack.pop() // num)
                sign = s[i]
                num = 0
        while stack:
            num += stack.pop()
        return num

if __name__ == '__main__':
    c = Calculator()
    print c.calculate("3+5*2-6/3")
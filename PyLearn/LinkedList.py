class ArbitaryLinkedList:
    def __init__(self,val):
        self.val = val
        self.next = None
        self.arbitrary = None

def makeArbitaryLinkedList(arr1,arr2):
    l1 = len(arr1)
    l2 = len(arr2)
    head = ArbitaryLinkedList(arr1[0])
    tail = head
    for i in range(1,l1):
        tail = insert_behind(arr1[i],head,tail)
    i = 0
    curr = head
    while i < l2 and curr is not None:
        p = head
        while p.val != arr2[i]:
            p = p.next
        curr.arbitrary = p
        curr = curr.next
        i += 1
    return head


def insert_behind(val, head, tail):
    if head is None:
        head = ArbitaryLinkedList(val)
        tail = head
    else:
        node = ArbitaryLinkedList(val)
        tail.next = node
        tail = tail.next
    return tail


def copyLinkedList(head):
    p = head
    while p is not None:
        newNode = ArbitaryLinkedList(p.val)
        newNode.next = p.next
        p.next = newNode
        p = p.next.next

    original = head
    copy = head.next
    copy_head = copy
    while copy.next is not None:
        copy.arbitrary = original.arbitrary.next
        original.next = copy.next
        copy.next = copy.next.next
        copy = copy.next
        original = original.next
    original.next = None
    return copy_head

def isCopyValid(head,copy_head):
    while head is not None and copy_head is not None:
        if head.val != copy_head.val:
            return False
        copy_head = copy_head.next
        head = head.next
    return True

class SuperStack:
    def __init__(self):
        self.top = None
        self.bottom = None

class SuperStackNode:
    def __init__(self, val):
        self.val = val
        self.below = None
        self.above = None

def superStack1(operations):
    s = SuperStack()
    for i in range(len(operations)):
        if 'push' in operations[i]:
            _, k = operations[i].split()
            val = int(k)
            s = push(s, val)
            peek(s)
        elif 'pop' in operations[i]:
            s = pop(s)
            peek(s)
        else:
            _, e, k = operations[i].split()
            e1 = int(e)
            k1 = int(k)
            s = inc(s, e1, k1)
            peek(s)
    # print_stack(s)

def push(s, val):
    if s.top is None:
        node = SuperStackNode(val)
        s.top = node
        s.bottom = node
    else:
        node = SuperStackNode(val)
        curr_node = s.top
        node.below = curr_node
        curr_node.above = node
        s.top = node
    return s

def pop(s):
    if s.top is None:
        return s
    else:
        node = s.top
        s.top = node.below
        node.below = None
        node.above = None
        return s

def inc(s, e, k):
    if s.top is None:
        return s
    else:
        b = s.bottom
        while e > 0:
            b.val += k
            b = b.above
            e -= 1
        return s


def print_stack(s):
    n = s.top
    if n is None:
        print 'EMPTY'
    while n is not None:
        print n.val
        n = n.below

def peek(s):
    n = s.top
    if n is None:
        print 'EMPTY'
    else:
        print n.val

def superStack(operations):
    s = []
    for i in range(len(operations)):
        if 'push' in operations[i]:
            _, k = operations[i].split()
            val = int(k)
            s.insert(0,val)
            print(s[0])
        elif 'pop' in operations[i]:
            s.remove(s[0])
            if not s:
                print 'EMPTY'
            else:
                print(s[0])
        else:
            _, e, k = operations[i].split()
            e1 = int(e)
            k1 = int(k)
            l = len(s)
            for i in range(l-e1, l):
                s[i] += k1
            print(s[0])

class LinkedList:
    def __init__(self,val):
        self.val = val
        self.next = None

def insert_at_back(head,tail,val):
    if head is None:
        head = LinkedList(val)
        tail = head
    else:
        node = LinkedList(val)
        tail.next = node
        tail = tail.next
    return tail

def reverse_k(arr,k):
    l = len(arr)
    head = LinkedList(arr[0])
    tail = head
    for i in range(1,l):
        tail = insert_at_back(head,tail,arr[i])
    print_linked_list(head)
    print '\n'
    new_head = head
    k -= 1
    while k > 0:
        new_head = new_head.next
        k -= 1
    p = head.next
    head.next = new_head.next
    while new_head is not head:
        tmp = p
        p = p.next
        tmp.next = head
        head = tmp
    print_linked_list(new_head)

def print_linked_list(head):
    p = head
    while p is not None:
        print p.val,
        p = p.next


def getIntersectionNode(headA, headB):
    """
    :type head1, head1: ListNode
    :rtype: ListNode
    """
    if headA is None or headB is None:
        return None
    listA = headA
    listB = headB
    ptrB = headB
    lenA = 1
    while listA.next is not None:
        lenA += 1
        listA = listA.next
    listA.next = headA
    i = 0
    while i < lenA:
        if listB:
            listB = listB.next
        else: return None
        i += 1
    ptr = listB
    if listB is None:
        return None
    listB = listB.next
    while listB != ptrB and listB != ptr:
        if listB is None:
            return None
        listB = listB.next
        ptrB = ptrB.next
    listA.next = None
    if listB == ptrB:
        return headB
    else:
        return None
if __name__ == '__main__':
    # head = makeArbitaryLinkedList([1,2,3,4,5],[3,1,5,3,2])
    # copy_head = copyLinkedList(head)
    # print isCopyValid(head,copy_head)
    #superStack(['push 4', 'pop', 'push 3', 'push 5', 'push 2', 'inc 3 1',
    #           'pop', 'push 1', 'inc 2 2', 'push 4', 'pop', 'pop'])
    # reverse_k([1,2,3,4,5],3)
    l1 = [1,3,5,7,9,11,13,15,17,19,21]
    l2 = [2]
    headA = LinkedList(1)
    tailA = headA
    headB = LinkedList(2)
    tailB = headB
    # for i in range(1,len(l1)):
    #     tailA = insert_at_back(headA,tailA,l1[i])
    node = getIntersectionNode(headB,headA)
    print node.val
import random
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

def print_linked_list(head):
    p = head
    while p is not None:
        print p.val,
        p = p.next

def shuffleLinkedList(head):
    if head is None:
        return head
    if head.next is None:
        return head
    splitHeads = splitLinkedList(head)
    splitHeads[0] = shuffleLinkedList(splitHeads[0])
    splitHeads[1] = shuffleLinkedList(splitHeads[1])
    newhead = shuffledMerge(splitHeads[0],splitHeads[1])
    return newhead


def splitLinkedList(head):
    head1, head2 = None, None
    curr1, curr2 = None, None
    curr = head
    while curr is not None:
        if head1 is None:
            head1 = curr
            curr1 = head1
            curr = curr.next
            curr1.next = None
        else:
            curr1.next = curr
            curr1 = curr1.next
            curr = curr.next
            curr1.next = None
        if curr is not None:
            if head2 is None:
                head2 = curr
                curr2 = head2
                curr = curr.next
                curr2.next = None
            else:
                curr2.next = curr
                curr2 = curr2.next
                curr = curr.next
                curr2.next = None
    result = [head1,head2]
    return result


def shuffledMerge(head1,head2):
    newhead = LinkedList(-1)
    curr = newhead
    curr1, curr2 = head1, head2
    while curr1 and curr2:
        choice = random.randint(1,10)
        if choice <= 5:
            curr.next = curr1
            curr = curr.next
            curr1 = curr1.next
            curr.next = None
        else:
            curr.next = curr2
            curr = curr.next
            curr2 = curr2.next
            curr.next = None
    if curr1:
        curr.next = curr1
    if curr2:
        curr.next = curr2
    return newhead.next


if __name__ == '__main__':
    arr = [1,2,3,4,5,6,56]
    head = LinkedList(arr[0])
    tail = head
    for i in range(1,len(arr)):
        tail = insert_at_back(head,tail,arr[i])
    newhead = shuffleLinkedList(head)
    print_linked_list(newhead)
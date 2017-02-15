import random

class BSTNode:
    def __init__(self,val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
        self.count = 1

'''
insert : inserts the given key in the BST with given root
parent is the parent node of the given root
every node in BST also has a count field giving the number
of nodes below it
'''
def insert(curr_node, parent, key):
    if curr_node is None:
        node = BSTNode(key)
        node.parent = parent
        if parent is not None:
            if key > parent.val:
                parent.right = node
            else:
                parent.left = node
    elif key > curr_node.val:
        curr_node.count += 1
        insert(curr_node.right, curr_node, key)
    else:
        curr_node.count += 1
        insert(curr_node.left, curr_node, key)

def BSTmin(root):
    if root.left:
        return BSTmin(root.left)
    else:
        return root

def BSTmax(root):
    if root.right:
        return BSTmax(root.right)
    else:
        return root

def BSTsuccessor(curr_node):
    if curr_node.right:
        return BSTmin(curr_node.right)
    else:
        key = curr_node.val
        curr_node = curr_node.parent
        while curr_node:
            if curr_node.val < key:
                curr_node = curr_node.parent
            else:
                break
        return curr_node


def BSTpredecessor(curr_node):
    if curr_node.left:
        return BSTmax(curr_node.left)
    else:
        key = curr_node.val
        curr_node = curr_node.parent
        while curr_node:
            if curr_node.val > key:
                curr_node = curr_node.parent
            else:
                break
        return curr_node

def BSTlevelorder(root):
    q = []
    q.append(root)
    while q:
        if q[0].left:
            q.append(q[0].left)
        if q[0].right:
            q.append(q[0].right)
        if q[0]:
            node = q.pop(0)
            print node.val, "->", node.count
                # node.parent.val if node.parent else "None"


def BSTpreorder(root):
    print root.val,
    if root.left:
        BSTpreorder(root.left)
    if root.right:
        BSTpreorder(root.right)

def BSTpostorder(root):
    if root.left:
        BSTpostorder(root.left)
    if root.right:
        BSTpostorder(root.right)
    print root.val,

def BSTdelete(keynode):
    if keynode.right is None and keynode.left is None:
        parent = keynode.parent
        if parent.right is keynode:
            parent.right = None
        else:
            parent.left = None
        keynode.parent = None
        del keynode
    elif keynode.right is None or keynode.left is None:
        parent = keynode.parent
        if keynode.right is None:
            child = keynode.left
        else:
            child = keynode.right
        if parent.left is keynode:
            parent.left = child
            child.parent = parent
        else:
            parent.right = child
            child.parent = parent
        del keynode
    else:
        pre = BSTpredecessor(keynode)
        val = pre.val
        pre.val = keynode.val
        keynode.val = val
        BSTdelete(pre)

def BSTsmallestK(root,k):
    rank = root.left.count + 1
    if rank == k:
        return collectK(root)
    elif rank > k:
        BSTsmallestK(root.left,k)
    else:
        BSTsmallestK(root.right,k-rank)

def BSTinorder(root):
    if root.left:
        BSTinorder(root.left)
    print root.val,
    if root.right:
        BSTinorder(root.right)

def collectK(root):
   return 0

def randomKey(root):
    selected = None
    count = 1
    q = []
    q.append(root)
    while q:
        node = q.pop(0)
        if 1.0/count >= random.random():
            selected = node
        choice = random.randint(0,1)
        if choice == 0 and node.left:
            q.append(node.left)
        elif node.right:
            q.append(node.right)
        count += 1
    return selected

def randomKey1(root,k):
    if root.left:
        rank = root.left.count + 1
    else:
        rank = root.count
    if rank == k:
        return root
    elif rank > k:
        return randomKey1(root.left, k)
    else:
        return randomKey1(root.right, k - rank)

if __name__ == '__main__':
    arr = [7,5,3,6,11,9,8,13]
    root, parent = BSTNode(arr[0]), None
    for i in range(1, len(arr)):
        insert(root, parent, arr[i])
    head1, head2, head3 = root, root, root
    res = [0] * 14
    for i in range(100000):
        choice = random.randint(1,len(arr))
        node = randomKey1(head1,choice)
        res[node.val] += 1
    print [res[x] for x in arr]
    # head1 = head1.right
    # BSTdelete(head1)
    # BSTlevelorder(head2)
    # BSTinorder(head1)
    # print "\n"
    # BSTpostorder(head1)
    # print "\n"
    # BSTpreorder(head1)
    # print "Min element:", BSTmin(head1).val
    # print "Max element:", BSTmax(head2).val
    # new = BSTsuccessor(head3)
    # print "Successor of 7:", new.val
    # print "Successor of 8:", BSTpredecessor(new).val
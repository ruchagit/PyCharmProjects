# Problem 6 (O(n^2))


class BSTNode():
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def getIndex():
    return constructTreeHelper.preIndex


def incrementIndex():
    constructTreeHelper.preIndex += 1


def constructTreeHelper(pre, low, high, size):
    # Base Case
    if (getIndex() >= size or low > high):
        return None

    root = BSTNode(pre[getIndex()])
    incrementIndex()

    # If the current subarray has only one element
    if low == high:
        return root

    # Search for the first element greater than root
    for i in range(low, high + 1):
        if (pre[i] > root.data):
            break

    # divide preorder array in two parts.
    root.left = constructTreeHelper(pre, getIndex(), i - 1, size)
    root.right = constructTreeHelper(pre, i, high, size)
    return root


def buildTree(pre):
    size = len(pre)
    constructTreeHelper.preIndex = 0
    return constructTreeHelper(pre, 0, size - 1, size)


if __name__ == '__main__':
    pre = [10, 5, 1, 7, 40, 50]
    root = buildTree(pre)
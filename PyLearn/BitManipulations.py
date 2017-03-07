def reverseBits(n):
    for i in range(16):
        n = swapBits(n, i, 32 - i - 1)
    return n

def swapBits(n, i, j):
    a = (n >> i) & 1
    b = (n >> j) & 1
    if (a ^ b) != 0:
        n ^= (1 << i) | (1 << j)
        return n
    return n

if __name__ == '__main__':
    print reverseBits(43261596)
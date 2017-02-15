def function1():
    sum=0
    for i in range(1,1000,1):
        if i%3 == 0 or i%5 == 0:
            sum=sum+i
    return sum

def function2():
    i=1
    j=2
    sum=2
    while i+j<=4000000:
        k=i+j
        i=j
        j=k
        if k%2 == 0:
            sum=sum+k
    return sum

def function3(n):
    i = 2
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
    return n


if __name__ == '__main__':
    print ('hi')
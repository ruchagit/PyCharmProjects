def match_pairs(nut, bolt, start, end):
    if start < end:
        pivot_idx = partition(nut, start, end, bolt[end])
        partition(bolt, start, end, nut[pivot_idx])
        match_pairs(nut, bolt, start, pivot_idx - 1)
        match_pairs(nut, bolt, pivot_idx + 1, end)


def partition(a, start, end, pivot):
    lt = start
    rt = start
    print(lt, rt)
    while rt < end:
        if a[rt] < pivot:
            a[rt], a[lt] = a[lt], a[rt]
            lt += 1
        elif a[rt] == pivot:
            a[rt], a[end] = a[end], a[rt]
            rt -= 1
        rt += 1
    a[lt], a[end] = a[end], a[lt]
    print(a)
    return lt


if __name__ == '__main__':
    nuts = [x for x in '@,#,$,%,^,&'.split(',')]
    bolts = [x for x in '$,%,&,^,@,#'.split(',')]
    match_pairs(nuts, bolts, 0, len(nuts)-1)
    print(nuts)
    print(bolts)


'''
@,#,$,%,^,&
$,%,&,^,@,#
n3,n2,n1,n4
b4,b2,b3,b1
'''
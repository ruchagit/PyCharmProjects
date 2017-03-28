def merge_two_times(l1,l2,t):
    i = 0
    j = 0
    while i<len(l1) and j<len(l2):
        if l1[i][0] < l2[j][0] or (l1[i][0] == l2[j][0] and l1[i][1] < l2[j][1]):
            t.append(l1[i])
            i+=1
        else:
            t.append(l2[j])
            j+=1
    while i<len(l1):
        t.append(l1[i])
        i+=1
    while j<len(l2):
        t.append(l2[j])
        j+=1

def find_free_slots(l1,l2):
    timetable = []
    res = []
    merge_two_times(l1,l2,timetable)
    print timetable
    latest_so_far = 0
    for i in range(len(timetable)-1):
        latest_so_far = max(latest_so_far,timetable[i][1])
        if timetable[i+1][0] > latest_so_far:
            res.append((latest_so_far,timetable[i+1][0]))
    return res

if __name__ == '__main__':
    print find_free_slots([(1,5),(10,14),(19,20),(21,24),(27,30)],
                          [(3,5),(12,15),(18,21),(23,24)])
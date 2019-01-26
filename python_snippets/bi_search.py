# bi search arr for the closest but not exceed val

def bi_search(arr, val):
    if len(arr) > 1:
        if arr[len(arr) / 2] > val:
            return bi_search(arr[0:len(arr) / 2], val)
        else:
            return bi_search(arr[len(arr) / 2:], val)
    else:
        if arr[0] <= val:
            return arr[0]
        else:
            return None


def execute(arr, val):
    print 'input array: {}, val: {}'.format(arr, val)
    print bi_search(arr, val)


execute(range(0, 20, 2), 8)
execute(range(0, 20, 2), 5)
execute(range(0, 20, 2), 2)
execute(range(0, 20, 2), 1)
execute(range(0, 20, 2), 0)
execute(range(0, 20, 2), -1)

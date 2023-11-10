import sys

count = None
a_list = None

for line in sys.stdin:
    if count is None:
        count = int(line.strip())
        continue
    a_list = [int(i) for i in line.strip().split(' ')]


def quick_sort(a_list):
    if len(a_list) <= 1:
        return a_list
    elif len(a_list) == 2:
        a_list.sort()
        print(' '.join([str(i) for i in a_list]))
        return a_list
    pivot = a_list[0]
    smaller_list = []
    greater_list = []
    for i in a_list[1:]:
        if i < pivot:
            smaller_list.append(i)
        else:
            greater_list.append(i)
    s = quick_sort(smaller_list)
    g = quick_sort(greater_list)
    print(' '.join([str(i) for i in s + [pivot] + g]))
    return s + [pivot] + g


quick_sort(a_list)

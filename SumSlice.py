def sumSlice(a):
    sums = []
    for x in range(len(a)):
        for y in range(x + 1, len(a)):
            if a[x] == a[y]:
                sum_ = a[x]
            else:
                sum_ = a[x] + a[y]
            sums.append(sum_)
    max_sum = max(sums)
    return max_sum


print(sumSlice([3, 2, -6, 4, 0]))

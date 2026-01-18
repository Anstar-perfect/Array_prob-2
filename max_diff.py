def max_diff(a,a_size):
    diff = 0
    for i in range(1,a_size):
        if a[i]>a[i-1]:
            diff+= a[i]-a[i-1]
    return diff

a = [202,103,343,903]
print('Max Differnce between element is',max_diff(a,len(a)))        
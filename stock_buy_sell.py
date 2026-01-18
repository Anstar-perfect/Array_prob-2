def profit(a,a_size):
    profit = 0
    for i in range(1,a_size):
        if a[i]>a[i-1]:
            profit+=a[i]-a[i-1]
    return profit


prices = [342,351,452,390,402,411,450]
profit = profit(prices,len(prices))
print('Max Profit :',profit)
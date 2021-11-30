import matplotlib.pyplot as plt

def get_count(mylist):
    count = 0
    for item in mylist:
        count = count + 1
    return count

def get_max(mylist):
    max_item = mylist[0]
    n = len(mylist)
    for i in range(1,n):
        item = mylist[i]
        if item > max_item:
            max_item = item
    return max_item

def get_min(mylist):
    min_item = mylist[0]
    n = len(mylist)
    for i in range(1,n):
        item = mylist[i]
        if item < min_item:
            min_item = item
    return min_item

def get_max_idx(mylist):
    max_item = mylist[0]
    max_idx = 0
    n = len(mylist)
    for i in range(1,n):
        item = mylist[i]
        if item > max_item:
            max_item = item
            max_idx = i
    return max_idx

def get_min_idx(mylist):
    min_item = mylist[0]
    min_idx = 0
    n = len(mylist)
    
    for i in range(1,n):
        item = mylist[i]
        if item < min_item:
            min_item = item
            min_idx = i
    return min_idx

def get_range(mylist):
    min_item = get_min(mylist)
    max_item = get_max(mylist)
    return [min_item, max_item]

def get_sum(mylist):
    total = 0
    for item in mylist:
        total = total + item
    return total

def get_squared_sum(mylist):
    total = 0
    for item in mylist:
        total = total + item*item
    return total

def get_mean(mylist):
    total = get_sum(mylist)
    n = len(mylist)
    mean = total/n
    return mean

def get_median(mylist):
    temp_list = mylist.copy()
    temp_list.sort()
    n = len(mylist)
    # n%2 means remainder after division by 2
    if n%2 == 1:
        # single middle value
        median_idx = int(n/2)
        median_value = mylist[median_idx]
    else:
        # two middle values
        median1_idx = int(n/2)
        median2_idx = int(n/2)-1
        median_value = mylist[median1_idx] + mylist[median2_idx]
    return median_value

def get_variance(mylist, mode="sample"):
    sum_x = get_sum(mylist)
    mean = get_mean(mylist)
    sum_xx = get_squared_sum(mylist)
    n = len(mylist)
    if mode == "sample":
        variance = ( (sum_xx-n*mean*mean)/(n-1) )
    else:
        variance = ( (sum_xx-n*mean*mean)/n )
    return variance

def get_stdev(mylist, mode="sample"):
    sum_x = get_sum(mylist)
    mean = get_mean(mylist)
    sum_xx = get_squared_sum(mylist)
    n = len(mylist)
    variance = get_variance(mylist, mode="sample")
    stdev = variance**0.5
    return stdev

def get_covariance(mylist1, mylist2, mode="sample"):
    
    x = mylist1
    y = mylist2
    n = len(x)
    
    mean_x = get_mean(mylist1)
    mean_y = get_mean(mylist2)
    
    sum_xy = 0
    for i in range(n):
        sum_xy = sum_xy + x[i]*y[i]
    
    if mode == "sample":
        covariance = ( (sum_xy-n*mean_x*mean_y)/(n-1) )
    else:
        covariance = ( (sum_xy-n*mean_x*mean_y)/n )
    
    return covariance

def get_correlation(mylist1, mylist2):
    x = mylist1
    y = mylist2    
    covariance = get_covariance(x, y)
    stdev_x = get_stdev(x)
    stdev_y = get_stdev(y)
    correlation = covariance/(stdev_x*stdev_y)
    return correlation

def get_linear_fit(mylist_x, mylist_y):
    # y = a + bx
    # b = cov/std(x)**2
    covariance = get_covariance(mylist_x, mylist_y)
    mean_x = get_mean(mylist_x)
    mean_y = get_mean(mylist_y)
    stdev_x = get_stdev(mylist_x)
    b = covariance/(stdev_x**2)
    a = mean_y - b*mean_x
    return [a,b]


def plot_data(mylist_x, mylist_y):
    
    fig = plt.figure()
    ax = fig.add_subplot()
    ax.plot(mylist_x, mylist_y, '*', label='data')
        
    results = get_linear_fit(mylist_x, mylist_y)
    a = results[0]
    b = results[1]
    
    eqn_str = f'eqn of fit: y = {a:.3f} + {b:.3f}x'
    
    min_x = min(mylist_x)
    max_x = max(mylist_x)
    x0 = min_x
    x1 = max_x
    y0 = a + b*x0
    y1 = a + b*x1
    
    ax.plot([x0, x1], [y0, y1], '-', label='fit')
    ax.legend()
    
    return
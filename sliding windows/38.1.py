
def most_weekly_sales(sales):
    l = 0
    r = 0

    window_sum = 0
    cur_max = 0

    while r < len(sales):
        window_sum += sales[r]
        r += 1
        if r - l == 7:
            cur_max = max(cur_max, window_sum)
            window_sum -= sales[l]
            l += 1
    return cur_max


sales = [0, 3, 7, 12, 10, 5, 0, 1, 0, 15, 12, 11, 1]

print(most_weekly_sales(sales))
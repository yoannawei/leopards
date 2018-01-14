def bestDays(arr):
    max_diff = arr[1] - arr[0]
    for i in range(len(arr)-1) in arr:
        diff = arr[i+1] - arr[i]
        if diff > max_diff:
            max_diff = diff
    return

arr = {17, 11, 60, 25, 150, 75, 31, 120}

bestDays(arr)
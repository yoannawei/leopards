def median(lst):
    n_lst = sorted(lst)
    if len(lst) % 2 ==0:
        return (n_lst[int(len(lst)/2)-1]+ n_lst[int(len(lst)/2)])/2
    else:
        return n_lst[(int(len(lst))/2)]

print(median([4,5,5,4]))
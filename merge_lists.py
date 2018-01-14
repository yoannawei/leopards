def my_function(my_list, alices_list):
    i, j = 0
    merge_lists = []
    while i < size(my_list):
        if my_list[i] < alices_list[j]:
            merge_lists.append(mylist[i])
            i++
        else:
            merge_lists.append(alices_list[j])
            j++
    return merge_lists

my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

print
merge_lists(my_list, alices_list)
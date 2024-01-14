numbers1 = [3, 13, 3, 4, 6]
numbers2 = [2, 2, 0, 4, 5]
numbers3 = [1, 3, 7, 7, 10]
all_numbers = [numbers1, numbers2, numbers3]


def calculate_average(list_to_append_to, index, list_of_lists, number_of_lists):
    sum = 0
    for num_lst in range(number_of_lists):
        sum += list_of_lists[num_lst][index]
    list_to_append_to.append(sum / number_of_lists)


"""
This function gets a list of lists (of the same size) of numbers, 
returns a list such that in each index, will be the average of the same index of all the lists in list  
"""


def average_list(lst):
    num_of_lists = len(lst)
    each_list_len = len(lst[0])  # we assume that the lists are of the same length
    average_lst = []
    for index in range(each_list_len):
        calculate_average(average_lst, index, lst, num_of_lists)
    return (average_lst)


print(average_list(all_numbers))
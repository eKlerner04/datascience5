import matplotlib.pyplot as plt
def mergeSort(list_to_sort):
    if len(list_to_sort) > 1:
        mid = len(list_to_sort) // 2
        left_half = list_to_sort[:mid]
        right_half = list_to_sort[mid:]

        mergeSort(left_half)
        mergeSort(right_half)

        left_index = 0
        right_index = 0
        sorted_index = 0

        while left_index < len(left_half) and right_index < len(right_half):
            if left_half[left_index] <= right_half[right_index]:
                list_to_sort[sorted_index] = left_half[left_index]
                left_index += 1
            else:
                list_to_sort[sorted_index] = right_half[right_index]
                right_index += 1
            sorted_index += 1

        while left_index < len(left_half):
            list_to_sort[sorted_index] = left_half[left_index]
            left_index += 1
            sorted_index += 1

        while right_index < len(right_half):
            list_to_sort[sorted_index] = right_half[right_index]
            right_index += 1
            sorted_index += 1




my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()
mergeSort(my_list)
x = range(len(my_list))
plt.plot(x, my_list)
plt.show()

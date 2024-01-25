def find_sub_array_with_sum_zero(arr):
    cumulative_sum = 0
    sum_indices = {0: -1}
    result = []

    for i, num in enumerate(arr):
        cumulative_sum += num

        if cumulative_sum in sum_indices:
            start_index = sum_indices[cumulative_sum] + 1
            end_index = i
            result = arr[start_index:end_index + 1]
            break

        sum_indices[cumulative_sum] = i

    return result


arr1 = [-5, 5, 2, 1, -3, -9]
arr2 = [3, 2, 5, 7, 8, 9]

result1 = find_sub_array_with_sum_zero(arr1)
result2 = find_sub_array_with_sum_zero(arr2)

print("result1: ", result1)
print("result2: ", result2)


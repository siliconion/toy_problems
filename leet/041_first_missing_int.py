def find_first_missing_int(input_array):
    unique_set = set(input_array)
    unique_positive_set = [i for i in unique_set if i > 0]
    length = len(unique_positive_set)
    index_array = [True for i in range(length)]    
    for i in unique_positive_set:
        if i < length - 1:
            index_array[i - 1] = False

    for i in index_array:
        if index_array[i]:
            return i - 1 
        return length + 1

input_arrays = [
[5,4,3,2,0,1],
[-3,9, 7, 0, -2, 7, 4]
]

for i in input_arrays:
    print i
    print find_first_missing_int(i)

# Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative numbers.
# If the input array is empty or null, return an empty array.
# Example
# For input [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15], you should return [10, -65].

# def count_positives_sum_negatives(arr):
    # store numbers > 0
    # store numbers < 0
    # store result
    # iterate over arr
    # add/append pos_numbers.count() to result
    # add/append sum_neg_numbers to result
def count_positives_sum_negatives(arr):
    pos = 0
    neg = []
    lst = list()
    for ele in arr:
        if ele > 0:
            pos += 1
        elif ele <= 0: 
            neg.append(ele)
    if len(arr) == 0:
        return lst
    return [pos, sum(neg)]

print(count_positives_sum_negatives([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14, -15]),[10,-65])
print(count_positives_sum_negatives([0, 2, 3, 0, 5, 6, 7, 8, 9, 10, -11, -12, -13, -14]),[8,-50])
print(count_positives_sum_negatives([1]),[1,0])
print(count_positives_sum_negatives([-1]),[0,-1])
print(count_positives_sum_negatives([0,0,0,0,0,0,0,0,0]),[0,0])
print(count_positives_sum_negatives([]),[])
"""
Build a sorting algorithm, inspired by Timsort, that takes advantage of the fact that 
real-world data is often already partly sorted

Modify the merge_sort function so that it identifies runs of already sorted data 
and uses insertion sort on unsorted sections only before merging sections

#### Rules
- Don't use `sorted()`
- Don't use `.sort()`
- You may use functions you've written yourself
- Your algorithm should work for lists of arbitrary length

Going further...
- Update your function to detect descending runs and reverse them.
- Update your function to break longer runs of unsorted data down into smaller sections 
(you decide what counts as a 'longer' run)
"""

def insertion_sort(numbers):
    """
    Sorts a list of values in ascending order in-place
    """

    for i in range(1, len(numbers)):

        value = numbers[i] # Store value at current postion in list

        j = i-1            

        # Shift earlier values in the list to the right if they are greater than the stored value
        while j>=0 and numbers[j]>value:
            numbers[j+1] = numbers[j]
            j -= 1

        # When a lower value is reached, insert the stored value after it
        numbers[j+1] = value


def merge(left, right):
    """
    Returns two already-sorted lists combined as a single sorted list
    """

    result = []
    i = 0
    j = 0
 
    while i < len(left) and j < len(right):
 
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1

        else:
            result.append(right[j])
            j += 1
 
    result += left[i:]
    result += right[j:]
 
    return result


def mergesort(numbers):
    """
    Sorts a list of values in ascending order in-place
    by sorting sections of data of maximum length 4 using 
    insertion sort, then merging increasingly large sections until a 
    single merged list achieved 
    """

    n = len(numbers)
    size = 4

    for start in range(0, n, size):

        section = numbers[start:start+size]

        # Insertion sort each section
        insertion_sort(section)

        # Replace section of original list with sorted section
        numbers[start:start+size] = section

    # Merge increasingly large sections until single merged list achieved 
    while size < n:
        for start in range(0, n, 2*size):
            left_section = numbers[start:start+size]
            right_section = numbers[start+size:start+2*size]

            merged = merge(left_section, right_section)

            numbers[start:start+len(merged)] = merged

        size *= 2



def my_timsort(numbers):
    """
    Sorts a list of values in ascending order in-place
    by sorting sections of data of maximum length 4 using 
    insertion sort, then merging increasingly large sections until a 
    single merged list achieved 
    """

    n = len(numbers)
    size = 4

    for start in range(0, n, size):

        section = numbers[start:start+size]

        # Insertion sort each section
        insertion_sort(section)

        # Replace section of original list with sorted section
        numbers[start:start+size] = section

    # Merge increasingly large sections until single merged list achieved 
    while size < n:
        for start in range(0, n, 2*size):
            left_section = numbers[start:start+size]
            right_section = numbers[start+size:start+2*size]

            merged = merge(left_section, right_section)

            numbers[start:start+len(merged)] = merged

        size *= 2


numbers = [38, 12, 27, 43, 9, 31, 18, 25, 3, 14]
my_timsort(numbers)
print(numbers)



# DATA STRUCTURE- LABORATORY EXERCISE
print("\nPROGRAMMED BY:")
print("IREANNE N. OMEGA")
print("BSCOE 2-2\n")

## QUICK SORT
def quick_sort(OwnArray, left, right):
    if left < right:
        partition_pos = partition(OwnArray, left, right)
        quick_sort(OwnArray, left, partition_pos - 1)
        quick_sort(OwnArray, partition_pos + 1, right)


def partition(OwnArray, left, right):
    i = left
    j = right - 1
    pivot = OwnArray[right]

    while i < j:
        while i < right and OwnArray[i] < pivot:
            i += 1
        while j > left and OwnArray[j] >= pivot:
            j -= 1

        if i < j:
            OwnArray[i], OwnArray[j] = OwnArray[j], OwnArray[i]

    if OwnArray[i] > pivot:
        OwnArray[i], OwnArray[right] = OwnArray[right], OwnArray[i]

        print("\t", OwnArray)

    return i

OwnArray = [53, 86, 25, 96, 79, 65, 37, 28, 80, 16]

## Print Statement
print("\n ===================== QUICK SORT =====================")
print("\n\t\tUnsorted Array List:\n\t\t", OwnArray, "\n")
print("\n-----------------------------------------------------------")
print("\t\tSelection Sorting:")
quick_sort(OwnArray, 0, len(OwnArray) - 1)
print("\n-----------------------------------------------------------")
print("\n\t\tSorted Array List:\n\t\t", OwnArray, "\n")
print("\n =========================================================")


# DATA STRUCTURE- LABORATORY EXERCISE
print("\nPROGRAMMED BY:")
print("IREANNE N. OMEGA")
print("BSCOE 2-2\n")

# Q U I C K  S O R T
def quick_sort(OwnArray, left, right):
    if left < right:
        partitionpos = partition(OwnArray, left, right)
        quick_sort(OwnArray, left, partitionpos - 1)
        quick_sort(OwnArray, partitionpos + 1, right)


def partition(OwnArray, left, right):
    i = left
    j = right - 1
    pivot = OwnArray[right]
    print("\n", pivot)

    while i < j:
        while i < right and OwnArray[i] < pivot:
            i += 1
        while j > left and OwnArray[j] >= pivot:
            j -= 1

        if i < j:
            OwnArray[i], OwnArray[j] = OwnArray[j], OwnArray[i]
            print("\t", OwnArray)

    if OwnArray[i] > pivot:
        OwnArray[i], OwnArray[right] = OwnArray[right], OwnArray[i]
        print("\t", OwnArray)

    return i

OwnArray = [53, 86, 25, 96, 79, 65, 37, 28, 80, 16]

# P R I N T  S T A T E M E N T
print("\n============================ QUICK SORT ==========================")
print("\n\t\t\t\t\t\tUnsorted Array List:\n\t\t\t", OwnArray, "\n")
print("\nSelection Sorting:")
quick_sort(OwnArray, 0, len(OwnArray) - 1)
print("\n\n\t\t\t\t\tSorted Array List:\n\t\t\t", OwnArray, "\n")
print("\n===================================================================")



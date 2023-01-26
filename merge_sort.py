# DATA STRUCTURE- LABORATORY EXERCISE
print("\nPROGRAMMED BY:")
print("IREANNE N. OMEGA")
print("BSCOE 2-2\n")

#===================== merge sort =======================
def merge_sort(OwnArray):
    if len(OwnArray) > 1:
        left_array = OwnArray[:len(OwnArray) // 2]
        right_array = OwnArray[len(OwnArray) // 2:]
        print("\t\t", left_array, right_array)

        merge_sort(left_array)
        merge_sort(right_array)

        print( left_array, right_array)

        i = 0
        j = 0
        k = 0
        while i < len(left_array) and j < len(right_array):
            if left_array[i] < right_array[j]:
                OwnArray[k] = left_array[i]
                i += 1
            else:
                OwnArray[k] = right_array[j]
                j += 1
            k += 1

        while i < len(left_array):
            OwnArray[k] = left_array[i]
            i += 1
            k += 1

        while j < len(right_array):
            OwnArray[k] = right_array[j]
            j += 1
            k += 1

    print(OwnArray)

OwnArray = [53, 86, 25, 96, 79, 65, 37, 28, 80, 16]

## Print Statement
print("\n ===================== MERGE SORT =====================")
print("\n\t\t\t\t\t\tUnsorted Array List:\n\t\t\t", OwnArray, "\n")
print("\n-----------------------------------------------------------")
print("\nSelection Sorting:")
merge_sort(OwnArray)
print("\n-----------------------------------------------------------")
print("\n\t\t\t\t\tSorted Array List:\n\t\t\t", OwnArray, "\n")
print("\n =========================================================")
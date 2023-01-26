# DATA STRUCTURE- LABORATORY EXERCISE
print("\nPROGRAMMED BY:")
print("IREANNE N. OMEGA")
print("BSCOE 2-2\n")

#===================== selection sort =======================
def selection_sort(OwnArray):
    for i in range (9):
        min_position = i
        for j in range(i, 10):
            if OwnArray[j] < OwnArray[min_position]:
                min_position = j

        temp_position = OwnArray[i]
        OwnArray[i] = OwnArray[min_position]
        OwnArray[min_position] = temp_position

        print(OwnArray)

OwnArray = [53, 86, 25, 96, 79, 65, 37, 28, 80, 16]

## Print Statement
print("\n ===================== SELECTION SORT =====================")
print("\n\t\t\t\t\t\tUnsorted Array List:\n\t\t\t", OwnArray, "\n")
print("\n-----------------------------------------------------------")
print("\nSelection Sorting:")
selection_sort(OwnArray)
print("\n-----------------------------------------------------------")
print("\n\t\t\t\t\tSorted Array List:\n\t\t\t", OwnArray, "\n")
print("\n =========================================================")
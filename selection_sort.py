# DATA STRUCTURE- LABORATORY EXERCISE
print("\nPROGRAMMED BY:")
print("IREANNE N. OMEGA")
print("BSCOE 2-2\n")

# S E L E C T I O N   S O R T
def selection_sort(OwnArray):
    for i in range (9):
        minposition = i
        for j in range(i, 10):
            if OwnArray[j] < OwnArray[minposition]:
                minposition = j

        temp_position = OwnArray[i]
        OwnArray[i] = OwnArray[minposition]
        OwnArray[minposition] = temp_position

        print(OwnArray)

OwnArray = [53, 86, 25, 96, 79, 65, 37, 28, 80, 16]

# P R I N T  S T A T E M E N T
print("\n========================= SELECTION SORT =====================")
print("\n\t\t\t\t\t\tUnsorted Array List:\n\t\t\t", OwnArray, "\n")
print("\nSelection Sorting:")
selection_sort(OwnArray)
print("\n\t\t\t\t\tSorted Array List:\n\t\t\t", OwnArray, "\n")
print("\n=============================================================")
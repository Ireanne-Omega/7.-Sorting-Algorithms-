# DATA STRUCTURE- LABORATORY EXERCISE
print("\nPROGRAMMED BY:")
print("IREANNE N. OMEGA")
print("BSCOE 2-2\n")

# I N S E R T I O N  S O R T
def insertion_sort(OwnArray):
    for i in range(1, len(OwnArray)):
        j = i
        while OwnArray[j - 1] > OwnArray[j] and j > 0:
            OwnArray[j - 1], OwnArray[j] = OwnArray[j], OwnArray[j-1]
            j -= 1

            print(OwnArray)

OwnArray = [53, 86, 25, 96, 79, 65, 37, 28, 80, 16]

# P R I N T  S T A T E M E N T
print("\n========================== INSERTION SORT ========================")
print("\n\t\t\t\t\t\tUnsorted Array List:\n\t\t\t", OwnArray, "\n")
print("\nSelection Sorting:")
insertion_sort(OwnArray)
print("\n\t\t\t\t\tSorted Array List:\n\t\t\t", OwnArray, "\n")
print("\n===============================================================")

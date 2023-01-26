# DATA STRUCTURE- LABORATORY EXERCISE
print("\nPROGRAMMED BY:")
print("IREANNE N. OMEGA")
print("BSCOE 2-2\n")

# B U B B L E  S O R T
def bubble_sort(OwnArray):
    for i in range(len(OwnArray) - 1, 0, -1):
        for j in range(i):
            if OwnArray[j] > OwnArray[j + 1]:
                temp_position = OwnArray[j]
                OwnArray[j] = OwnArray[j + 1]
                OwnArray[j + 1] = temp_position

                print(OwnArray)

OwnArray = [53, 86, 25, 96, 79, 65, 37, 28, 80, 16]

# P R I N T  S T A T E M E N T
print("\n=========================== BUBBLE SORT =======================")
print("\n\t\t\t\t\t\tUnsorted Array List:\n\t\t\t", OwnArray, "\n")
print("\nSelection Sorting:")
bubble_sort(OwnArray)
print("\n\t\t\t\t\tSorted Array List:\n\t\t\t", OwnArray, "\n")
print("\n==============================================================")
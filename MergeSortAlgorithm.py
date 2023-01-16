
def mergeSort(values, labels):
    if len(values and labels) > 1:

        r = len(values) // 2
        L = values[:r]
        M = values[r:]

        r2 = len(labels) // 2
        L2 = labels[:r2]
        M2 = labels[r2:]


        mergeSort(L, L2)
        mergeSort(M, M2)

        i = j = k = 0


        while i < len(L) and j < len(M):
            if L[i] < M[j]:
                values[k] = L[i]
                labels[k] = L2[i]
                i += 1
            else:
                values[k] = M[j]
                labels[k] = M2[j]
                j += 1
            k += 1

        while i < len(L) and i < len(L2):
            values[k] = L[i]
            labels[k] = L2[i]
            i += 1
            k += 1

        while j < len(M) and j < len(M2):
            values[k] = M[j]
            labels[k] = M2[j]
            j += 1
            k += 1

    return labels

def printList(values):
    for i in range(len(values)):
        print(values[i], end=" ")
    print()

def printList2(labels):
    for i in range(len(labels)):
        print(labels[i], end=" ")
    print()


if __name__ == '__main__':
    values = [1, 43, 4, 6, 4, 7]
    labels = ["kon", "osa", "pies", "kot", "qn", "qn2"]

    print(mergeSort(values, labels))

   # print("Sorted array is: ")
   # printList(values)
   # printList(labels)


class Sort:
    def mergeSort(self, alist):
        if len(alist) < 2:
            return alist
        mid = len(alist) // 2
        left = self.mergeSort(alist[:mid])
        right = self.mergeSort(alist[mid:])
        return self.mergeSortedArrary(left, right)

    def mergeSortedArrary(self, A, B):
        sortedArray = []
        i, j = 0, 0
        while i < len(A) and j < len(B):
            if A[i] < B[j]:
                sortedArray.append(A[i])
                i += 1
            else:
                sortedArray.append(B[j])
                j += 1
        sortedArray += A[i:]
        sortedArray += B[j:]
        return sortedArray


if __name__ == '__main__':
    unsortedArray = [6, 5, 3, 1, 8, 7, 2, 4]
    merge_sort = Sort()
    print(merge_sort.mergeSort(unsortedArray))

# Know how sorting algos work 
# Bubble Sort 
'''
bubble up the highest number 
O(n^2) comparing items in nested loops 
good space complexity 
'''
def bubbleSort(array):
    n = len(array)
    for i in range(n-1):
        for j in range(0, n-i-1):
            if array[j] > array[j+1]:
                temp = array[j]
                array[j] = array[j+1]
                array[j+1] = temp
    
numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
bubbleSort(numbers)
print(numbers)

#Selection Sort 
'''
Scan list for smallest element and swap for first element
O(n^2)
O(1) space complexity 
'''

def selectionSort(array):
    n = len(array)
    for i in range(n-1):
        minIndex = i
        for j in range(i+1, n):
            if array[minIndex] >= array[j]:
                minIndex = j
        array[i], array[minIndex] = array[minIndex], array[i]


    
numbers = [-1,99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
selectionSort(numbers)
print(numbers)

#Insertion Sort 
'''
useful when you think the list is almost sorted 
small data sets 
'''

def insertionSort(array):
    length = len(array)
    for i in range(1,length):
        key = array[i] 
        j = i - 1
        while j>= 0 and key < array[j]:
            array[j+1] = array[j]
            j -= 1
        array[j+1] = key

numbers = [-1,99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
insertionSort(numbers)
print(numbers)

#Merge Sort 
'''
    O(n log n)
    still comparing each elment 
    O(n) space complexity 
    divivde and conquer 
    keep splitting in half 
'''

def mergeSort(array):
    if len(array) > 1: 

        m = len(array)//2
        left = array[:m]
        right = array[m:]
        left = mergeSort(left)
        right = mergeSort(right)
        array = []

        while len(left) > 0 and len(right) > 0:
            if left[0] < right[0]:
                array.append(left[0])
                left.pop(0)
            else:
                array.append(right[0])
                right.pop(0)
        for i in left:
            array.append(i)
        for i in right: 
            array.append(i)
    return array

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
answer = mergeSort(numbers)
print(answer)

#Quick Sort 
'''
Pick a random pivot 
and compare all the elements to it 
and just need to sort to the left and right of the pivot after 
pick a new pivot and quick sort it again 
space Complexity (log(n))
average O(n log n) worst case O(n^2)
'''

def quickSort(array):
    return array

numbers = [99, 44, 6, 2, 1, 5, 63, 87, 283, 4, 0]
answer = quickSort(numbers)
print(answer)



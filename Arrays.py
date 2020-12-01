class Array:
    def __init__(self):
        self.length = 0
        self.data = {}

    def get(self, index):
        if self.length == 0:
            return None
        return self.data[index]

    def push(self, item):
        self.data[self.length] = item 
        self.length += 1 

    def pop(self):
        print(self.length)
        item = self.data[self.length-1]
        del self.data[self.length-1]
        self.length -= 1
        return item

    def delete(self,index):
        item = self.data[index]
        self.shiftItems(index)
        return item

    def shiftItems(self, index):
        for i in range(index,self.length-1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length -= 1 


'''
newArray = Array()
newArray.push("hi")
newArray.push("how")
newArray.push("are")
newArray.push("you")
newArray.delete(1)
print(newArray.data)
'''

#Reverse A String 
def reverse(str):
    #check input 
    if(str is None or len(str) == 0):
        return None
    rvs_str = ''
    for i in str:
        rvs_str = i + rvs_str
    return rvs_str


#uses extended slice syntax 
#[start,stop,step]
#start at the end of the string and end at the start
def reverse2(str):
    if(str is None or len(str) == 0):
        return None
    return str[::-1]

#print(reverse("andreea"))
#print(reverse2("andreea"))

def mergeSortedArrays(arr1, arr2):
    #check array inputs 
    #note to self parentheses important for or/and logic 
    if (arr1 is None or len(arr1) == 0) and (arr2 is None or len(arr2) == 0):
        return None
    #else arr1 valid arry 2 not valid vice versa 
    if arr1 is None or len(arr1) == 0:
        return arr2
    if arr2 is None or len(arr2) == 0: 
        return arr1

    mergedArray = []
    array1Item = arr1[0]
    array2Item = arr2[0]
    i1 = 1 
    i2 = 1

    while(array1Item or array2Item):
        if array1Item == None: 
            mergedArray += arr2[i2-1:]
            break
        if array2Item == None: 
            mergedArray += arr1[i1-1:]
            break
        if array1Item < array2Item:
            mergedArray.append(array1Item)
            if i1 < len(arr1):
                array1Item = arr1[i1]
                i1 += 1
            else:
                array1Item = None
        else:
            mergedArray.append(array2Item)
            if i2 < len(arr2):
                array2Item = arr2[i2]
                i2 += 1
            else:
                array2Item = None
    return mergedArray


#print(mergeSortedArrays([0,3,4,31], [4,6,30]))


#Interview Questions 
    


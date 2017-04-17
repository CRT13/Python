def QuickSort(list1):
   quickSort(list1,0,len(list1)-1)

def quickSort(list1,first,last):
   if first<last:

       splitpoint = partition(list1,first,last)

       quickSort(list1,first,splitpoint-1)
       quickSort(list1,splitpoint+1,last)


def partition(list1,first,last):
   pivotvalue = list1[first]
   leftindex = first+1
   rightindex = last

   done = False
   while not done:
       #Move through left/right indices as long as the values are smaller/greater
       #than pivotvalue and left/right indices do not contradict.
       while list1[leftindex] <= pivotvalue and leftindex <= rightindex:
           leftindex += 1
       while list1[rightindex] >= pivotvalue and rightindex >= leftindex:
           rightindex -= 1
       #If they contradict, break - just swap First-Right values
       if rightindex < leftindex:
           done = True
       #If they don't, first swap Left-Right values
       else:
           temp = list1[leftindex]
           list1[leftindex] = list1[rightindex]
           list1[rightindex] = temp
   #Swap First(CurrentPivot) & Right Values
   temp = list1[first]
   list1[first] = list1[rightindex]
   list1[rightindex] = temp
   return rightindex

list1 = [24,56,103,127,7,36,444,5,20]
print('Unsorted List: ',list1)
QuickSort(list1)
print('Sorted List: ',list1)

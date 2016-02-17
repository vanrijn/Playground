'''
Given two arrays/Lists (choose whatever you want to) with sorted and
non-intersecting intervals. Merge them to get a new sorted non intersecting
array/list.

Eg: 
Given: 
Arr1 = [3-11, 17-25, 58-73]; 
Arr2 = [6-18, 40-47]; 

Wanted: 
Arr3 = [3-25, 40-47, 58-73];
'''
arr1 = range(3,12)
arr1.extend(range(17,26))
arr1.extend(range(58,74))
print "arr1: %s" % str(arr1)

arr2 = range(6,19)
arr2.extend(range(40,48))
print "arr2: %s" % str(arr2)

'''
Approach:
size1 = size of arr1
size2 = size of arr2
save size3 as the size of arr1 + size of arr2
create arr3 with an initial size of size3, if initial size is available
create 2 index values, idxarr1, idxarr2, both are initially 0
iterate size3 - 1 times and for each iteration:
   if idxarr2 is greater than the size of arr2 - 1, or the next value of arr1
       is less than the next value of arr2:
           copy it into arr3
           increment idxarr1
   else if the idxarr1 is greater than the size of arr1 - 1, or the next value
       of arr2 is less than the next value of arr1:
           copy it into arr3
           increment idxarr2
'''
size1 = len(arr1)
size2 = len(arr2)
size3 = size1 + size2

arr3 = []

idxarr1 = 0
idxarr2 = 0

print "Size of arr1: %d, size of arr2: %d" % (size1, size2)

for idxarr3 in xrange(size3):
    print "Iteration %d in idxarr3 loop" % idxarr3
    if idxarr2 >= size2 or arr1[idxarr1] < arr2[idxarr2]:
        arr3.append(arr1[idxarr1])
        idxarr1 += 1
    elif idxarr1 >= size1 or arr2[idxarr2] < arr1[idxarr1]:
        arr3.append(arr2[idxarr2])
        idxarr2 += 1

print "combined arr3: %s" % str(arr3)

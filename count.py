def countsort(input):
    # initialize of sorted array
    sortedarray=[0 for i in range (0,len(input))]
    # print(sortedarray)
    # initialize Max number of the input Array
    maxVal=max(input)
    counts=[0 for i in range(maxVal+1)]
    # print(counts)

    for i in array:
        counts[i]+=1
   

    for i in range(1,maxVal):
        counts[i]=counts[i-1]+counts[i]
    print(counts)

    for i in range(0,(maxVal)):
        # print(i)
        ind = counts[input[i]]
        sortedarray[ind]=input[i]
        counts[input[i]]=counts[input[i]]-1  
        
   

        
    # # print(count array)
    # return counts

    # print(sortedarray)
    return sortedarray

    # # return input

array = [9,8,7,7,6,3,3,2,1,0]

result=countsort(array)
print(result)

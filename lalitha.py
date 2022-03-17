def findTotalDistance(input1,input2):
    count=0
    for i in range(input1-1):
        count+= abs(input2[i]-input2[i+1])
    return count

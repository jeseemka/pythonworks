arr=[1,2,3,4,5,7,8,9,10,2,5]
arr.sort()
count=1
for i in range(0,len(arr)-1):
    for j in range (i+1,len(arr)):
        ith_element=arr[i]
        jth_element=arr[j]
        difference=ith_element-jth_element
        if difference==0:
                 print(ith_element,end=",")
                 break
                 count+=1

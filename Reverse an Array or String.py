def reverse(arr,start,end):
    while(start!=end and start<end):
        arr[start],arr[end]=arr[end],arr[start]
        start+=1
        end-=1
        print(arr)
    
    return arr
    

arr=[1,2,3,4,5]    
arr2=[1, 2, 3, 4, 5, 6]
print(reverse(arr2,0,len(arr2)-1))
print(arr2[::-1])
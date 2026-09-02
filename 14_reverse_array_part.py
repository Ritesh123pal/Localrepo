# here's a function to reverse a part of an array from index s to index e.
def reverse_part(arr,s,e):
    while(s<e):
        
        temp=arr[s]
        arr[s]=arr[e]
        arr[e]=temp
        s=s+1
        e=e-1
arr=[2,3,4,5,6,7,8,9]
s=2
e=6
reverse_part(arr,s,e)
print(arr)      
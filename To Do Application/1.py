x=8
print(x)
def insertion_sort(arr):
    for i in range(1,len(arr)):
        key=arr[j]
        i=j-1
        while i>=0 and arr[j]>key:
            arr[i+1]=arr[i]
            i=i-1
            arr[i+1]=key
            return arr

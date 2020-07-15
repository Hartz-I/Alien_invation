import math as m

arr=[4,3,2,6,5,8,64,68421,55,4,8,56,8,4,5,8,7,4,8,6,89,7444,98,8,23,3543,216145,4]

while True:
    i = 0
    while i<=len(arr)-2:
        if arr[i]>=arr[i+1]:
            first_n=arr[i]
            arr[i]=arr[i+1]
            arr[i+1]=first_n



        i+=1

    print(arr)

    if arr==sorted(arr):
        break
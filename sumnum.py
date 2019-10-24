#the closest numbers to the target numbers

def sumnum(arr1,arr2,num):
    target=0
    band=False
    if(num>0):
        for i in arr1:
            target=num-i
            for j in arr2:
                if (target==j):
                    band=True
                    print("The numbers are: ",i,':',j)
                    return 0
            if (i==arr1[(len(arr1))-1]):
                sumnum(arr1,arr2,num-1)

    else:
        print("We did not find the numbers")

arr1=[1,3,5,7]
arr2=[2,6,8,1]
num=2

sumnum(arr1,arr2,num)




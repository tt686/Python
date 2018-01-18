def odd_even():
    for x in range(1,20):
        if x % 2 != 0:
            print "Number is",x,"This is an odd number."
        else:
            print "Number is",x,"This is an even number."

odd_even()

Version 1 
def multiply():
    arr = [9, 15, 12, 26, 28]
    for x in range(0, len(arr)):
        arr[x] = arr[x] * 8
    print arr

print multiply()

Version 2
def multiply2(num,arr):
    for x in range(0, len(arr)):
        arr[x]= arr[x] * num
    print arr

multiply2(8,[9, 15, 12, 26, 28])

Version 3
def multiply3(num,arr):
    for x in range(0, len(arr)):
        arr[x] *= num
    print arr

arr = [9, 15, 12, 26, 28]
num = 8

multiply3(num, arr)



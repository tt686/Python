# 1 Multiples
#     part I:
num = 1000
for i in range (0,num):
    if i % 2 != 0:
        print i

#     part II:
num1 = 5
num2 = 100 #-->original value was 1 million. Shortened to 100 for simplicity.
def MultofFive(num1,num2):
   for i in range (num1, num2):
       if i % 5 == 0:
           print i
MultofFive(num1,num2)  

# 2 Sum List
def sumList(arr):
    sum = 0
    for i in range (0,len(arr)):
        sum += arr[i]
    print sum
sumList([1,2,5,10,255,3])

# 3 Average List
def avgList(arr):
    sum = 0
    for i in range (0, len(arr)):
        sum += arr[i]
    avg = sum/len(arr)
    print avg
avgList([1,2,5,10,255,3])

words = "It's thanksgiving day. It's my birthday, too!"
print words
#It's thanksgiving day. It's my birthday, too!
print words.find('day')
#18

print words.replace('day', 'month')
#It's thanksgiving month. It's my birthmonth, too!

x = [2,54,-2,7,12,98]
print max(x), min(x)
# 98,-2

x = ["hello",2,54,-2,7,12,98,"world"]
print x[0],x[-1]
# hello world

x = [19,2,54,-2,7,12,98,32,10,-3,6]
x.sort()
print x
# [-3, -2, 2, 6, 7, 10, 12, 19, 32, 54, 98]
x = sorted(x)
left_x = x[:len(x)/2]
right_x = x[len(x)/2:]

print left_x
# [-3, -2, 2, 6, 7]
print right_x
#[10, 12, 19, 32, 54, 98]

right_x.insert(0,left_x)
print right_x
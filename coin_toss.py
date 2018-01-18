# x = .23945593
# y = .798839238
# x_rounded = round(x)
# # x_rounded will be rounded down to 0
# y_rounded = round(y)
# # y_rounded will be rounded up

import random

def toss(reps):
    print "Starting the program..."
    head = 0
    tail = 0
    for count in range(1,reps):#set parametrs w/ start and finish. This will toss the coin 50 times.
        random_num = random.randint(0,1)
        if random_num <.50:
            x = round(random_num)
            head += 1
            print "Attempt #", count, ": Throwing a coin ... It's a head! ... Got ", head," head(s) so far and ",tail," tail(s) so far"
        else:
            y = round(random_num)
            tail += 1
            print "Attempt #", count, ": Throwing a coin ... It's a tail! ... Got ", head," head(s) so far and ",tail," tail(s) so far"
    print "Ending the program, thank you!"
toss(5001)
import random
# the random function will return a floating point number, that is 0.0 <= random_num < 1.0
#or use...

def grade():#create function
    print "Scores and Grades"#print first statement
    for x in range(1,10):#set parameters w/ start and finish. This will run loop 10 times.
        random_num = random.randint(60,101)#set value of variable to random.randint function
        if random_num >= 60 and random_num <=69:
            print "Score: ", random_num,"; Your grade is D"
        elif random_num >= 70 and random_num <=79:
            print "Score: ", random_num,"; Your grade is C"
        elif random_num >= 80 and random_num <=89:
            print "Score: ", random_num,"; Your grade is B"
        elif random_num >= 90 and random_num <=100:
            print "Score: ", random_num,"; Your grade is A"
        else:
            print "You failed"
    print "End of the program. Bye!"

grade()
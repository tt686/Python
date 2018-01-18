def draw_stars():#Parameter inside funcion. Don't need to pass it thru as argument when calling functionat the end
    x = [4,6,1,3,5,7,25]
    for i in x:#i is referring to the value at the 0 index and so forth. NOT the index itself
        print "*" * i
draw_stars()

def draw_stars2():
    x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]
    for i in x:# i is referring to the value at the 0 index and so forth. NOT the index itself
        if type(i) == int:
            print("*" * i)
        elif type(i) == str:
            print(i[0].lower() * len(i))
draw_stars2()
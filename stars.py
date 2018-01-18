x = [4,6,1,3,5,7,25]#Parameter outside of function. Must pass it thru as argument when calling function at the end
def draw_stars(container):
    stars = "*"
    for i in container:
        print i * stars
    return
    
print draw_stars(x)

x = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]#select the index with a string and use the .lower() method to take the first letter of the string and multiply it by the length of the string
def draw_part2(container):
    stars = "*"
    for i in container:
        if type(i) == int:
            print i * stars
        elif type(i) == str:
            print i[2].lower() * len(i)
draw_part2(x)

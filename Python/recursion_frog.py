# there is a river with the length of 12ft
# there are 11 rocks evenly spread across the river, 1ft apart
# the distance between the ends of the river and the rocks is also 1ft
# there is a frog that wants to jump to the other side of the river
# the frog can at any point jump 1ft or 2ft forward
# how many possible ways the frog can reach the end?

combinations = 0
river_length = 4


def jump(step):
    global combinations
    if step == river_length:
        combinations += 1
    else:
        if step < river_length:
            jump(step+1)
        if step < river_length-1:
            jump(step+2)
    return


jump(0)
print(combinations)

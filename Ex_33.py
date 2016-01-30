i = 0
numbers = []

while i < 6:
    print "At the top i is %d" % i
    numbers.append(i)

    print "Numbers now: ", numbers
    i += 1
    print "At the bottom i is %d" % i


print "The numbers: "

for num in numbers:
    print num


# Rewriting to a function


def make_list(list_length, list_increment):
    j = 0
    make_numbers = []
    while j < list_length:
        make_numbers.append(j)
        j = j + list_increment
    return make_numbers


def make_list_range(list_length, list_increment):
    make_numbers = list(range(0, list_length, list_increment))
    return make_numbers


print "Generated list with make_list: ", make_list(9, 2)
print "Generated list with make_list_range: ", make_list_range(9, 2)

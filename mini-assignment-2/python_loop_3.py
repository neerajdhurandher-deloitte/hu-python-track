import utils as utils


def upper_triangle_body(mid, space, stars):
    utils.print_space(space)
    if mid > 0:
        utils.print_star(stars)
    utils.print_space(2 * mid - 1)
    utils.print_star(stars)
    utils.print_next_line()


def upper_triangle(height):
    for i in range(height - 1):
        space = (height - i)
        upper_triangle_body(i, space, 1)
    utils.print_space(1)
    print('*' * ((2 * height) - 1))


def right_hand_triangle(height):
    for i in range(height, 0, -1):
        utils.print_space(height - i)
        utils.print_star(1)
        if i == height:
            utils.print_star(height-2)
        else:
            utils.print_space(i-2)
        if i > 1:
            utils.print_star(1)
        utils.print_next_line()



inputHeight = input("Enter height of upper triangle :- ")
upper_triangle(int(inputHeight))

inputHeight = input("Enter height of right hand triangle :- ")
right_hand_triangle((int(inputHeight)))


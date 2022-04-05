import utils as utils


def triangle_body(space, stars):
    utils.print_space(space)
    utils.print_star(stars)
    utils.print_space(space)
    utils.print_next_line()


def draw_pattern(n):
    for i in range(n + 1):
        stars = (2 * i) - 1
        space = int((2 * (n - i)) / 2)
        triangle_body(space, stars)

    for i in range(1, n + 1):
        stars = (2 * (n - i)) - 1
        space = int((2 * i) / 2)
        triangle_body(space, stars)


input_item = input("Enter number of rows :- ")
draw_pattern(int(input_item))

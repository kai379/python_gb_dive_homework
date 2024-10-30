from sys import argv
from guess_the_number_game import guess_the_number


if __name__ == '__main__':
    if len(argv) == 2:
        number_of_attempts_new = int(argv[1])
        guess_the_number(number_of_attempts=number_of_attempts_new)
    elif len(argv) == 3:
        max_num_new, number_of_attempts_new = map(int, argv[1:])
        guess_the_number(max_num=max_num_new, number_of_attempts=number_of_attempts_new)
    elif len(argv) == 4:
        min_num_new, max_num_new, number_of_attempts_new = map(int, argv[1:])
        guess_the_number(min_num=min_num_new, max_num=max_num_new, number_of_attempts=number_of_attempts_new)

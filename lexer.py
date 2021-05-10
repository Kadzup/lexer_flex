# %%

import os

m = ("Keyword Cancel", "Keyword Call", "Number")

states = (
    (1, 4, 0, 0, 0, 0, -4),
    (2, 4, 0, 0, 0, 0, -4),
    (3, 4, 0, 0, 0, 0, -4),
    (-1, 4, 0, 0, 0, 0, -4),
    (1, 4, 5, 0, 0, 0, -4),
    (1, 4, 0, 6, 7, 0, -4),
    (1, 4, 0, -2, 0, 0, -4),
    (1, 8, 0, 0, 0, 0, -4),
    (1, 4, 5, 0, 0, 9, -4),
    (1, 4, 0, -3, 0, 0, -4)
)


def rec_symbol(s: str) -> int:
    if s in ('1', '2', '3'):
        return 0
    elif s == 'c':
        return 1
    elif s == 'a':
        return 2
    elif s == 'l':
        return 3
    elif s == 'n':
        return 4
    elif s == 'e':
        return 5
    else:
        return 6


def write_to_file(message, *args):
    with open("output.txt", "a+") as file:
        file.write(message)
        file.write('\n')
        for arg in args:
            file.write(arg)
            file.write('\n')


def parse(string: str):
    st, i, begin = 0, 0, 0
    while i < len(string):
        symbol = string[i]
        cl = rec_symbol(symbol)

        st = states[st][cl]

        if st == 1 or st == 4 or st == 0:
            begin = i
        if st == 5:
            begin = i - 1
        i += 1

        if st == -1 or st == -2 or st == -3:
            to_write = string[begin:i]
            write_to_file("<{token}, {type}>".format(
                token=m[st], type=to_write))
            st = 0
            begin = i
        elif st == -4:
            st = 0
            begin = i


line_num = 1
with open("input.txt", "r") as line:
    lines = line.readlines()

os.remove("output.txt")

for line in lines:
    line_clear = line.split('\n')[0]

    write_to_file("\nLine %i" %
                  line_num, "Text:", line_clear)

    parse(line_clear)

    line_num += 1

# %%

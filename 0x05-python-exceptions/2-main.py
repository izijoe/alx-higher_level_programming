12
nb_print: 2
12345
nb_print: 5
12345Traceback (most recent call last):
    File "./2-main.py", line 14, in <module>
    nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
    File "/0x05/2-safe_print_list_integers.py", line 7, in safe_print_list_integers
    print("{:d}".format(my_list[i]), end="")
    IndexError: list index out of range

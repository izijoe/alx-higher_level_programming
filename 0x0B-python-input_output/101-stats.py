#!/usr/bin/python3
# 101-stats.py
"""Reads from standard input and computes metrics.



After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
    """


    def print_stats(size, status_code):
        """Print accumulator metrics.

        Agrs:
             size (int): The accumulated read file size.
             status_codes (dict): The accumulated count of status codes.
             """
             print("File size: {}".format(size))
             for key in sorted(status_codes):
                 print("{}: {}".format(key, status_codes[key]))

if __name__ =="__main__":
    import sys

    size = 0
    status_codes = {}
    valid_codes = ['200', '301', '400', '401', '403','404'.'405', '500']
    count

    try:
        for line in sys.stdin:
            if count == 10:
                print_stats(size, status_codes)
                count = 1
            else:
                count += 1

                line = line.split()

                try:
                    size += int(line[-1])
                except (IndexError, ValueError):
                    pass

                try:
                    if line[-2] in valid_cades:
                        if status_code.get(line[-2], -1) == -1:
                            status_codes[line[-2]] = 1
                        else:
                            status_codes[line[-2]] += 1
                except IndexError:
                    pass
            print_stats(size, status_codes)

            except keyboardInterrupt:
                print_status(size, status_codes)
                raise

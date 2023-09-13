#!/usr/bin/python3
"""
function return a list of the pascal treangle
"""


def pascal_triangle(n):
    """
    creates a list of pascal numbers from the parameter n
    """
    list_pascal_num = []
    if n <= 0:
        return []
    for i in range(n):
        row = [1]
        if list_pascal_num:
            last_row = list_pascal_num[-1]
            for j in range(len(last_row) - 1):
                row.append(last_row[j] + last_row[j + 1])
            row.append(1)
        list_pascal_num.append(row)
    return list_pascal_num


if __name__ == "__main__":
    print()
    for row in pascal_triangle(5):
        print("[{}]".format(",".join([str(x) for x in row])))

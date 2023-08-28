#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    result = list()
    for i in range(max(len(my_list_1), len(my_list_2))):
        try:
            result.append(my_list_1[i] / my_list_2[i])
        except ZeroDivisionError:
            print("division by 0")
            result.append(0)
        except TypeError:
            print("wrong type")
            result.append(0)
        except IndexError:
            print("out of range")
            result.append(0)
    return result

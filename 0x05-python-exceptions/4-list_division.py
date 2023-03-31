#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    """Divides tow lists element by element.

    Args:
        my_list_1 (list): The first list.
        my_list_2 (list): The second list.
        list_length (int): The number of elements to divide.
    Returns:
        A new list of length list_length containing all the divisions.
    """
    new_list = []
    for i in range(list_length):
        try:
            div_result = my_list_1[i]/my_list_2[i]
        except ZeroDivisionError:
            print("division by 0")
            div_result = 0
        except TypeError:
            print("wrong type")
            div_result = 0
        except IndexError:
            print("out of range")
            div_result = 0
        finally:
            new_list.append(div_result)
    return new_list

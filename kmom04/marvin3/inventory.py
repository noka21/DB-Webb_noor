
"""
here
"""


def pick(backpack_func, pick_list_func, pick_list_index=None):
    """
    here
    """
    
    if pick_list_index is None:
        backpack_func.append(pick_list_func)
        print(f"{pick_list_func} has been added on the list ")   

    elif len(backpack_func) < int(pick_list_index) :
        print(f"Error, {pick_list_index} is too high index")

    else:
            
        backpack_func.insert(int(pick_list_index), pick_list_func)
        print(f"{pick_list_func} has been added on the list in {pick_list_index} position")
    return backpack_func


def inventory(backpack_func):
    """
    here
    """
    x=len(backpack_func)
    print(f"there are {x} in the list:\n {backpack_func}")



def drop(backpack_func,drop_list_func):
    """
    here
    """
    try:
        backpack_func.remove(drop_list_func)
        print(f"{drop_list_func} has been deleted from the list ")
    except ValueError:
        print("Error")
        print(f"{drop_list_func} is not in list")
    return backpack_func



def swap(backpack_funk,list_swap_1,list_swap_2):
    """
    here
    """
    if len(backpack_funk)==0:
        print("Error there is no {list_swap_1} or {list_swap_2}")
    if list_swap_1==list_swap_2:
        print("Error, {list_swap_1} is the same as {list_swap_2}")

    elif list_swap_1  not in backpack_funk or list_swap_2  not in backpack_funk :
        print(f"Error  {list_swap_1} or  {list_swap_2}  is not in list")
    else:
        index_list_swap_1=backpack_funk.index(list_swap_1)
        index_list_swap_2=backpack_funk.index(list_swap_2)
        
        temp=backpack_funk[index_list_swap_1]
        backpack_funk[index_list_swap_1]=backpack_funk[index_list_swap_2]
        backpack_funk[index_list_swap_2]=temp


        print(f"{list_swap_1} changed position with {list_swap_2} ")
    return backpack_funk

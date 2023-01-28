def permute_set(set_str):
    """Permute elements of a set of length 3."""
    set_elements = set_str[1:-1] # remove curly braces
    # set_elements = set_elements.strip("}{") # alternative

    final_set = "{"
    for first in set_elements:
        rest = set_elements.replace(first,'')
        for second in rest:
            third = rest.replace(second,'')
            element = first + second + third
            final_set += element + ", "
    else:
        final_set = final_set[:-2] # remove trailing comma and space
        final_set += "}"

    print(final_set)
    

def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """
    #make phrase into list
    #iterate over list
    #if char.casefold() = to_swap.casefold()
    #char.swapcase()
    #join new list and return

    return ''.join([char.swapcase() if char.casefold() == to_swap.casefold() else char for char in phrase])

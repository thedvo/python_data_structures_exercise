def flip_case(phrase, to_swap):
    """Flip [to_swap] case each time it appears in phrase.

        >>> flip_case('Aaaahhh', 'a')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'A')
        'aAAAhhh'

        >>> flip_case('Aaaahhh', 'h')
        'AaaaHHH'

    """

    lst = []

    for char in phrase:
        if char.lower() == to_swap.lower():
            lst.append(char.swapcase())
        else:
            lst.append(char)

    return "".join(lst)

def list_check(lst):
    """Are all items in lst a list?

        >>> list_check([[1], [2, 3]])
        True

        >>> list_check([[1], "nope"])
        False
    """

    for val in lst:
        if not isinstance(val, list):
            return False
        else:
            return True

    # return all(isinstance(item, list) for item in lst)

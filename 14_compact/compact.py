def compact(lst):
    """Return a copy of lst with non-true elements removed.

        >>> compact([0, 1, 2, '', [], False, (), None, 'All done'])
        [1, 2, 'All done']
    """
    return list(filter(bool, lst))

    # truthy_list = []
    # for item in list:
    #     if(bool(item)):
    #         truthy_list.append(item)
    # return truthy_list

    # return [val for val in lst if val]

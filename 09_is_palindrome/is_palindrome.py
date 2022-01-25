def is_palindrome(phrase):
    """Is phrase a palindrome?

    Return True/False if phrase is a palindrome (same read backwards and
    forwards).

        >>> is_palindrome('tacocat')
        True

        >>> is_palindrome('noon')
        True

        >>> is_palindrome('robert')
        False

    Should ignore capitalization/spaces when deciding:

        >>> is_palindrome('taco cat')
        True

        >>> is_palindrome('Noon')
        True
    """

    ignore_caps_spaces = phrase.lower().replace(' ', '')
    return ignore_caps_spaces == ignore_caps_spaces[::-1]

    # entered_phrase = phrase.lower().replace(" ", "")
    # reverse = phrase[::-1].lower().replace(" ", "")

    # if entered_phrase == reverse:
    #     return True

    # else:
    #     return False

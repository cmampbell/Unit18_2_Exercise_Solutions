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
    #Get rid of spaces
    no_space_phrase = phrase.replace(' ', '')
    #Get reverse phrase
    reversed_list = list(no_space_phrase)
    reversed_list.reverse()
    reversed = ''.join(reversed_list)
    #Return bool with results
    return no_space_phrase.upper() == reversed.upper()

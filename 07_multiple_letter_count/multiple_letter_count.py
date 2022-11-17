def multiple_letter_count(phrase):
    """Return dict of {ltr: frequency} from phrase.

        >>> multiple_letter_count('yay')
        {'y': 2, 'a': 1}

        >>> multiple_letter_count('Yay')
        {'Y': 1, 'a': 1, 'y': 1}
    """
    # return { += 1 if ([char]) else [char] for char in phrase}

    #check is key exists in dictionary
    #if it does, += 1
    #else make key in dictionary

    letter_count = {}
    for char in phrase:
        if (char in letter_count):
            letter_count[char] += 1
        else:
            letter_count[char] = 1
    return letter_count
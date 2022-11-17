def truncate(phrase, n):
    """Return truncated-at-n-chars version of  phrase.
    
    If the phrase is longer than, or the same size as, n make sure it ends with '...' and is no
    longer than n.
    
        >>> truncate("Hello World", 6)
        'Hel...'
        
        >>> truncate("Problem solving is the best!", 10)
        'Problem...'
        
        >>> truncate("Yo", 100)
        'Yo'
        
    The smallest legal value of n is 3; if less, return a message:
    
        >>> truncate('Cool', 1)
        'Truncation must be at least 3 characters.'

        >>> truncate("Woah", 4)
        'W...'

        >>> truncate("Woah", 3)
        '...'
    """
    truncated_list = []
    if (n < 3):
        return 'Truncation must be at least 3 characters.'
    elif(len(phrase) >= n):
        i = 0
        while (i < n-3):
            truncated_list.append(phrase[i])
            i += 1
        truncated_list.append('...')
        return ''.join(truncated_list)
    else:
        return phrase



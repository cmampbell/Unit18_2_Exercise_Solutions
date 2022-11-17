def includes(collection, sought, start=None):
    """Is sought in collection, starting at index start?

    Return True/False if sought is in the given collection:
    - lists/strings/sets/tuples: returns True/False if sought present
    - dictionaries: return True/False if *value* of sought in dictionary

    If string/list/tuple and `start` is provided, starts searching only at that
    index. This `start` is ignored for sets/dictionaries, since they aren't
    ordered.

        >>> includes([1, 2, 3], 1)
        True

        >>> includes([1, 2, 3], 1, 2)
        False

        >>> includes("hello", "o")
        True

        >>> includes(('Elmo', 5, 'red'), 'red', 1)
        True

        >>> includes({1, 2, 3}, 1)
        True

        >>> includes({1, 2, 3}, 1, 3)  # "start" ignored for sets!
        True

        >>> includes({"apple": "red", "berry": "blue"}, "blue")
        True
    """
    #check for start value
    # if start value, set i = start value

    i=0

    if(start):
        i = start

    collection_type = type(collection)

    if (collection_type == dict):
        if sought in collection.values():
            return True
        else:
            return False
    elif (collection_type == str or collection_type == set or i == 0):
        if sought in collection:
            return True
        else:
            return False
    elif (collection_type == list or collection_type == tuple and start):
        if sought in collection[start:]:
            return True
        else:
            return False


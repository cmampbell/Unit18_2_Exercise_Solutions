def same_frequency(num1, num2):
    """Do these nums have same frequencies of digits?
    
        >>> same_frequency(551122, 221515)
        True
        
        >>> same_frequency(321142, 3212215)
        False
        
        >>> same_frequency(1212, 2211)
        True
    """
    #check count for each digit
    #make set from each num

    num1_dict = {num: str(num1).count(num) for num in set(str(num1))}
    num2_dict = {num: str(num2).count(num) for num in set(str(num2))}

    return num1_dict == num2_dict
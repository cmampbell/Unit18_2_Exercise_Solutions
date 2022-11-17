def sum_pairs(nums, goal):
    """Return tuple of first pair of nums that sum to goal.

    For example:

        >>> sum_pairs([1, 2, 2, 10], 4)
        (2, 2)

    (4, 2) sum to 6, and come before (5, 1):

        >>> sum_pairs([4, 2, 10, 5, 1], 6) # (4, 2)
        (4, 2)

    (4, 3) sum to 7, and finish before (5, 2):

        >>> sum_pairs([5, 1, 4, 8, 3, 2], 7)
        (4, 3)

    No pairs sum to 100, so return empty tuple:

        >>> sum_pairs([11, 20, 4, 2, 1, 5], 100)
        ()
    """
    #start on first num
    #check next number in array
    #move to second num, check next num in array
    #if we reach last num, start over, check num two away

    for j in range(1, len(nums)):
        for i in range(len(nums)):
            if(i+j < len(nums)):
                if(nums[i] + nums[i+j] == goal):
                    return (nums[i], nums[i+j])
    return ()

    #---------------------------------PROCESS----------------------------------

    #loop through list
    #while sum does not equal goal
    #keep looping
    #keep track of index we are on
    #keep track of difference between index of the two numbers that sum to goal

    # distance = 0
    # i = 0

    # num1_index = 0
    # num2_index = 0
    # nums_length = len(nums)
    # print(f"Num length is {nums_length}")
    # for num in nums:
    #     j = 0
    #     current_index = nums.index(num)
    #     print(f"Current index is {current_index}")

    #     for num2 in nums:
    #         if not (i == j):
    #             if((num + num2) == goal):
    #                 print(f"I is: {i}, J is {j}")
    #                 if (distance < i - j):
    #                     num1_index = i
    #                     num2_index = j
    #                     distance = j - i
    #                     print(f"Goal distance is {distance}")
    #         j += 1
    #     i += 1
    
    # return (nums[num1_index], nums[num2_index])

    #want to check each numbers neighbor first
    #if sum doesnt match goal, check each numbers 2nd closest neighbor
    #if still no match, continue until we check all number pairs

    # i = 0
    # while (i < len(nums)):
    #     print(i)
    #     i += 1

    # i = 0
    # j = 1

    # while(i < len(nums)):
    #     j = 1
    #     while (j < len(nums)):
    #         if (nums[i] + nums[j] == goal):
    #             return (nums[i], nums[j])
    #         j += 1
    #     i += 1

            
        # j = 1
        # for num2 in nums[0::j]:
        #     print(f"J: {j}, num: {num}, num2: {num2}, Sum: {num + num2}")

    #we have index 0
    #check if index 0 + index 1 = goal
    #if not move to next index,
    #check if index 1 + index 2 = goal




        
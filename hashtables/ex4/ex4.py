def has_negatives(a):
    """
    YOUR CODE HERE
    """
    # Your code here

    nums = {}

    for i in a:
        if i not in nums:
            nums[i] = None
        if (i * -1) in nums:
            nums[i * -1] = i
            nums[i] = i * -1

    result = []

    for i in nums:
        if i > 0 and nums[i] is not None:
            result.append(i)

    return result


if __name__ == "__main__":
    print(has_negatives([-1, -2, 1, 2, 3, 4, -4]))

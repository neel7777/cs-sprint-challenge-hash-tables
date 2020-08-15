def get_indices_of_item_weights(weights, length, limit):
    """
    YOUR CODE HERE
    """
    # Your code here

    weight = {}
    dupe = False
    dupes = {}

    for i in range(0, length):
        current = weights[i]

        weight[current] = i

        ans = limit - current

        if ans in weight:
            
            if current > ans or current < ans:
                return(i, weight[ans])
            elif ans == current:
                if dupe is False:
                    dupe = True
                    dupes[current] = i
                elif dupe is True:
                    return(i, dupes[current])



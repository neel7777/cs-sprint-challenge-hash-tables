#  Hint:  You may not need all of these.  Remove the unused functions.
class Ticket:
    def __init__(self, source, destination):
        self.source = source
        self.destination = destination


def reconstruct_trip(tickets, length):
    """
    YOUR CODE HERE
    """
    # Your code here

    route = {}

    for i in tickets:
        route[i.source] = i.destination

    start = route['NONE']

    airports = [start]

    for i in range(0, length-1):
        nexts = airports[i]
        nextd = route[nexts]
        airports.append(nextd)

    return airports


    

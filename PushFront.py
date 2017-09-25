# Write a function that takes in a list and a value,
# and adds the value to the front of that list, outputting the changed list.
# This should be done in place> This means you should not create a new list,
# but change the existing one.
# Try using your newly discovered Python swap! Here's what your function should look like:

def push_front(lst, val):
    lst += [val]
    print "Before move.", lst

    for i in range(len(lst)-1, 0, -1):
        print "Counter:", i
        lst[i], lst[i-1] = lst[i-1], lst[i]
    print "after move.", lst
    return lst

print push_front([1,2,3,4,5,6], 0)

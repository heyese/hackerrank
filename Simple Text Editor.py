
import collections


# Question talks about a string, but it makes sense
# to use a list for the string S.
#  I need to be able to index it (look up random characters),
# and this provides amortized O(1) time for that
S = []

# As a record of strings I've deleted, I'm going to use
# a 'deque' for it's fast 'popping' time.
deletes = collections.deque()

# Finally, I'll have one more deque to use as a stack to remember
# what append / delete methods I've been using
# I'll say that 'i' (positive int) means we added i characters on,
# and '-i' means we deleted i characters.
record = collections.deque()

Q = int(input())
for _ in range(Q):
    # First step is to process the given input
    # Might need to look and see if I can make this cleaner ...
    action = input().strip()
    if action != '4':
        action, arg = action.split()
        if action != '1':
            arg = int(arg)
    action = int(action)


    if action == 1:
        # Adding string 'arg'
        for i, char in enumerate(arg):
            S.append(char)
        # Note that we've added i characters
        record.append(i+1)

    elif action == 2:
        # Deleting string length arg
        for _ in range(arg):
            deletes.append(S.pop())
        record.append(-arg)

    elif action == 3:
        print(S[arg-1])

    elif action == 4:
        # Undo last action on record
        last_action = record.pop()
        if last_action > 0:
            for _ in range(last_action):
                S.pop()
        else:
            for _ in range(-last_action):
                S.append(deletes.pop())
    else:
        print('This shouldn\'t happen')

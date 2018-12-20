

# https://www.hackerrank.com/challenges/friend-circle-queries/problem
# Will implement a proper union-find data structure

class Union_Find():
    def __init__(self):
        self.root = dict()
        self.set_sizes = dict()
        self.max_set = 0

    def initialise(self, i):
        """
        In this Hackerrank puzzle, I don't need to initialise all elements,
        so I only do those I come across
        """
        self.root[i] = i
        self.set_sizes[i] = 1

    def find_root(self, i):
        """
        Returns the root of the set containing element i
        """
        j = i
        if i not in self.root:
            self.initialise(i)

        # This 'tree' structure can get very long.
        # Need to implement 'path compression'
        while self.root[j] != j:
            j = self.root[j]
        return j

    def path_compress(self, i, root):
        """
        Given root is root of the set containing i.
        This function implements 'path compression'
        """
        while i != root:
            i_root = self.root[i]
            self.root[i] = root
            i = i_root

    def update_set_sizes(self, update, discard):
        """
        Sets with update_root and discard_root have been 'union'ed.
        Stop track size of discard_root set and update the other
        """
        self.set_sizes[update] += self.set_sizes[discard]
        del(self.set_sizes[discard])
        self.max_set = max(self.max_set, self.set_sizes[update])


    def union(self, a, b):
        """
        Points the root of the set containing one element at the
        root of the set containing the other.
        Returns True if a change was made, False if not.
        """
        root_a, root_b = self.find_root(a), self.find_root(b)
        if root_a != root_b:
            # Here I've just chosen a root at random, but it makes sense
            # for the new root to be the root of the tree with
            # the greater height.  Then the height of the new tree
            # can be at most one larger than this, speeding
            # up the find function.
            chosen_root, root_to_update = root_a, root_b
            self.root[root_to_update] = chosen_root
            self.update_set_sizes(chosen_root, root_to_update)
            self.path_compress(b, chosen_root)
            return True
        return False


def maxCircle(queries):
    friend_circles = Union_Find()
    max_circles = []
    for a, b in queries:
        friend_circles.union(a, b)
        max_circles.append(friend_circles.max_set)
    return max_circles



if __name__ == '__main__':

    q = int(input())

    queries = []

    for _ in range(q):
        queries.append(list(map(int, input().rstrip().split())))

    ans = maxCircle(queries)
    print('\n'.join(map(str, ans)))
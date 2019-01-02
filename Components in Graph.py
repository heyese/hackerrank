# https://www.hackerrank.com/challenges/components-in-graph/problem

# Another disjoint set problem

class Disjoint_Set():
    def __init__(self):
        self.roots = dict()
        self.sizes = dict()
        self.max_size = 0

    def find_root(self, a):
        if a not in self.roots:
            # Initialise a
            self.roots[a] = a
            self.sizes[a] = 1
            return a
        x = a
        while x != self.roots[x]:
            x = self.roots[x]

        self.path_compress(element=a, root=x)
        return x

    def update_size(self, *, update, delete):
        """
        previous root of a set b has been pointed to root a
        """
        self.sizes[update] += self.sizes[delete]
        del(self.sizes[delete])

    def union(self, a, b):
        a_root, b_root = self.find_root(a), self.find_root(b)
        if a_root != b_root:
            chosen_root, update_root = b_root, a_root
            self.update_size(update=chosen_root, delete=update_root)
            self.roots[update_root] = chosen_root

    def path_compress(self, element, root):
        x = element
        while x != root:
            y = self.roots[x]
            self.roots[x] = root
            x = y

    def max_and_min(self):
        min, max = None, 0
        for i in range(1, 2*n+1):
            try:
                size = self.sizes[self.roots[i]]
            except:
                continue
            if not min:
                min = size
            else:
                if size < min:
                    min = size
            if size > max:
                max = size
        return [min, max]


def componentsInGraph(gb):
    components = Disjoint_Set()
    for a, b in gb:
        components.union(a, b)
    return components.max_and_min()


if __name__ == '__main__':
    n = int(input())
    gb = []

    for _ in range(n):
        gb.append(list(map(int, input().rstrip().split())))

    result = componentsInGraph(gb)

    print(' '.join(map(str, result)))

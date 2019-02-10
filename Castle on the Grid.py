# https://www.hackerrank.com/challenges/castle-on-the-grid/problem

# Complete the minimumMoves function below.
import collections

def minimumMoves(grid, startX, startY, goalX, goalY):
    # Use a dict to mark the open and blocked cells
    is_open_cell = collections.defaultdict(lambda: True)
    for row, line in enumerate(grid):
        for column, char in enumerate(line):
            if char == 'X':
                is_open_cell[(row, column)] = False

    num_moves = 0
    start = (startX, startY)
    finish = (goalX, goalY)
    if start == finish:
        return 0

    # So (check_horizontal union check_vertical) is the set of points we've visited
    check_horizontal = {start}
    check_vertical = {start}
    checked_horizontal = collections.defaultdict(lambda: False)
    checked_vertical = collections.defaultdict(lambda: False)
    checked_horizontal[start] = checked_vertical[start] = True

    # And (check_horizontal_next union check_vertical_next) is the set of points
    # we can get to in one move
    check_horizontal_next = set()
    check_vertical_next = set()

    while finish not in check_horizontal.union(check_vertical):
        for row, column in check_horizontal:
            # Explore walking left and right from this point.
            # All the points we come across need to be added to check_vertical_next
            # so we explore above and below them on the next move.
            for r in (
                    range(column + 1, n),      # walking right
                    range(column - 1, -1, -1)  # walking left
            ):
                for i in r:
                    if checked_horizontal[(row, i)]:
                        # We've checked this line before
                        break
                    checked_horizontal[(row, i)] = True
                    if is_open_cell[(row, i)]:
                        check_vertical_next.add((row, i))
                    else:
                        # If it's a blocked cell, we can't go further
                        break

        for row, column in check_vertical:
            # Explore walking up and down from this point.
            # All the points we come across need to be added to check_horizontal_next
            # so we explore to the right and left of them on the next move.
            for r in (
                    range(row + 1, n),      # walking down
                    range(row - 1, -1, -1)  # walking up
            ):
                for i in r:
                    if checked_vertical[(i, column)]:
                        # We've checked this column before
                        break
                    checked_vertical[(i, column)] = True
                    if is_open_cell[(i, column)]:
                        check_horizontal_next.add((i, column))
                    else:
                        break

        check_horizontal = check_horizontal_next
        check_vertical = check_vertical_next
        check_horizontal_next = set()
        check_vertical_next = set()
        num_moves += 1
    return num_moves


if __name__ == '__main__':

    n = int(input())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    startXStartY = input().split()
    startX = int(startXStartY[0])
    startY = int(startXStartY[1])
    goalX = int(startXStartY[2])
    goalY = int(startXStartY[3])
    result = minimumMoves(grid, startX, startY, goalX, goalY)

    print(f'{result}')

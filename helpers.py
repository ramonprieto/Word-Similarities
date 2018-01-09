from enum import Enum


class Operation(Enum):
    """Operations"""

    DELETED = 1
    INSERTED = 2
    SUBSTITUTED = 3

    def __str__(self):
        return str(self.name.lower())


def distances(a, b):
    """Calculate edit distance from a to b"""
    # Initialize 2D array with (0, None)
    matrix = [[(0, None) for j in range(len(b) + 1)] for i in range(len(a) + 1)]

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            # Fill first row with (column, Operation.INSERTED)
            if i == 0 and j != 0:
                # 1st row
                matrix[i][j] = (j, Operation.INSERTED)

            # Fill first with (row, Operation.DELETED)
            elif i != 0 and j == 0:
                # 1st column
                matrix[i][j] = (i, Operation.DELETED)

            elif i != 0:

                # get lowest cost around current cell
                min_cost = min(matrix[i - 1][j][0], matrix[i][j - 1][0], matrix[i - 1][j - 1][0])

                # no substitution cost if chars are equal
                if a[i - 1] == b[j - 1]:
                    cost = matrix[i - 1][j -1][0]
                    matrix[i][j] = (cost, Operation.SUBSTITUTED)

                # compare costs to select operation
                elif matrix[i - 1][j][0] == min_cost:
                    matrix[i][j] = (min_cost + 1, Operation.DELETED)

                elif matrix[i][j - 1][0] == min_cost:
                    matrix[i][j] = (min_cost + 1, Operation.INSERTED)

                elif matrix[i - 1][j - 1][0] == min_cost:
                    matrix[i][j] = (min_cost + 1, Operation.SUBSTITUTED)

    return matrix

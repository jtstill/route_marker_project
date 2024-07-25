def file_to_dict(filename):
    d = {}
    f = open(filename)
    for line in f:
        line = line.replace(" ", "")
        key, value = line.split(":")
        line_list = value.strip().split(",")
        line_set = set(line_list)
        d[key] = line_set

    return d

def flip_dict(dict):
    d2 = defaultdict(set)
    for k, s in dict.items():
        for v in s:
            d2[v].add(k)
    return d2

def initial_board(dict):
    headers = list(dict.keys())
    initial_table = [[0 for x in range(len(dict))] for y in range(len(dict))]

    output = ""
    output += "\t"
    for h in headers:
        output += h + "\t"
    output += "\n"
    i = 1
    for row in initial_table:
        line = str(i) + "\t"
        for column in row:
            line += str(column) + "\t"
        output += line + "\n"
        i += 1
    #print(output)
    #print("\n")

    return initial_table, output, headers

def show_table(table, headers):
    output = ""
    output += "\t"
    for h in headers:
        output += h + "\t"
    output += "\n"
    i = 1
    for row in table:
        line = str(i) + "\t"
        for column in row:
            line += str(column) + "\t"
        output += line + "\n"
        i += 1
    print(output)
    print("\n")

'''
def solve(dict, reference_board):
    """Solve the n queens puzzle and print the number of solutions"""
    positions = [-1] * len(dict)
    print(positions)
    put_queen(positions, 0, dict, reference_board)
    #print("Found", self.solutions, "solutions.")

def put_queen(positions, target_row, dict):
    # Base (stop) case - all N rows are occupied
    if target_row == len(positions):
        show_table(positions)
        #self.solutions += 1
        #print("showing full board for solution", self.solutions)
    else:
        # For all N columns positions try to place a queen
        for column in range(self.size):
            # Reject all invalid positions
            if self.check_place(positions, target_row, column):
                positions[target_row] = column
                self.put_queen(positions, target_row + 1)

def check_place(positions, ocuppied_rows, column):
    """
    Check if a given position is available
    """
    for i in range(ocuppied_rows):
        if positions[i] == column or \
            positions[i] - i == column - ocuppied_rows or \
            positions[i] + i == column + ocuppied_rows:
            return False
    return True
'''


def main():
    """Initialize the dictionary"""
    #filename = "doable_state_highways.txt"
    filename = "testfile2.txt"
    dict = file_to_dict(filename)
    pprint.pprint(dict)
    mapped = flip_dict(dict)
    pprint.pprint(mapped)

    """Generate a blank table of spaces based on the dictionary"""
    initial_table, output, headers = initial_board(dict)
    print(output)
    print(initial_table)

    """Fill in initial table spaces as either valid or invalid (1 or 0, respectively). 
    This will become reference table"""
    num = 1 # the first number
    reference_table = []
    for row in initial_table:
        ref_row = []
        for col, state in zip(row, headers):
            valid = False
            if state in mapped[str(num)]:
                valid = True

            if(valid):
                ref_row.append(1)
            else:
                ref_row.append(0)
            print(valid, state, num)
        reference_table.append(ref_row)
        num += 1

    show_table(reference_table, headers)

    """Find solutions"""
    solve(dict)










'''
    headers = list(dict.keys())
    print(headers)

    data = np.array(initial_table)

    data = pd.DataFrame(data[1:, 1:], columns=headers, index=range(1, len(dict)+1))
    data.columns.name = 'Title'
    print(data)

    """Fill in the spaces as valid or invalid (0 for invalid, 1 for valid)"""
    for row in initial_table:
        print("Row:", row)
        for column in initial_table:
            print("Column:", column)

    #print('\n'.join([''.join(['{:3}'.format(item) for item in row])
    #                 for row in initial_table]))
    #print(np.matrix(initial_table))
'''



if __name__ == "__main__":
    from collections import defaultdict
    from itertools import product
    import numpy as np, pandas as pd
    import pprint

    # execute only if run as a script
    main()

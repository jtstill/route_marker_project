""""The n states puzzle"""

class NStates:
    """Generate all valid solutions for the n queens puzzle"""
    def __init__(self, filename, max_out):
        # Store the puzzle (problem) size and the number of valid solutions
        self.dict = self.file_to_dict(filename)
        self.mapped = self.flip_dict()
        self.states = list(self.dict.keys())
        self.size = len(self.dict)
        self.reference_board = self.make_reference_board()
        # self.show_table(self.reference_board)
        self.solutions = 0
        self.kill_switch = max_out
        # a dictionary of [lists of state-number] --> created in solve
        self.solution_dict = {}
        # solves itself upon initiation --> prints solutions
        self.solve()

    def file_to_dict(self, filename):
        d = {}
        f = open(filename)
        for line in f:
            line = line.replace(" ", "")
            key, value = line.split(":")
            line_list = value.strip().split(",")
            line_set = set(line_list)
            d[key] = line_set
        return d

    def flip_dict(self):
        d2 = defaultdict(set)
        for k, s in self.dict.items():
            for v in s:
                d2[v].add(k)
        return d2

    def make_reference_board(self):
        reference_table = []
        for state in self.states:  # for each state, loop 1-50 and fill with valid or invalid
            ref_row = []
            for num in range(1,51): # loop 1-50 and fill with valid/invalid
                if str(num) in self.dict[state]:
                    ref_row.append(1)
                else:
                    ref_row.append(0)
            reference_table.append(ref_row)
        return reference_table

    def solve(self):
        """Solve the n states puzzle and print the number of solutions"""
        positions = [-1] * self.size
        self.choose_combo(positions, 0)
        print("Found", self.solutions, "solutions.\n")

    def choose_combo(self, positions, target_row):
        """
        Try to place a state on target_row (highway number) by checking all N possible cases.
        If a valid place is found the function calls itself trying to choose a state
        for the next number until all N states/numbers are chosen on the NxN board.
        """
        # Base (stop) case - all N rows are occupied
        if target_row == self.size:
            print("Solution:")
            self.show_finished_board(positions)
            self.solutions += 1
            # Add solution to the dictionary
            self.update_solution_dict(positions)
            print("Above is solution #:", self.solutions)
        else:
            # Kill switch for if the number of solutions is just too many for the program
            if self.solutions >= self.kill_switch:
                return

            # For all N columns positions try to choose a state
            for column in range(self.size):
                # if target_row >= 48 and column == 49: # Only use for troubleshooting: manual manipulation
                #     #print("COLUMN IS", column, "and target row is now", target_row)
                #     self.show_finished_board(positions)
                #     #return
                # Reject all invalid positions
                if self.check_place(positions, target_row, column):
                    # print("row", target_row, "had a valid spot in column", column)
                    positions[target_row] = column
                    # self.show_finished_board(positions)
                    # print("Positions:", positions)
                    self.choose_combo(positions, target_row + 1)

    def check_place(self, positions, occupied_rows, column):
        """
        Check if a given position is valid for choosing a state (check straight up column and valid positions)
        """
        for i in range(occupied_rows):
            # print("looking at occupied row:", i, "in column:", column)
            # print("Positions:", positions, "and positions[i]:", positions[i])
            # self.show_finished_board(positions)
            if positions[i] == column:  # column taken
                # print("False because", positions[i], "equals", column, " (in same column)")
                return False

        # looked at all the previous rows to make sure no column conflicts, now need to look at the occupied row
        # to make sure we can actually choose it
        # print("Now to check", self.reference_board[occupied_rows], "at column", column)
        if self.reference_board[occupied_rows][column] == 0: # invalid
            return False
        return True

    def update_solution_dict(self, positions):
        solution = []
        # positions signify the column of an X in each row
        for row, header in zip(range(self.size), self.states):
            choice = header + " " + str(positions[row]+1)
            solution.append(choice)
        key = "Solution " + str(self.solutions)
        self.solution_dict[key] = solution
        print("The solution as a list:", self.solution_dict[key])

    def show_finished_board(self, positions):
        """Show the full NxN board"""
        output = ""
        output += "\t"
        for num in range(1, 51):
            output += str(num) + "\t"
        output += "\n"
        for row, header in zip(range(self.size), self.states):
            line = header + "\t"
            for column in range(self.size):
                if positions[row] == column:
                    line += colored("X ", "green") + "\t"
                else:
                    line += colored(". ", "red") + "\t"
            output += line + "\n"
        print(output)
        print("\n")

    def show_table(self, table):
        output = ""
        output += "\t"
        for num in range(1, 51):
            output += str(num) + "\t"
        output += "\n"
        i = 1
        for row, header in zip(table, self.states):
            line = header + "\t"
            for column in row:
                if column == 1 or column == 'X': # 1/0 in reference table, X/. in solution
                    line += colored(str(column), "green") + "\t"
                else:
                    line += colored(str(column), "red") + "\t"
            output += line + "\n"
            i += 1
        print(output)
        print("\n")


def main():
    """Initialize and solve the n queens puzzle"""
    # NStates uses a filename and find up to a number solutions (to save computing time)
    #nstates = NStates("testfile2.txt", 10)
    nstates = NStates("doable_sh_by_size.txt", 1000)

    # Print the reference table
    print("Reference Table:")
    nstates.show_table(nstates.reference_board)
    # print("Reference Table (plain):")
    # print(nstates.reference_board)

    # Print the solution dictionary
    # construct output for solution dict
    solution_dict = nstates.solution_dict
    # states
    print("States:      ", end = "")
    for value in solution_dict["Solution 1"]:
        state, num = value.split(" ")
        print(state, end=" ")
    print()
    # the solutions
    for key, values in solution_dict.items():
        if len(key) == 10:
            print(key, ": ", sep="", end=" ")
        else:
            print(key, ":", sep="", end=" ")
        if isinstance(values, list):
            for value in values:
                state, num = value.split(" ")
                if len(num) == 1: # single digit
                    num = " " + num
                print(num, end=" ")
        print()
        # else:
        #     print(value)


if __name__ == "__main__":
    from collections import defaultdict
    from itertools import product
    import numpy as np, pandas as pd
    import pprint
    from termcolor import colored

    # execute only if run as a script
    main()

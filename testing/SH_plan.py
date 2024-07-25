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


def find_order(dict):
    order = []
    while len(order) < len(dict): # stops process from continuing once all the numbers are filled
        for key, val in dict.items():
            for i in val:
                if int(i) not in order:
                    order.append(int(i))
    return order


def generate_solutions(filename):
    dict = file_to_dict(filename)
    # print("DICT:")
    # pprint.pprint(dict)
    # print()

    mapped = flip_dict(dict)
    # print("INVERTED:")
    # pprint.pprint(mapped)
    # print()

    order = find_order(dict)
    #print("ORDER:", order)

    solutions = [x for x in product(*mapped.values()) if len(set(x)) == len(mapped)] # the len statement stops duplicates
    # solutions = []
    # for x in product(*mapped.values()):
    #     if len(set(x)) == len(mapped):
    #         solutions.append(x)
    # print("SOLUTIONS:")
    # i = 1
    # for sol in solutions:
    #     print(i, ": ", sol, sep="")
    #     i = i + 1
    # print()

    # Order each solution by number before printing it out --> Final step
    # print("SOLUTIONS:")
    i = 1
    for sol in solutions:
        # zipped = zip(sol, order)
        zipped = sorted(zip(sol, order), key = lambda x: x[1])
        # print(zipped)
        # states, nums = zip(*zipped)
        # print(states)
        # print(nums)

        final = []
        for j, k in zipped:
            final.append(j + " " + str(k))
        # print("Solution ", i, ": ", final, sep="")
        i = i + 1

    print()
    print("# SOLUTIONS:", len(solutions))
    print()


if __name__ == "__main__":
    from collections import defaultdict
    from itertools import product
    import pprint

    generate_solutions("testfile.txt")
    #generate_solutions("doable_state_highways.txt")
'''
    dict = file_to_dict("doable_state_highways.txt")
    print("DICT:")
    pprint.pprint(dict)
    print()

    mapped = flip_dict(dict)
    print("INVERTED:")
    pprint.pprint(mapped)
    print()

    order = find_order(dict)
    print(order)

    # Heuristic: take all the states with only one #, and eliminate the state and # from all points in the dictionaries
    # Step 2: take all the #s with only one state, eliminate state and # from all points in the dictionaries
    # Step 3: alternate between 1 and 2

    # Heuristic: find which states can satisfy highways 1-50 (mapped)
    # Step 2: choose a state for highway 1, then 2, etc., eliminating that state from the remaining numbers
    # If the number has no states to choose from, not a valid way to do it: go back one and choose a different state
    # (similar to the queen problem from CS462)
    mapped2 = defaultdict(list)
    for k, s in dict.items():
        for v in s:
            mapped2[v].append(k)

    # IMPLEMENT: go through the mapped num --> states from least in length to most, that way all the back and forth happens in the end
    # and it will be forced to pick the first few the same way every time

    solution = []
    sh_num = 1
    offset = 0
    while sh_num <= 50:
        states = mapped2[str(sh_num)]
        print("Number:", sh_num, ", States:", states)
        #print(states)
        # Choose a state
        sc = 0 + offset
        state_choice = states[sc]
        while state_choice in solution:
            sc = sc + 1
            try:
                print(state_choice, "already in solution, ", end = "")
                state_choice = states[sc]
            except: # no more choices --> go back one number and try with a new state
                print("no choices available for SH", sh_num)
                offset = 1
                sh_num = sh_num - 2
                del solution[-1]
                break
        # Append to solution
        print("Adding", state_choice, sh_num)
        solution.append(state_choice)
        print(solution)
        print()
        # Increase counter
        sh_num = sh_num + 1
    print("SOLUTION (position indicates number):", solution)
'''























    # print("\n\n\n\n")
    # d = {'B': {1, 2},
    #      'A': {1, 2, 4, 5},
    #      'C': {2, 3, 5},
    #      'E': {3},
    #      'D': {1, 3, 4, 5}}
    #
    # # order = []
    # # print("order time!")
    # # while len(order) < len(d):
    # #     for key, val in d.items():
    # #         print(key, val)
    # #         for i in val:
    # #             if i not in order:
    # #                 order.append(i)
    # # print("ORDER: ", order)
    #
    # from collections import defaultdict
    # from itertools import product
    #
    # d2 = defaultdict(set)
    # for k, s in d.items():
    #     for v in s:
    #         d2[v].add(k)
    # pprint.pprint(d2)
    # # {1: {'A', 'B', 'D'},
    # #  2: {'A', 'B', 'C'},
    # #  3: {'A', 'C', 'D', 'E'},
    # #  4: {'A', 'B', 'D', 'E'},
    # #  5: {'A', 'C', 'D'}}
    #
    # out = [x for x in product(*d2.values()) if len(set(x)) == len(d2)]
    # print("SOLUTIONS:")
    # i = 1
    # for o in out:
    #     print(i, ": ", o, sep="")
    #     i = i + 1
    # print()
    # print("# SOLUTIONS:", len(out))

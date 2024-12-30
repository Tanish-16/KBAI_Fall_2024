from BlockWorldAgent import BlockWorldAgent

def test():
    #This will test your BlockWorldAgent
	#with eight initial test cases.
    test_agent = BlockWorldAgent()

    initial_arrangement_1 = [["A", "B", "C"], ["D", "E"]]
    goal_arrangement_1 = [["A", "C"], ["D", "E", "B"]]
    goal_arrangement_2 = [["A", "B", "C", "D", "E"]]
    goal_arrangement_3 = [["D", "E", "A", "B", "C"]]
    goal_arrangement_4 = [["C", "D"], ["E", "A", "B"]]

    print(test_agent.solve(initial_arrangement_1, goal_arrangement_1))
    print(test_agent.solve(initial_arrangement_1, goal_arrangement_2))
    print(test_agent.solve(initial_arrangement_1, goal_arrangement_3))
    print(test_agent.solve(initial_arrangement_1, goal_arrangement_4))
    # #
    initial_arrangement_2 = [["A", "B", "C"], ["D", "E", "F"], ["G", "H", "I"]]
    goal_arrangement_5 = [["A", "B", "C", "D", "E", "F", "G", "H", "I"]]
    goal_arrangement_6 = [["I", "H", "G", "F", "E", "D", "C", "B", "A"]]
    goal_arrangement_7 = [["H", "E", "F", "A", "C"], ["B", "D"], ["G", "I"]]
    goal_arrangement_8 = [["F", "D", "C", "I", "G", "A"], ["B", "E", "H"]]

    print(test_agent.solve(initial_arrangement_2, goal_arrangement_5))
    print(test_agent.solve(initial_arrangement_2, goal_arrangement_6))
    print(test_agent.solve(initial_arrangement_2, goal_arrangement_7))
    print(test_agent.solve(initial_arrangement_2, goal_arrangement_8))

    initial_arrangement_3 = [['H', 'B'], ['C'], ['E'], ['D', 'I'], ['F', 'A', 'G']]
    goal_arrangement_9 = [['H'], ['D', 'B'], ['G'], ['I', 'A'], ['F'], ['C', 'E']]
    print(test_agent.solve(initial_arrangement_3, goal_arrangement_9))

    initial_arrangement_4 = [['C', 'L', 'I'], ['B', 'E', 'M', 'G'], ['F', 'H', 'K', 'J', 'A', 'D']]
    goal_arrangement_10 = [['I'], ['E', 'K', 'G', 'B'], ['F', 'H', 'J', 'A'], ['C'], ['L', 'D', 'M']]
    print(test_agent.solve(initial_arrangement_4, goal_arrangement_10))

    initial_arrangement_5 = [['A', 'B', 'C', 'D', 'E', 'F', 'G']]
    goal_arrangement_11 = [['G', 'F', 'E', 'D', 'C', 'B', 'A']]
    print(test_agent.solve(initial_arrangement_5, goal_arrangement_11))

    goal_arrangement_12 = [['A', 'B', 'C'], ['G', 'F', 'E'], ['D']]
    print(test_agent.solve(initial_arrangement_5, goal_arrangement_12))

if __name__ == "__main__":
    test()
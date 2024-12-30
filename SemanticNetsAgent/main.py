from SemanticNetsAgent import SemanticNetsAgent

def test():
    #This will test your SemanticNetsAgent
	#with seven initial test cases.
    test_agent = SemanticNetsAgent()

    print(test_agent.solve(1, 1))
    print(test_agent.solve(2, 2))
    print(test_agent.solve(3, 3))
    print(test_agent.solve(5, 3))
    print(test_agent.solve(6, 3))
    print(test_agent.solve(7, 3))
    print(test_agent.solve(5, 5))
    print(test_agent.solve(10, 5))
    print(test_agent.solve(13, 9))
    print(test_agent.solve(20, 9))
    print(test_agent.solve(9, 5))
    print(test_agent.solve(9, 2))
    print(test_agent.solve(9, 9))
    print(test_agent.solve(6, 6))
    print(test_agent.solve(7, 5))
    print(test_agent.solve(7, 2))
    print(test_agent.solve(4, 2))
    print(test_agent.solve(3, 2))

if __name__ == "__main__":
    test()
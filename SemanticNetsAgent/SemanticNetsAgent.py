import time
class State:
    def __init__(self, left_sheep, right_sheep, left_wolves, right_wolves, initial_sheep, initial_wolves, direction):
        self.left_sheep = left_sheep
        self.right_sheep = right_sheep
        self.left_wolves = left_wolves
        self.right_wolves = right_wolves
        self.initial_sheep = initial_sheep
        self.initial_wolves = initial_wolves
        self.direction = direction

    def __eq__(self, other):
        if isinstance(other, State):
            if self.left_sheep == other.left_sheep and self.right_sheep == other.right_sheep and self.left_wolves == other.left_wolves and self.right_wolves == other.right_wolves and self.initial_sheep == other.initial_sheep and self.initial_wolves == other.initial_wolves and self.direction == other.direction:
                return True
            return False

    def __hash__(self):
        return hash((self.left_sheep, self.right_sheep, self.left_wolves, self.right_wolves, self.initial_sheep, self.initial_wolves, self.direction))

    def __str__(self):
        return "Left sheep = {} Right sheep = {} Left wolves = {} Right wolves = {}".format(self.left_sheep, self.right_sheep, self.left_wolves, self.right_wolves)

    def is_state_valid(self):
        if (self.left_sheep < 0 or self.left_sheep > self.initial_sheep) or (self.right_sheep < 0 or self.right_sheep > self.initial_sheep) or (
                self.left_wolves < 0 or self.left_wolves > self.initial_wolves) or (self.right_wolves < 0 or self.right_wolves > self.initial_wolves):
            return False
        if self.left_wolves > self.left_sheep:
            if self.left_sheep == 0:
                return True
            return False
        if self.right_wolves > self.right_sheep:
            if self.right_sheep == 0:
                return True
            return False

        return True

    def is_final_state(self):
        if self.left_sheep == 0 and self.left_wolves == 0 and self.right_sheep == self.initial_sheep and self.right_wolves == self.initial_wolves and self.direction == 0:
            return True
        return False
iter = 0
class SemanticNetsAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def find_states(self, state, possible_moves, is_visited, solution_steps, solutions_set, prev_move=None):
        # print(state)
        global iter
        iter += 1
        if iter > 10000000:
            return

        if state.is_final_state():
            solutions_set.append(solution_steps.copy())
            # print(solutions_set)
            return
        is_visited.add(state)
        for move in possible_moves:
            if prev_move != move:
                if state.direction == 0:
                    new_left_sheep = state.left_sheep + move[0]
                    new_left_wolves = state.left_wolves + move[1]
                    new_right_sheep = state.right_sheep - move[0]
                    new_right_wolves = state.right_wolves - move[1]
                else:
                    new_left_sheep = state.left_sheep - move[0]
                    new_left_wolves = state.left_wolves - move[1]
                    new_right_sheep = state.right_sheep + move[0]
                    new_right_wolves = state.right_wolves + move[1]

                new_state = State(new_left_sheep, new_right_sheep, new_left_wolves, new_right_wolves, state.initial_sheep, state.initial_wolves, 1-state.direction)
                if new_state.is_state_valid() and new_state not in is_visited:
                    solution_steps.append(move)
                    self.find_states(new_state, possible_moves, is_visited, solution_steps, solutions_set, move)
                    solution_steps.pop()
        is_visited.remove(state)

    def find_shortest_path(self, solutions_set):
        shortest_length = 10**9
        shortest_path = []
        for solution in solutions_set:
            if len(solution) < shortest_length:
                shortest_length = len(solution)
                shortest_path = solution

        return shortest_path


    def solve(self, initial_sheep, initial_wolves):
        start_time = time.time()
        left_sheep = initial_sheep
        right_sheep = 0
        left_wolves = initial_wolves
        right_wolves = 0
        possible_moves = [(0, 1), (0, 2,), (1, 0), (1, 1), (2, 0)]
        initial_state = State(left_sheep, right_sheep, left_wolves, right_wolves, initial_sheep, initial_wolves, 1)
        is_visited = set()
        solutions_set = []
        solution_steps = []
        self.find_states(initial_state, possible_moves, is_visited, solution_steps, solutions_set)
        global iter
        iter = 0
        end_time = time.time()
        print("Runtime is {}".format(end_time - start_time))
        return self.find_shortest_path(solutions_set)
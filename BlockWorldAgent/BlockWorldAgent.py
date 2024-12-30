import copy
from collections import deque
import heapq
import time


class State:
    goal_config = []
    def __init__(self, initial_arrangement):
        size = 0
        for i in range(len(initial_arrangement)):
            size += len(initial_arrangement[i])
        self.state_config = []
        self.parent = None
        self.origin_move = None
        if initial_arrangement:
            self.state_config = [[None for _ in range(2)] for _ in range(size)]
            for i in range(len(initial_arrangement)):
                for j in range(len(initial_arrangement[i])):
                    block = initial_arrangement[i][j]
                    if j == 0:
                        self.state_config[ord(block)-ord('A')][0] = "Table"
                    else:
                        self.state_config[ord(block)-ord('A')][0] = initial_arrangement[i][j-1]
                    if j == len(initial_arrangement[i]) - 1:
                        self.state_config[ord(block)-ord('A')][1] = -1
                    else:
                        self.state_config[ord(block)-ord('A')][1] = initial_arrangement[i][j+1]

    def is_final_state(self):
        if self.state_config == State.goal_config:
            return True
        return False

    def __eq__(self, other):
        return self.state_config == other.state_config

    def __hash__(self):
        return hash(tuple(tuple(item) for item in self.state_config))
    def __lt__(self, other):
        correct_positioned_blocks1 = 0
        correct_positioned_blocks2 = 0
        for i in range(len(self.state_config)):
            if self.state_config[i][0] == State.goal_config[i][0] and self.state_config[i][1] == State.goal_config[i][1]:
                correct_positioned_blocks1 += 1
            if other.state_config[i][0] == State.goal_config[i][0] and other.state_config[i][1] == State.goal_config[i][1]:
                correct_positioned_blocks2 += 1
        return correct_positioned_blocks1 < correct_positioned_blocks2


class BlockWorldAgent:
    def __init__(self):
        #If you want to do any initial processing, add it here.
        pass

    def set_goal_config(self, goal_arrangement):
        size = 0
        for i in range(len(goal_arrangement)):
            size += len(goal_arrangement[i])
        State.goal_config = [[None for _ in range(2)] for _ in range(size)]
        for i in range(len(goal_arrangement)):
            for j in range(len(goal_arrangement[i])):
                block = goal_arrangement[i][j]
                if j == 0:
                    State.goal_config[ord(block) - ord('A')][0] = "Table"
                else:
                    State.goal_config[ord(block) - ord('A')][0] = goal_arrangement[i][j - 1]
                if j == len(goal_arrangement[i]) - 1:
                    State.goal_config[ord(block) - ord('A')][1] = -1
                else:
                    State.goal_config[ord(block) - ord('A')][1] = goal_arrangement[i][j + 1]

    def get_below_blocks_in_stack(self, current_state, top_block):
        current_block = chr(top_block + ord('A'))
        block_stack = []
        block_stack.append(current_block)
        while True:
            curr_index = ord(current_block) - ord('A')
            if current_state.state_config[curr_index][0] == "Table":
                break
            block_stack.append(current_state.state_config[curr_index][0])
            current_block = current_state.state_config[curr_index][0]
        block_stack.reverse()
        return block_stack

    def find_next_states(self, current_state):
        top_blocks = []
        next_states = []
        for i in range(len(current_state.state_config)):
            if current_state.state_config[i][1] == -1:
                top_blocks.append(i)
        for i in range(len(top_blocks)):
            for j in range(len(top_blocks)+1):
                if i == j:
                    continue
                new_state = State([])
                new_state.state_config = copy.deepcopy(current_state.state_config)
                if j == len(top_blocks):  #move block on table
                    top_block = top_blocks[i]
                    # If the stack containing the top block is 100% correct as per goal config skip
                    current_block_stack = self.get_below_blocks_in_stack(new_state, top_block)
                    starting_block = current_block_stack[0]
                    if State.goal_config[ord(starting_block) - ord('A')][0] == "Table": # If the root block of current stack is also a root in the goal config
                        goal_block_stack = []
                        curr_block = starting_block
                        goal_block_stack.append(starting_block)
                        while True:
                            curr_index = ord(curr_block) - ord('A')
                            if State.goal_config[curr_index][1] == -1:
                                break
                            goal_block_stack.append(State.goal_config[curr_index][1])
                            curr_block = State.goal_config[curr_index][1]
                        ptr1 = 0
                        ptr2 = 0
                        flag = True
                        while ptr1 < len(current_block_stack) and ptr2 < len(goal_block_stack):
                            if current_block_stack[ptr1] != goal_block_stack[ptr2]:
                                flag = False
                                break
                            ptr1 += 1
                            ptr2 += 1
                        if flag and len(current_block_stack) <=  len(goal_block_stack):
                            continue
                    if new_state.state_config[top_block][0] == "Table":  # If block is on top of table, no need to change config of it's lower block
                        continue
                    else:
                        lower_block = new_state.state_config[top_block][0]
                        new_state.state_config[ord(lower_block) - ord('A')][1] = -1
                        new_state.state_config[top_block][0] = "Table"
                        new_state.state_config[ord(lower_block) - ord('A')][1] = -1
                    new_state.origin_move = (chr(top_block + ord('A')), "Table")
                else:   #move block on top of other block
                    top_block = top_blocks[i]
                    bottom_block = top_blocks[j]
                    if State.goal_config[top_block][0] != chr(bottom_block + ord('A')): #If top block is not exactly above the bottom block in goal config, skip
                        continue
                    # If bottom block config is incorrect, skip
                    bottom_block_stack = self.get_below_blocks_in_stack(new_state, bottom_block)
                    goal_block_stack = []
                    bottom_block_stack_root = bottom_block_stack[0]
                    if State.goal_config[ord(bottom_block_stack_root) - ord('A')][0] != "Table":
                        continue
                    if new_state.state_config[top_block][0] == "Table": # If block is on top of table, no need to change config of it's lower block
                        new_state.state_config[top_block][0] = chr(ord('A') + bottom_block)
                        new_state.state_config[bottom_block][1] = chr(ord('A') + top_block)
                    else:
                        lower_block = new_state.state_config[top_block][0]
                        new_state.state_config[ord(lower_block) - ord('A')][1] = -1
                        new_state.state_config[top_block][0] = chr(ord('A') + bottom_block)
                        new_state.state_config[bottom_block][1] = chr(ord('A') + top_block)
                    new_state.origin_move = (chr(top_block + ord('A')), chr(bottom_block + ord('A')))
                new_state.parent = current_state
                next_states.append(new_state)
                # print("New State generated is: {}".format(new_state.state_config))
        return next_states

    def calc_heuristic(self, current_state):
        cost = 0
        blocks_above_goal_config = [0] * len(State.goal_config)
        for i in range(len(State.goal_config)):
            block_index = i
            cnt = 0
            temp = block_index
            while temp != -1:
                if State.goal_config[temp][1] == -1:
                    break
                temp = ord(State.goal_config[temp][1]) - ord('A')
                cnt += 1
            blocks_above_goal_config[block_index] = cnt
        blocks_above_current_config = [0] * len(current_state.state_config)
        for i in range(len(current_state.state_config)):
            block_index = i
            cnt = 0
            temp = block_index
            while temp != -1:
                if current_state.state_config[temp][1] == -1:
                    break
                temp = ord(current_state.state_config[temp][1]) - ord('A')
                cnt += 1
            blocks_above_current_config[block_index] = cnt
        for i in range(len(blocks_above_goal_config)):
            if blocks_above_goal_config[i] < blocks_above_current_config[i]:
                cost += 100 * (blocks_above_current_config[i] - blocks_above_goal_config[i])
        return cost

    def populate_moves(self, goal_state):
        moves = []
        curr_state = goal_state
        while curr_state is not None:
            if curr_state.parent is None:
                break
            moves.append((curr_state.origin_move))
            curr_state = curr_state.parent
        moves.reverse()
        return moves

    def solve(self, initial_arrangement, goal_arrangement):
        start_time = time.time()
        self.set_goal_config(goal_arrangement)
        init_state = State(initial_arrangement)
        q = deque()
        # pq = []
        # heapq.heappush(pq, (self.calc_heuristic(init_state), init_state))
        q.append((0, init_state))
        is_visited = set()
        is_visited.add(init_state)
        # while len(pq) > 0:
        #     current_cost, curr_state = heapq.heappop(pq)
        #     # print("Current state is {}".format(curr_state.state_config))
        #     if curr_state.is_final_state():
        #         # print("final state achieved in {} moves".format(num_moves))
        #         return self.populate_moves(curr_state)
        #     else:
        #         next_states = self.find_next_states(curr_state)
        #         for next_state in next_states:
        #             if next_state not in is_visited:
        #                 is_visited.add(next_state)
        #                 heapq.heappush(pq, (self.calc_heuristic(next_state), next_state))
        while len(q) > 0:
            num_moves, curr_state = q.popleft()
            # print("Current state is {}".format(curr_state.state_config))
            if curr_state.is_final_state():
                # print("final state achieved in {} moves".format(num_moves))
                end_time = time.time()
                print("Time taken is {}".format(end_time - start_time))
                return self.populate_moves(curr_state)
            else:
                next_states = self.find_next_states(curr_state)
                for next_state in next_states:
                    if next_state not in is_visited:
                        is_visited.add(next_state)
                        q.append((1+num_moves, next_state))

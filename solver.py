from puzzle_utils import state_check, get_manhattan_distance, get_succ, format_puzzle_state

import heapq

def inversion_counter(state):
    count = 0
    for i in range(len(state)):
        for j in range(i + 1, len(state)):
            if state[i] != 0 and state[j] != 0 and state[i] > state[j]:
                count += 1
    return count

def check_solvability(state):
    if state.count(0) > 1:
        return True
    else:
        return inversion_counter(state) % 2 == 0

def display_sol_path(visited, state, goal_state):
    path = []
    while state is not None:
        g, parent_state = visited[state]
        path.append((state, get_manhattan_distance(state, goal_state), g))
        state = parent_state

    for state_info in reversed(path):
        print(format_puzzle_state(*state_info))

def solve(state):
    initial_state = tuple(state)
    goal_state = state_check(state)
    solvable_condition = check_solvability(initial_state)
    explored = {initial_state: (0, None)}
  
    if not solvable_condition:
        print(False)
        return
    else:
        print(True)

    f = get_manhattan_distance(initial_state, goal_state) + 0 
    pq = []
    heapq.heappush(pq, (f, initial_state, 0))
    
    while pq:
        element = heapq.heappop(pq)
        f, current_state, g = element

        if goal_state == current_state:
            display_sol_path(explored, current_state, goal_state)
            return

        for succ in get_succ(list(current_state)):
            succ_state = tuple(succ)
            cost_to_succ = g + 1
            heuristic_cost = get_manhattan_distance(succ_state, goal_state)
            total_cost = cost_to_succ + heuristic_cost

            if succ_state in explored:
                if explored[succ_state][0] > cost_to_succ:
                    explored[succ_state] = (cost_to_succ, current_state)
                    heapq.heappush(pq, (total_cost, succ_state, cost_to_succ))
            else:
                explored[succ_state] = (cost_to_succ, current_state)
                heapq.heappush(pq, (total_cost, succ_state, cost_to_succ))

    print(False)

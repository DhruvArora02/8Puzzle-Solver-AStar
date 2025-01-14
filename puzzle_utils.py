import heapq

def state_check(state):
    non_zero_numbers = [n for n in state if n != 0]
    num_tiles = len(non_zero_numbers)
    if num_tiles == 0:
        raise ValueError('At least one number is not zero.')
    elif num_tiles > 9:
        raise ValueError('At most nine numbers in the state.')
    matched_seq = list(range(1, num_tiles + 1))
    if len(state) != 9 or not all(isinstance(n, int) for n in state):
        raise ValueError('State must be a list contain 9 integers.')
    elif not all(0 <= n <= 9 for n in state):
        raise ValueError('The number in state must be within [0,9].')
    elif len(set(non_zero_numbers)) != len(non_zero_numbers):
        raise ValueError('State can not have repeated numbers, except 0.')
    elif sorted(non_zero_numbers) != matched_seq:
        raise ValueError('For puzzles with X tiles, the non-zero numbers must be within [1,X], '
                         'and there will be 9-X grids labeled as 0.')
    goal_state = matched_seq
    for _ in range(9 - num_tiles):
        goal_state.append(0)
    return tuple(goal_state)

def get_tile_position(state):
    return {tile: idx for idx, tile in enumerate(state) if tile != 0}

def get_manhattan_distance(current_state, goal_state):
    goal_positions = get_tile_position(goal_state)
    distance = sum(
        abs(i // 3 - goal_positions[tile] // 3) + abs(i % 3 - goal_positions[tile] % 3)
        for i, tile in enumerate(current_state) if tile != 0
    )
    return distance

def get_succ(state):
    moves = {
        0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
        3: [0, 4, 6], 4: [1, 3, 5, 7], 5: [2, 4, 8],
        6: [3, 7], 7: [4, 6, 8], 8: [5, 7]
    }
    succ_states = []
    for i in range(9):
        if state[i] != 0:
            for m in moves[i]:
                if state[m] == 0:
                    next_state = list(state)
                    next_state[m], next_state[i] = next_state[i], next_state[m]
                    succ_states.append(next_state) if next_state not in succ_states else None
    return sorted(succ_states)

def format_puzzle_state(state, h, moves=None):
    return f"{list(state)} h={int(h)}" + (f" moves: {moves}" if moves is not None else "")

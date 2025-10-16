 from heapq import heappush, heappop

goal_state = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 0]]

moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def find_zero(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def manhattan_distance(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_x, target_y = (value - 1) // 3, (value - 1) % 3
                distance += abs(i - target_x) + abs(j - target_y)
    return distance

def get_neighbors(state):
    neighbors = []
    x, y = find_zero(state)
    for dx, dy in moves:
        new_x, new_y = x + dx, y + dy
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = [row[:] for row in state]
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            neighbors.append(new_state)
    return neighbors

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def solve_puzzle(start):
    heap = []
    visited = set()
    heappush(heap, (manhattan_distance(start), 0, start, []))
    while heap:
        est_total, cost, state, path = heappop(heap)
        if state == goal_state:
            return path + [state]
        visited.add(state_to_tuple(state))
        for neighbor in get_neighbors(state):
            if state_to_tuple(neighbor) not in visited:
                new_cost = cost + 1
                heappush(heap, (new_cost + manhattan_distance(neighbor), new_cost, neighbor, path + [state]))
    return None

start_state = [[1, 2, 3],
               [4, 0, 6],
               [7, 5, 8]]

solution = solve_puzzle(start_state)

if solution:
    print("Steps to solve the 8-puzzle:\n")
    for step, state in enumerate(solution):
        print(f"Step {step}:")
        for row in state:
            print(row)
        print()
else:
    print("No solution found!")


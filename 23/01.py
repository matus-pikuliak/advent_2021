import heapq

costs = {'A': 1, 'B': 10, 'C': 100, 'D': 1000}

def clear_path(s, r, h):
    p1, p2 = sorted((r, h))
    return all(
        not s[h]
        for h in halls
        if p1 < h < p2
    )


def move(c, s, r, h):
    s = list(s)
    s[h], s[r] = s[r], s[h]
    step_cost = costs[s[h] or s[r]]
    num_steps = (abs(pos[h][1] - pos[r][1]) + pos[r][0])
    c += step_cost * num_steps
    return c, tuple(s)


def generate_states(c, s):

    # Move from hallways to rooms
    for h in halls:
        if s[h] and clear_path(s, rooms[s[h]], h):
            r = rooms[s[h]]
            for i in range(room_size - 1, -1, -1):
                if not s[r + i]:
                    yield move(c, s, r + i, h)
                    break
                elif s[r + i] != s[h]:
                    break

    # Move from rooms to hallways
    for char, r in rooms.items():
        top = None
        for i in range(room_size):
            if s[r + i] and not top:
                top = r + i
            if s[r + i] and s[r + i] != char:
                break
        else:
            continue

        for h in halls:
            if not s[h] and clear_path(s, top, h):
                yield move(c, s, top, h)


for room_size in {2, 4}:

    if room_size == 2:
        start_state = ('', '', 'D', 'B', '', 'D', 'C', '', 'B', 'A', '', 'A', 'C', '', '')
        end_state = ('', '', 'A', 'A', '', 'B', 'B', '', 'C', 'C', '', 'D', 'D', '', '')
        halls = [0, 1, 4, 7, 10, 13, 14]
        rooms = {'A': 2, 'B': 5, 'C': 8, 'D': 11}
        pos = [(0, 0), (0, 1), (1, 2), (2, 2), (0, 3), (1, 4), (2, 4), (0, 5), (1, 6), (2, 6), (0, 7), (1, 8), (2, 8),
               (0, 9), (0, 10)]
    else:
        start_state = ('', '', 'D', 'D', 'D', 'B', '', 'D', 'C', 'B', 'C', '', 'B', 'B', 'A', 'A', '', 'A', 'A', 'C', 'C', '', '')
        end_state = ('', '', 'A', 'A', 'A', 'A', '', 'B', 'B', 'B', 'B', '', 'C', 'C', 'C', 'C', '', 'D', 'D', 'D', 'D', '', '')
        halls = [0, 1, 6, 11, 16, 21, 22]
        rooms = {'A': 2, 'B': 7, 'C': 12, 'D': 17}
        pos = [(0, 0), (0, 1), (1, 2), (2, 2), (3, 2), (4, 2), (0, 3), (1, 4), (2, 4), (3, 4), (4, 4), (0, 5), (1, 6),
               (2, 6), (3, 6), (4, 6), (0, 7), (1, 8), (2, 8), (3, 8), (4, 8), (0, 9), (0, 10)]

    heapq.heapify(state_heap := [(0, start_state)])
    visited = set()
    while state_heap[0][1] != end_state:
        c, s = heapq.heappop(state_heap)
        if s not in visited:
            for new_c, new_s in generate_states(c, s):
                if new_s not in visited:
                    heapq.heappush(state_heap, (new_c, new_s))
        visited.add(s)

    print(state_heap[0][0])
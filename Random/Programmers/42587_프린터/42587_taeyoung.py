def solution(priorities, location):
    ret = 1
    priority_index = [x for x in range(len(priorities))]

    while len(priorities) > 1:
        ready_val = priorities.pop(0) # O(N)
        ready_idx = priority_index.pop(0) # O(N)
        max_val = max(priorities) # O(N)
        if max_val > ready_val:
            priorities.append(ready_val)
            priority_index.append(ready_idx)
        elif ready_idx == location:
            return ret
        else:
            ret += 1
    return ret
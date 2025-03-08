#using DFS to solve water jug problem

def waterJugDFS(jug1, jug2, target, visited, path):
    
    if jug1 == target or jug2 == target:
        path.append((jug1, jug2))
        print("Solution Found!")
        for step in path:
            print(step)
        return True
    

    if (jug1, jug2) in visited:
        return False
    
    visited.add((jug1, jug2))
    path.append((jug1, jug2))
    
    rules = [
        (capacity1, jug2, "Fill Jug 1"),
        (jug1, capacity2, "Fill Jug 2"),
        (0, jug2, "Empty Jug 1"),
        (jug1, 0, "Empty Jug 2"),
        #updated rules 5 & 6
        (jug1 - min(jug1, capacity2 - jug2), jug2 + min(jug1, capacity2 - jug2), "Pour Jug 1 -> Jug 2"),
        (jug1 + min(jug2, capacity1 - jug1), jug2 - min(jug2, capacity1 - jug1), "Pour Jug 2 -> Jug 1")
    ]
    
    for new_jug1, new_jug2, action in rules:
        print(f"Applying rule: {action} -> ({new_jug1}, {new_jug2})")
        if waterJugDFS(new_jug1, new_jug2, target, visited, path.copy()):
            return True
    
    return False
capacity1 = 4
capacity2 = 3
target = 2

visited_states = set()
print("Starting DFS Search...")
if not waterJugDFS(0, 0, target, visited_states, []):
    print("No Solution Found")

# 1. ------------------------------------
def logistic_map(x, r):
    return r * x * (1 - x)
    
# 2. ------------------------------------
initial_condition = 0.5
t_final = 10
r = 1.0
trajectory = [initial_condition]
for t in range(1, t_final):
    trajectory[t] = logistic_map(trajectory[t-1], r)
    
# 3. -----------------------------------
def iterate(initial_condition, t_final, r):
    trajectory = [initial_condition]
    for t in range(1, t_final):
        trajectory[t] = logistic_map(trajectory[t-1], r)
    return trajectory
import math
import random

def simulated_annealing(initial_state, value_fn, neighbor_fn, schedule):
    current = initial_state
    for t in range(1, 1000):  # thay cho vòng lặp vô hạn
        T = schedule(t)
        if T == 0:
            return current
        next_state = random.choice(neighbor_fn(current))
        delta_e = value_fn(next_state) - value_fn(current)
        if delta_e > 0:
            current = next_state
        else:
            if random.uniform(0, 1) < math.exp(delta_e / T):
                current = next_state
    return current


# ví dụ test: cực đại của f(x) = -(x^2) + 10
def value_fn(x):
    return -(x ** 2) + 10

def neighbor_fn(x):
    return [x - 1, x + 1]

def schedule(t):
    return max(0.01, 1.0 / t)

result = simulated_annealing(initial_state=random.uniform(-10, 10),
                             value_fn=value_fn,
                             neighbor_fn=neighbor_fn,
                             schedule=schedule)

print("Kết quả:", result)
print("Giá trị:", value_fn(result))

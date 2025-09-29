from simpleai.search import CspProblem, backtrack, SearchProblem
from simpleai.search.local import hill_climbing, simulated_annealing, genetic
import random

# ====== 1. Định nghĩa CSP cho 5-Queens ======
N = 5
variables = ['Q' + str(i) for i in range(N)]
domains = {var: list(range(N)) for var in variables}

def constraint_different(var_values, values):
    var1, var2 = var_values
    value1, value2 = values
    # Không cùng cột
    if value1 == value2:
        return False
    # Không cùng chéo
    i = int(var1[1:])
    j = int(var2[1:])
    if abs(i - j) == abs(value1 - value2):
        return False
    return True

# Tạo danh sách constraints cho tất cả cặp biến
constraints = []
for i in range(N):
    for j in range(i + 1, N):
        constraints.append(((variables[i], variables[j]), constraint_different))

problem_csp = CspProblem(variables, domains, constraints)

# ====== 2. Hàm in bàn cờ ======
def print_board(solution, title=""):
    print("\n" + title)
    board = [['.' for _ in range(N)] for _ in range(N)]

    # solution có thể là dict (backtrack) hoặc list/tuple (local search)
    if isinstance(solution, dict):
        for var, col in solution.items():
            row = int(var[1:])
            board[row][col] = 'Q'
    else:
        for row, col in enumerate(solution):
            board[row][col] = 'Q'

    for row in range(N):
        print(" ".join(board[row]))
    print()

# ====== 3. Hàm phân tích nghiệm ======
def analyze_solution(state):
    """Đếm số conflicts và in kết quả"""
    conflicts = 0
    n = len(state)

    # Nếu là dict (CSP) -> convert sang tuple để check
    if isinstance(state, dict):
        converted = [None] * n
        for var, col in state.items():
            row = int(var[1:])
            converted[row] = col
        state = tuple(converted)

    for i in range(n):
        for j in range(i + 1, n):
            # Cùng cột
            if state[i] == state[j]:
                conflicts += 1
            # Cùng đường chéo
            elif abs(state[i] - state[j]) == abs(i - j):
                conflicts += 1

    total_pairs = n * (n - 1) // 2
    print(f"Số conflicts: {conflicts}")
    print(f"Giá trị hàm đánh giá: {total_pairs - conflicts}/{total_pairs}")

    if conflicts == 0:
        print("=> Đây là lời giải HOÀN HẢO!")
    else:
        print("=> Lời giải chưa hoàn hảo")
    print()

# ====== 4. Local Search Problem ======
class FiveQueensProblem(SearchProblem):
    def __init__(self, initial_state=None):
        if initial_state is None:
            initial_state = tuple(random.randint(0, N-1) for _ in range(N))
        super().__init__(initial_state)

    def actions(self, state):
        actions = []
        for col in range(N):
            for new_row in range(N):
                if new_row != state[col]:
                    actions.append((col, new_row))
        return actions

    def result(self, state, action):
        col, new_row = action
        new_state = list(state)
        new_state[col] = new_row
        return tuple(new_state)

    def value(self, state):
        non_attacking_pairs = 0
        for i in range(N):
            for j in range(i + 1, N):
                if not self.is_attacking(state, i, j):
                    non_attacking_pairs += 1
        return non_attacking_pairs  # càng nhiều cặp không tấn công càng tốt

    def is_attacking(self, state, i, j):
        if state[i] == state[j]:
            return True
        if abs(state[i] - state[j]) == abs(i - j):
            return True
        return False

    # Genetic Algorithm cần thêm 3 hàm này
    def generate_random_state(self):
        return tuple(random.randint(0, N-1) for _ in range(N))

    def crossover(self, state1, state2):
        point = random.randint(1, N - 2)
        return state1[:point] + state2[point:]

    def mutate(self, state):
        state = list(state)
        col = random.randint(0, N-1)
        state[col] = random.randint(0, N-1)
        return tuple(state)

# ====== 5. Backtracking (CSP) ======
solution_bt_ac3 = backtrack(problem_csp)  # mặc định inference=True
print("Backtracking + AC3:", solution_bt_ac3)
print_board(solution_bt_ac3, "Backtracking + AC3 Solution")
analyze_solution(solution_bt_ac3)

solution_bt_noac3 = backtrack(problem_csp, inference=False)
print("Backtracking (no AC3):", solution_bt_noac3)
print_board(solution_bt_noac3, "Backtracking without AC3 Solution")
analyze_solution(solution_bt_noac3)

# ====== 6. Local Search (HC, SA, GA) ======
problem_local = FiveQueensProblem()

solution_hc = hill_climbing(problem_local, iterations_limit=1000)
print("Hill Climbing:", solution_hc.state)
print_board(solution_hc.state, "Hill Climbing Solution")
analyze_solution(solution_hc.state)

solution_sa = simulated_annealing(problem_local, iterations_limit=1000)
print("Simulated Annealing:", solution_sa.state)
print_board(solution_sa.state, "Simulated Annealing Solution")
analyze_solution(solution_sa.state)

solution_ga = genetic(problem_local, population_size=50, mutation_chance=0.2, iterations_limit=200)
print("Genetic Algorithm:", solution_ga.state)
print_board(solution_ga.state, "Genetic Algorithm Solution")
analyze_solution(solution_ga.state)
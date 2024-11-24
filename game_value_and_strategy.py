from ortools.linear_solver import pywraplp
import numpy as np

def solve_zero_sum_game(payoff_matrix):
    """
    Solves a zero-sum game using linear programming.
    
    Args:
        payoff_matrix (np.ndarray): The payoff matrix for the game
        
    Returns:
        tuple: (game_value, optimal_strategy)
            - game_value (float): The value of the game
            - optimal_strategy (list): Optimal mixed strategy probabilities
    """
    payoff_matrix = np.array(payoff_matrix)
    m, n = payoff_matrix.shape
    
    # Create solver
    solver = pywraplp.Solver.CreateSolver('GLOP')
    if not solver:
        return None, None

    # Variables: x1, x2, ..., xn (probabilities) and v (game value)
    x = [solver.NumVar(0, 1, f'x_{i+1}') for i in range(n)]
    v = solver.NumVar(-solver.infinity(), solver.infinity(), 'v')
    
    # Constraint: sum of probabilities = 1
    solver.Add(sum(x) == 1)
    
    # Constraints for minimizing maximum payoff
    for i in range(m):
        solver.Add(
            sum(payoff_matrix[i][j] * x[j] for j in range(n)) >= v
        )
    
    # Objective: maximize v
    solver.Maximize(v)
    
    # Solve
    status = solver.Solve()
    
    if status == pywraplp.Solver.OPTIMAL:
        game_value = v.solution_value()
        optimal_strategy = [x[i].solution_value() for i in range(n)]
        return game_value, optimal_strategy
    else:
        return None, None 
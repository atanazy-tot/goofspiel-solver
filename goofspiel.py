from itertools import combinations
import numpy as np
from game_value_and_strategy import solve_zero_sum_game

def calculate_subgame_values(k: int, subgame_values: dict, num_cards: int):
    """
    Calculates optimal strategies for subgames of size k.
    
    Args:
        k (int): Size of the subgame (number of cards in each player's hand)
        subgame_values (dict): Dictionary storing values of smaller subgames
        num_cards (int): Total number of unique cards in the game
        
    Returns:
        dict: Updated subgame_values dictionary with new computed values
    """
    if k < 0:
        return 0
    
    elif k == 1:
        # Base case: games with single cards
        for A in combinations(range(1, num_cards + 1), k):
            for B in combinations(range(1, num_cards + 1), k):
                for C in combinations(range(1, num_cards + 1), k):
                    a, b, c = A[0], B[0], C[0]
                    if a > b:
                        subgame_values[A, B, C] = c
                    elif a < b:
                        subgame_values[A, B, C] = -c
                    else:
                        subgame_values[A, B, C] = 0
    
    else:
        # Recursive case: larger subgames
        for A in combinations(range(1, num_cards + 1), k):
            for B in combinations(range(1, num_cards + 1), k):
                for C in combinations(range(1, num_cards + 1), k):
                    sub_sums = 0
                    for c in C:
                        payoff_list = []
                        for a in sorted(A):
                            for b in sorted(B):
                                if a > b:
                                    p = c
                                elif a < b:
                                    p = -c
                                else:
                                    p = 0
                                
                                As = tuple(sorted(set(A) - {a}))
                                Bs = tuple(sorted(set(B) - {b}))
                                Cs = tuple(sorted(set(C) - {c}))
                                payoff_list.append(p + subgame_values[As, Bs, Cs])
                        
                        # Convert to square matrix
                        n = int(np.sqrt(len(payoff_list)))
                        payoff_matrix = np.array(payoff_list).reshape(n, n)
                        
                        # Solve the game
                        game_value, strategies = solve_zero_sum_game(payoff_matrix)
                        
                        # Reverse the strategies list before printing
                        strategies = strategies[::-1]
                        
                        print(f'For A: {A}, B: {B}, C: {C} and revealed card: {c} '
                              f'game value is {round(float(game_value), 4)}')
                        print(f'Optimal strategy for first player: '
                              f'{[round(float(s), 4) for s in strategies]}\n')
                        
                        sub_sums += round(float(game_value), 4)
                    
                    # Calculate expected value
                    subgame_values[A, B, C] = round(sub_sums / len(C), 4)
                    print(f'Expected value for the game: {subgame_values[A, B, C]}.\n')
    
    return subgame_values 
from goofspiel import calculate_subgame_values

def main():
    # Initialize parameters
    N = 6  # number of cards
    subgame_values = dict()
    
    # Calculate values for increasing subgame sizes
    for k in range(1, N + 1):
        print(f"\nCalculating strategies for subgames of size {k}...")
        subgame_values = calculate_subgame_values(k, subgame_values, N)

if __name__ == "__main__":
    main() 
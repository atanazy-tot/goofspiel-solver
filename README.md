# Goofspiel Solver: Linear Programming Approach to Game of Pure Strategy

This project implements a solver for the Goofspiel card game (also known as GOPS - Game Of Pure Strategy) using linear programming techniques. The implementation is based on the methodology described in:

> Rhoads, G. C.; Bartholdi, L. (2012). "Computer Solution to the Game of Pure Strategy". Games. 3 (4): 150–156.

## What is Goofspiel?

Goofspiel is a two-player card game that exemplifies strategic decision-making under uncertainty. The game uses a standard deck of cards with the following setup:

- Remove all cards of one suit
- Give one suit to each player
- Use the remaining suit as a prize deck (shuffled and placed face-down)

Card values range from low to high: Ace=1, 2, 3, ..., 10, Jack=11, Queen=12, King=13.

### Gameplay

1. Each round begins by revealing the top card from the prize deck
2. Players simultaneously select one card from their hand
3. The player who plays the higher card wins the value of the prize card
4. If cards are equal, the prize points are split
5. All played cards are discarded
6. Game continues for 13 rounds
7. Winner is the player with the most points (46+ points needed to win)

## Mathematical Formulation

### Zero-Sum Game Representation

Let's define the game formally:
- Let $A$ be the payoff matrix where $a_{ij}$ represents the payoff when Player 1 plays strategy $i$ and Player 2 plays strategy $j$
- Let $x$ be Player 1's mixed strategy vector
- Let $y$ be Player 2's mixed strategy vector
- The game value $v$ represents the expected payoff under optimal play

### Linear Programming Solution

The zero-sum game can be represented as a minimax problem:

$v = \max_x \min_y x^T A y$

subject to:
$$
\begin{align*}
\sum_{i=1}^n x_i &= 1 \\
x_i &\geq 0 \quad \forall i
\end{align*}
$$

This can be reformulated as the linear program:

$$
\begin{align*}
\text{maximize} \quad & v \\
\text{subject to} \quad & \sum_{i=1}^n x_i = 1 \\
& x_i \geq 0 \quad \forall i \\
& (Ay)_i \geq v \quad \forall i
\end{align*}
$$

### Subgame Value Calculation

For a subgame with cards sets $A$, $B$, and prize cards $C$, the value function $V(A,B,C)$ is calculated recursively:

$$
V(A,B,C) = \frac{1}{|C|} \sum_{c \in C} v_c
$$

where $v_c$ is the value of the subgame when card $c$ is revealed, computed as:

$$
v_c = \text{val}\begin{pmatrix}
p(a_1,b_1,c) + V(A\setminus\{a_1\}, B\setminus\{b_1\}, C\setminus\{c\}) & \cdots & p(a_1,b_n,c) + V(A\setminus\{a_1\}, B\setminus\{b_n\}, C\setminus\{c\}) \\
\vdots & \ddots & \vdots \\
p(a_n,b_1,c) + V(A\setminus\{a_n\}, B\setminus\{b_1\}, C\setminus\{c\}) & \cdots & p(a_n,b_n,c) + V(A\setminus\{a_n\}, B\setminus\{b_n\}, C\setminus\{c\})
\end{pmatrix}
$$

where:
- $p(a,b,c)$ is the immediate payoff function:
$$
p(a,b,c) = \begin{cases}
c & \text{if } a > b \\
0 & \text{if } a = b \\
-c & \text{if } a < b
\end{cases}
$$

### Base Cases

For single-card subgames ($|A| = |B| = 1$):

$$
V(\{a\}, \{b\}, \{c\}) = \begin{cases}
c & \text{if } a > b \\
0 & \text{if } a = b \\
-c & \text{if } a < b
\end{cases}
$$

### Optimal Strategy Properties

The optimal strategy $x^*$ satisfies:

1. Nash Equilibrium condition:
   $$x^{*T} A y^* \geq x^T A y^* \quad \forall x$$

2. Expected value guarantee:
   $$\mathbb{E}[payoff] \geq v \quad \text{against any strategy}$$

## Implementation

The solver uses dynamic programming to build solutions from smaller subgames to larger ones. For a game with $n$ cards, the complexity is:

- Time complexity: $O(n! \cdot n^2)$
- Space complexity: $O(n^3)$

## Performance Analysis

For a game with $n$ cards, we need to solve:
- $\binom{n}{k}^3$ subgames of size $k$
- Each subgame requires solving a $k \times k$ linear program

The total number of linear programs solved is:
$$\sum_{k=1}^n \binom{n}{k}^3$$

## Usage

[Installation and usage instructions to be added]

## Mathematical Optimality

The solver guarantees:
1. Nash equilibrium strategies
2. Optimal expected payoff against rational opponents
3. Minimization of exploitability

## Performance Considerations

The computational complexity grows with:
- Number of cards (N)
- Size of subgames (k)
- Number of possible game states (O(N!))

For practical purposes, the implementation is optimized for games up to N=6 cards, though it can theoretically handle larger games with sufficient computational resources.

## References

1. Rhoads, G. C.; Bartholdi, L. (2012). "Computer Solution to the Game of Pure Strategy". Games. 3 (4): 150–156.
2. Ross, S. M. (1971). "Goofspiel — the game of pure strategy". Journal of Applied Probability, 8(3), 621-625.
3. [Additional relevant references to be added]

## License

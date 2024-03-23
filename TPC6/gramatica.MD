
# Projecto:
?a
b = a * 2 / (27 - 3)
! a + b 
c = a * b / (a/b)

## gramatica:
P -> C P | ε
C -> E | A | S
E -> ? V
S -> ! X
A -> V = X
X -> X + T | X - T | T
T -> T * F | T / F | F
F -> ( X ) | N | V
V = [a-b]+
N = [0-9]+
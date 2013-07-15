calc
====

A very simple calculator based on a recursive descent parser (not
using python `eval`)

Supports exponentiation, add, sub, mul, div, modulo/formatting,
shift, bitwise and/or/xor, comparison operators, logical and/or
(not short-circuited), unary negation, parenthesized subexpressions
and assignment (an operator like in C, not a statement like in Python).

Atoms can be integers, floats, strings or variables.

It's also possible to store an expression in a variable (like a spreadsheet
formula) using the `:=` operator. No check about circular formulas is present.

The core parser/evaluator is about 40 lines. The whole program is less
than 100 lines in total.

Works in both Python 2.x and 3.x

Example session:

    > 1 + 1
    2
    > 1 + 2*3
    7
    > 1 + 2*(3 + 4)
    15
    > pi = 3.141592654
    3.141592654
    > r = 10
    10
    > r * r * pi
    314.1592654
    > area := r * r * pi
    314.1592654
    > r = 100
    100
    > area
    31415.92654
    > r =42
    42
    > area
    5541.76944166

calc
====

A very simple calculator based on a recursive descent parser (not
using python `eval`)

Supports exponentiation, add, sub, mul, div, modulo/formatting,
shift, bitwise and/or/xor, comparison operators, logical and/or
(not short-circuited), unary negation, parenthesized subexpressions
and assignment (an operator like in C, not a statement like in Python).

Atoms can be integers, floats, strings or variables.

The core parser/evaluator is about 40 lines. The whole program is less
than 100 lines in total.

Works in both Python 2.x and 3.x

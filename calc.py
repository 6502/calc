import re, sys

ops = {"**":  (1, "R", lambda x, y: value(x) ** value(y) ),
       "*":   (2, "L", lambda x, y: value(x) * value(y)  ),
       "/":   (2, "L", lambda x, y: value(x) / value(y)  ),
       "%":   (2, "L", lambda x, y: value(x) % value(y)  ),
       "+":   (3, "L", lambda x, y: value(x) + value(y)  ),
       "-":   (3, "L", lambda x, y: value(x) - value(y)  ),
       "<<":  (4, "L", lambda x, y: value(x) << value(y) ),
       ">>":  (4, "L", lambda x, y: value(x) >> value(y) ),
       "|":   (5, "L", lambda x, y: value(x) | value(y)  ),
       "&":   (5, "L", lambda x, y: value(x) & value(y)  ),
       "^":   (5, "L", lambda x, y: value(x) ^ value(y)  ),
       "<":   (6, "L", lambda x, y: value(x) < value(y)  ),
       "<=":  (6, "L", lambda x, y: value(x) <= value(y) ),
       ">":   (6, "L", lambda x, y: value(x) > value(y)  ),
       ">=":  (6, "L", lambda x, y: value(x) >= value(y) ),
       "==":  (6, "L", lambda x, y: value(x) == value(y) ),
       "!=":  (6, "L", lambda x, y: value(x) != value(y) ),
       "and": (7, "L", lambda x, y: value(x) and value(y)),
       "or":  (8, "L", lambda x, y: value(x) or value(y) ),
       "=":   (9, "R", lambda x, y: (vars.__setitem__(name(x), value(y)),
                                     value(y))[1])}

vars = {}

def value(x):
    return vars[x[0]] if isinstance(x, tuple) else x

def name(x):
    if isinstance(x, tuple):
        return x[0]
    raise RuntimeError("Only variables can be assigned")

number = "[0-9]+(?:\\.[0-9]*)?(?:[EeDd][-+]?[0-9]+)?"
string = "\"(?:[^\"\\\\]|\\\\.)*\""
var = "[A-Za-z_][A-Za-z0-9_]*"

tkexpr = ("|".join(map(re.escape, sorted(ops.keys(), key=len, reverse=True))) +
          "|[()]" +
          "|" + number +
          "|" + string +
          "|True|False" +
          "|" + var +
          "|[^ ]")

def expr(tk, i, level=max(v[0] for v in ops.values())):
    if level == 0:
        if tk[i] == "-":
            x, i = expr(tk, i + 1, 0)
            return -x, i
        if tk[i] == "(":
            x, i = expr(tk, i + 1)
            if tk[i] != ")": raise RuntimeError("')' expected")
            return x, i+1
        if len(tk[i]) > 1 and tk[i][0] == "\"":
            return tk[i][1:-1], i + 1
        if tk[i] in ("True", "False"):
            return tk[i] == "True", i + 1
        if re.match(var, tk[i]):
            return (tk[i],), i + 1
        try:
            return int(tk[i]), i + 1
        except ValueError:
            return float(tk[i]), i + 1
    else:
        x, i = expr(tk, i, level - 1)
        op = ops.get(tk[i])
        while op and op[0] == level:
            y, i = expr(tk, i + 1, level - (op[1] == "L"))
            x = op[2](x, y)
            op = ops.get(tk[i])
        return x, i

def calc(s):
    tk = re.findall(tkexpr, s) + ["#"]
    x, i = expr(tk, 0)
    if tk[i] != "#":
        raise RuntimeError("Extra tokens at end of expression")
    return value(x)

if __name__ == "__main__":
    if sys.version_info < (3,):
        input = raw_input

while True:
    print("%r" % calc(input("> ")))
from sys import stdin

groups = {}

def is_op(token):
    return token in ['union', 'difference', 'intersection']

def evalexp(tokens):
    stack = [groups[tokens.pop()]]
    while tokens:
        t = tokens.pop()
        if is_op(t):
            res = eval('stack.pop().' + t + '(stack.pop())')
            stack.append(res)
        else:
             stack.append(groups[t])
    return stack[0]

empties = 0
for line in stdin:
    tokens = line.strip().split()
    if tokens[0] == 'group':
        groups[tokens[1]] = set(tokens[3:])
        for p in groups[tokens[1]]:
            groups[p] = set([p])
    else:
        empties += not evalexp(tokens)

print empties

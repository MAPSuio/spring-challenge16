from sys import stdin

expressions = map(lambda line: line.strip(), stdin.readlines())

balanced = 0

begin_brace = {}
begin_brace[")"] = "("
begin_brace["]"] = "["
begin_brace["}"] = "{"


for expression in expressions:
    stack = []
    stack_touched = False

    for brace in expression:

        if brace in ["{", "(", "["]:
            stack.append(brace)
            stack_touched = True

        elif len(stack) > 0 and stack[-1] == begin_brace[brace]:
                stack.pop()

    if len(stack) == 0 and stack_touched:
        balanced += 1

print balanced

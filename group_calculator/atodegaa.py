from sys import stdin

inp = stdin.readlines()
group_statements = [i.split() for i in inp if i.startswith("group")]

groups = {}
for statement in group_statements:
    groups[statement[1]] = set(statement[3:])

selection_statements = [i.split() for i in inp if not i.startswith("group")]

keywords = ["union", "intersection", "difference"]
def parser(expression):
    stack = []
    for word in expression:
        if word in keywords:
            stack.append(word)
        else:
            if stack == []:
                return groups[word]
            elif stack[-1] in keywords:
                stack.append(groups[word])
            else:
                stack.append(groups[word])
                while len(stack) > 2:
                    if stack[-3] not in keywords:
                        break
                    if stack[-2] in keywords:
                        break
                    gp1 = stack.pop()
                    gp2 = stack.pop()
                    op = stack.pop()
                    if op == "union":
                        stack.append(gp1 | gp2)
                    elif op == "intersection":
                        stack.append(gp1 & gp2)
                    else:
                        stack.append(gp2 - gp1)
    return stack[0]

count = 0
for statement in selection_statements:
    gp = parser(statement)
    if len(gp) == 0:
        count += 1
print count

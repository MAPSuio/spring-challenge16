from random import choice, sample, randint

#####Generating the data set for the problem Group Calculator
girls = ["Emma", "Nora", "Sara", "Sofie", "Olivia", "Emilie", "Ella", "Lea", "Maja", "Khaleesi", "Jennifer", "Barbara", "Ashley", "Fiona", "Mary", "Tiril", "Solveig", "Hanne", "Clare"]
boys = ["William", "Matias", "Oliver", "Jakob", "Lukas", "Filip", "Liam", "Aksel", "Emil", "Oskar", "Donald", "Nate", "Harry", "Ole", "Geoff", "Michael", "Jack", "Ryan"]
people = girls + boys
groupnames = ["geeks", "nerds", "jocks", "mathematicians", "engineers", "gamers", "politicians", "students", "journalists", "photographers", "constables", "fashionistas", "alcoholics", "builders", "actors", "soldiers", "athletes"]

groups = {"unstumpables": ["Donald"]}

for group in groupnames:
    num = randint(2, len(people))
    members = sample(people, num)
    s = str(members)[1:-1].replace("'", "")
    s = s.replace(",", "")
    print "group", group, num, s

print "group", "unstumpables", 1, "Donald"

keywords = ["union", "intersection", "difference"]

rules = groupnames + keywords
for _ in xrange(1000):
    expression = [choice(keywords), False, False]
    while False in expression:
        new_expression = []
        for x in expression:
            if x != False:
                new_expression.append(x)
            else:
                rule = choice(rules)
                if rule not in keywords:
                    new_expression.append(rule)
                else:
                    new_expression.append(rule)
                    new_expression.append(False)
                    new_expression.append(False)
        expression = new_expression
    s = str(expression).replace("'", "")
    s = s[1:-1].replace("," ,"")
    print s
print len(people)

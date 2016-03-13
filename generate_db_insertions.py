from os import path
from os import walk

CONTEST_START = "new Date"

def create_entry(root, files):

    answer_fd = open(path.join(root, 'answer.md'), 'ro')
    answer = answer_fd.readlines()[0].strip()
    answer_fd.close()

    description_fd = open(path.join(root, 'README.md'), 'ro')
    description = description_fd.readlines()
    description_fd.close()

    title = description[0].strip()[2:]

    print "    Problems.insert"
    print "      title: " + "\"" + title + "\""
    print "      solution: " + "\"" + answer + "\""
    print "      answers: []"
    print "      draft: false"
    print "      activeFrom: " + CONTEST_START
    print "      description:" + "\"\"\"" + "".join(description[1:]) + "\"\"\""


print "Meteor.startup ->"
print "  if Problems.find().count() is 0"

for root, _, files in walk('.'):

    if root == ".":
        continue

    if root.startswith('./.git'):
        continue

    create_entry(root, files)

print  "if Meteor.users.find().count() is 1\n Meteor.users.update {}, {$set: {isAdmin: true}}"


##Group calculator

Playing the popularity game is all about getting yourself into the right groups. If you are on the football team and the honor roll, this might impress some people. If you are in the AV club, chess club, and academic probation, perhaps not so much. For this problem, develop a program that computes the set of people inside or outside various groups.

[This file](https://gist.githubusercontent.com/cmrosenberg/5944a94d75a7d4b2af8b/raw/84c7f23e8733df951847a6fdbb30510250c227ec/gistfile1.txt)
begins with the description of a collection of 18 groups. Each group starts with a line of the form “group X n” where X is the name of the group and 1≤n≤37 is the number of people in the group. This is followed by n individual names, all on the same line. Group names and individual names are sequences of upper and lower-case letters.

The group descriptions will be followed by 1000 selection expressions, one per line. A selection expression is an expression in Polish notation for identifying a set of individuals and may take one of the following forms:

* G - Where G is the name of a group, selects the set of individuals in group G.
* union S1 S2 - Where S1 and S2 are selection expressions, selects the set of individuals in (selected by) either S1 or S2
* intersection S1 S2 - Where S1 and S2 are selection expressions, selects the set of individuals in both S1 and S2
* difference S1 S2 - Where S1 and S2 are selection expressions, selects the set of individuals in S1 but not in S2

Each selection expression contains up to 100 group names and set operations.

The sequence of select statements ends at the end of file. No group will have the name group, union, intersection or difference. Different people will have different names; different groups will have different names.

How many of the 1000 selection expressions evaluate to a set with no members, the empty set?

### Sample Input

*  group geeks 6 Jennifer Sofie Aksel Ella Michael Oliver
*  group students 4 Hanne Khaleesi Emil Olivia
*  group unstumpables 1 Donald
*  union geeks students
*  intersection geeks union student unstumpables

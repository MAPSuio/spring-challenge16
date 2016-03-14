# 15 Movie Bucket

Ole is weirdo. Firstly, he only watches and buys films that are among
the top 200 grossing US box office films adjusted for inflation.
Secondly, Ole keeps his Blu-Ray movies stacked in a deep bucket. All
films are unique. [This file](https://gist.githubusercontent.com/cmrosenberg/063797d95318b2af3a07/raw/3b5bf3508e1ff14c549a7068774ef308d0fa6479/gistfile1.txt)
gives  a history of when Ole

* buys new films (adds them on top of the stack)
* sells films (removes them from the stack)
* watches films (finds them in the stack, watches them, then puts them back on
  top of the stack)

How deep into the stack is the movie "Gone with the Wind"?

Ole is human, so he uses 1-based indexing: That is, if "Gone with the
Wind" is on top of the stack, the answer is 1, and so forth.

The dataset is encoded in the following way:

```
buys The Matrix
watches The Matrix
sells The Matrix
```

*An error in the input dataset was detected during the competittion. The correct answer,
given the dataset that was given in the competition is 249.*

# 09 Frenemies

![Image frenemies](https://dl.dropboxusercontent.com/u/1833533/trump.jpg)

Some people are friends, but secretly hate each other: They are
*frenemies*. Specifically, we will say that x and y are *frenemies* if

1. x and y are friends, and
2. x hates y, and
3. y hates x

[This file](https://gist.githubusercontent.com/cmrosenberg/213e8bfff3c9c3253568/raw/11627d7bb903c0da822d1d4561c27bd57cb004e8/gistfile1.txt)
gives a history of friendship formations and moments in time when a person
hates another, determine the number of *pairs* of frenemies.

The dataset has the following format:

```
friends alice bob
alice hates bob
bob hates alice
friends alice mallory
...
```

The first line means that alice and bob are friends.
The second line means that alice hates bob.

You can assume that

1. All names are hononyms (ie. consist of one word)
2. There are no redundant lines in the dataset.

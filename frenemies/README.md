# Frenemies

![Image frenemies](http://saintpetersblog.com/wp-content/uploads/2016/03/Trump-and-Christie-hostage-840x440.jpg)

Some people are friends, but secretly hate each other: They are
*frenemies*. Specifically, we will say that x and y are *frenemies* if

1. x and y are friends, and
2. x hates y, and
3. y hates x

Given a history of friendship formations and moments in time when a person
hates another, determine the number of *pairs* of frenemies

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

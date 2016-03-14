# 10 Frengers

*Frengers*, apart from being the title of an absolutely essential Pop Rock album,
is the concept of being "not quite friends, not quite strangers". You probably
have a few frengers here at IFI.

For our purposes, we will say that two people are *frengers* if they

1. have met, and
2. have at least 3 friends in common, but
3. are not themselves friends.

[This file](https://gist.githubusercontent.com/cmrosenberg/9b65d73805127ac4fe4c/raw/47c5add5a3c0004d41a26bed1bd9757e3cb6c015/gistfile1.txt)
gives a history of meetings and friendship formations.  Determine how many *pairs* of people are frengers.

You can assume that each name refers to one and and only one person.
All names are mononyms – they consist of only one word.

The dataset is of the following format:

```
friends kari per
meet kari ola
...
```

The first entry says that kari and per are friends
The second entry says kari and per have met.

Example:

```
friends kari per
meet kari ola
friends kari petter
friends kari martin
friends kari lone
friends ola petter
friends ola martin
friends ola lone
```
Answer: 1

The answer is one, because kari and ola are frengers.

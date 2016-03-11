# Sorting diamonds

![Image diamond](https://upload.wikimedia.org/wikipedia/commons/d/d3/Playing_card_diamond_A.svg)

You are given all the cards of a given suit (13 cards) from a standard
deck of cards.

We want to be able to do a neat trick, and we need your help to figure
out the starting configuration of the stack.

Here is the neat trick: Starting with our cards in a stack, we want to
place every card on the table in increasing order, starting with the Ace
and ending with the King (1 2 3 4 5 6 7 8 9 10 11 12 13) by executing
the following algorithm:

1. Put the card on top of the stack on the table
2. If the stack is empty, terminate.
3. Put the card currently on top of the stack, at the bottom of the stack
4. Go to step 1.

How must the 13 cards be sorted for this trick to work?

Give your answer as a space-separated string, with the topmost card to the left, like so:
         1 13 12 11 10 9 8 7 6 5 4 3 2

# 14 Words, Words, Words


[This file](https://gist.githubusercontent.com/cmrosenberg/45153f04750aebde65f2/raw/9df26ecd54dc7d35856fb1ae45052aa04b933680/gistfile1.txt)
 contains 10,000 (lowercase) English words. When interpreting this
collection of words in a special way, you can find a secret word.

Each word is given a MAPS-score, which is the sum of the ASCII values of
each of its characters plus 10. We do not count the newline character as
part of the word. As an example, the MAPS-score of the word `stop` is
`115 + 116 + 111 + 112 + 10 = 464`.

Each block of 1000 words encodes a single character.You decipher the
character in the following manner: Determine the MAPS-score for each
word. Sum all these scores, then take the remainder when dividing by
128. You will now have an ASCII value. The corresponding character is
the character you're looking for.

To discover the hidden word, find the character encoded by the first
1000 words, then the second character from the next 1000 words and so on.

Note: The hidden word contains both upper and lower case letters.

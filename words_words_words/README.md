##Words, Words, Words


The file `data.txt` contains 10,000 (lowercase) English words. Your challenge is to find a special, familiar word which is encoded by this collection of words.

Each word is given a MAPS-score, which is the sum of the ASCII-values of each of its characters, and added 10 (which is the ASCII-value of a newline character).*

Each block of 1000 words encodes a character as such: Take the sum of the MAPS-score of each word, add it all together, and take the remainder when dividing by 128. Then take the character which has that number as its ASCII-value.

To discover the hidden word, the first character is encoded by the first 1000 words, the second character is encoded by the next 1000 words and so on.


\*As an example, the MAPS-score of the word `stop` is `115 + 116 + 111 + 112 + 10 = 464`.

main = print $ head $ dropWhile (\x -> x * x < 1234567890) [1..]

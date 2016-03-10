dual ')' = '('
dual ']' = '['
dual '}' = '{'

isOpen  = flip elem "([{"
isClose = flip elem ")]}"

closes x y = isClose x && dual x == y

isBalanced' []     ys     = null ys
isBalanced' (x:xs) []     = isBalanced' xs [x]
isBalanced' (x:xs) (y:ys) | x `closes` y = isBalanced' xs ys
                          | isOpen x     = isBalanced' xs (x:y:ys)
                          | otherwise    = False

isBalanced xs = isBalanced' xs []

main = do
  content <- getContents
  print $ length $ filter isBalanced $ lines content

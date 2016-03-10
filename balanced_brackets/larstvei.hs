isBalanced xs = null $ foldl f [] xs
    where f ('(':xs) ')' = xs
          f ('[':xs) ']' = xs
          f ('{':xs) '}' = xs
          f xs        y  = y:xs

main = do
  content <- getContents
  print $ length $ filter isBalanced $ lines content

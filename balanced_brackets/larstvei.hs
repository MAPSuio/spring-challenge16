isBalanced xs = null $ foldl f [] xs
    where f ('(':ys) ')' = ys
          f ('[':ys) ']' = ys
          f ('{':ys) '}' = ys
          f ys        x  = x:ys

main = do
  content <- getContents
  print $ length $ filter isBalanced $ lines content

import Data.List (nub)

main = do
  contents <- getContents
  let lns = lines contents
  print $ length lns - (length . nub) lns

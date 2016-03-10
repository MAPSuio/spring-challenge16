paren '(' = 1
paren ')' = -1

(.&&.) f g a = (f a) && (g a)

isBalanced = (((==0) . last) .&&. all (>=0)) . scanl1 (+) . map paren

main = do
  content <- getContents
  print $ length $ filter isBalanced $ lines content

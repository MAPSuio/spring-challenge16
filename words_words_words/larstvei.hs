import Data.Char (ord, chr)

chunksOf _ [] = []
chunksOf n xs = take n xs : (chunksOf n $ drop n xs)

score = (+10) . sum . map ord
word = chr . (`rem` 128) . sum

main = do
  contents <- getContents
  let scores = map (word . map score) $ chunksOf 1000 $ lines contents
  putStrLn scores

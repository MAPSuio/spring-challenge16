import Data.List.Split (chunksOf)
import Data.Char (ord, chr)

score = (+10) . sum . map ord
word = chr . (`rem` 128) . sum

main = do
  contents <- getContents
  let scores = map (word . map score) $ chunksOf 1000 $ lines contents
  print scores

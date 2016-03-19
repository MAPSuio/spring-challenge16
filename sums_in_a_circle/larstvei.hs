import Data.Graph
import Data.Array

buildEdges n = filter p [(x,y) | x <- [1..n], y <- [1..n]]
    where p (x, y) = x + y <= n && x /= y

build n = buildG (1, n) $ buildEdges n

solutions 0 xs v g | elem 1 (g!v) && (v+1) `notElem` xs = [v+1 : v : xs]
                   | otherwise    = []
solutions i xs v g = concatMap f ys
    where ys = filter p $ g!v
          p y = y `notElem` xs && v+y `notElem` xs
          f y = solutions (i-1) (v+y : v : xs) y g

solve n = solutions ((n `quot` 2) - 1) [] 1 $ build n

main = (print . (`quot` 2) . length . solve) 20

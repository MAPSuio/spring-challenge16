main = print $ length $ takeWhile (<74207281) maps
    where maps = 26 : 47 : zipWith (+) maps (tail maps)

-- Alternativ 1
-- Løs for n og m
f (n,m) = n * m == 3240 && 2*n + 2*m - 4 == 230

main = let pairs  = concatMap (\a -> zip (repeat a) [a..3240]) [1..3240]
           (n, m) = head $ filter f pairs in
       putStrLn $ show n ++ " " ++ show m

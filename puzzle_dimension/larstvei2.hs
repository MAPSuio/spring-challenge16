-- Alternativ 2
-- Sett inn for n og løs for m
f m = 2 * (3240/m) + 2*m - 4 == 230

main = let [n, m] = map round $ filter f [1..3240] in
       putStrLn $ show n ++ " " ++ show m

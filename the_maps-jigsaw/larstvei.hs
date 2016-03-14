isqrt = floor . sqrt . fromIntegral

divides n = (==0) . (mod n)

minedges n = (i, n `quot` i)
    where m = isqrt n
          i = head $ filter (divides n) [m,m-1..1]

edgepieces (n, m) | n == 1 = m
                  | otherwise = 2*n + 2*m - 4

main = print $ edgepieces $ minedges 8387035452956160000

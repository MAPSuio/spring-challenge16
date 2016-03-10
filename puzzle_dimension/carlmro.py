edge_bricks = 230
total_bricks = 3240

if (edge_bricks+4) % 4 == 0:
    x = (edge_bricks+4) / 4
    y = (edge_bricks+4) / 4

    while x*y != total_bricks:
        x += 1
        y -= 1

    print y, x
else:
    x = (edge_bricks+4) / 4
    y = (edge_bricks+4) / 4 + 1

    while x*y != total_bricks:
        x += 1
        y -= 1

    print y, x

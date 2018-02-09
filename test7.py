def hanioTower(n, a, b, c):
  if n <= 1:
    print(a, '->', c)
  else:
    hanioTower(n-1, a, c, b)
    print(a, '->', c)
    hanioTower(n-1, b, a, c)

hanioTower(10, 'A', 'B', 'C')

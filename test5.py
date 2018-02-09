# -*- coding:UTF-8 -*-
num = input('please input a number:')
n = int(num)
for i in range(2, n):
  m = int(i ** 0.5)
  b = True
  for j in range(2, m):
    if i % j == 0:
      b = False
      break
  if b == True:
    print(i)




for ii in range(1, 10):
  for jj in range(1, 10):
    print(ii, 'x' , jj, '=', ii * jj, end='\t')
  print()

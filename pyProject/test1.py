# -*- coding:UTF-8 -*-

x = input('请输入一个年份：')
print(x)
year = int(x)
if year % 400 == 0:
  print("%d是闰年！"%(year))
elif year % 100 == 0:
  print("%d是不是闰年！"%(year))
elif year % 4 == 0:
  print("%d是闰年！"%(year))
else:
  print("%d是不是闰年！"%(year))
  

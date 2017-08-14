ench_num = 0
ench = " "
while ench_num <= 255:
  ench += "{id:" + str(ench_num) + ",lvl:10}"
  if ench_num != 255:
    ench += ", "
  ench_num += 1




print("/give @p minecraft:golden_leggings 1 0 {ench:[" + ench + "], Unbreakable:1}")

